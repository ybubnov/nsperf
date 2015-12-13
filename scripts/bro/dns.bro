# Custom DNS events.
@load policy/frameworks/communication/listen
@load base/protocols/dns/main

redef Communication::nodes += {
    ["api"] = [$host=127.0.0.1, $connect=F, $ssl=F]
};

global custom_dns_request: event(msg: dns_msg, query: string, qtype: count, qclass: count);

event dns_request(c: connection, msg: dns_msg, query: string, qtype: count, qclass: count) &priority=5
    {
    event custom_dns_request(msg, query, qtype, qclass);
    }

import select

import broccoli as bro


dns_msg = bro.record_type(
    "id", "opcode", "rcode", "QR", "AA", "TC", "RD", "RA",
    "Z", "num_queries", "num_answers", "num_auth", "num_addl")


@bro.event(dns_msg, bro.string, bro.count, bro.count)
def custom_dns_request(msg, query, qtype, qclass):
    print(msg, query, qtype, qclass)

conn = bro.Connection("127.0.0.1:47760", connect=False)

conn.connect()
fd = bro.bro_conn_get_fd(conn.bc)

while True:
    r, _, _ = select.select([fd], [], [])
    conn.processInput()

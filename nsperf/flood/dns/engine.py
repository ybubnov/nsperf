import socket

import dns.name
import dns.message
import dns.rdatatype


class DomainNameSystemEngine(object):
    """ Engine to generate DNS packets.
    """
    __protocol_port = 53

    def __init__(self, **kwargs):
        """ Initialize a new instance of the engine.
        """
        self._resource_record = kwargs.get("resource_record")
        self._local_address = kwargs.get("local_address")
        self._remote_address = kwargs.get("remote_address")

    def _build_packet(self):
        """ Returns a new DNS packet.
        """
        domain = dns.name.from_text('google.com')
        rdatatype = dns.rdatatype.from_text(self._resource_record)

        if not domain.is_absolute():
            domain = domain.concatenate(domain.name.root)

        request = dns.message.make_query(domain, rdatatype)
        return request.to_wire()

    def establish_connection(self):
        """ Create a UDP socket and bind in to the specified local address.
        """
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.bind((self._local_address, self.__protocol_port))

    def spawn(self):
        """ Generate DNS packages with specified options.
        """
        dns_packet = self._build_packet()
        endpoint = (self._remote_address, self.__protocol_port)

        self._socket.sendto(dns_packet, endpoint)

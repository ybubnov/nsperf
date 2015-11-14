import argparse
import sys
import time

import nsperf.flood.dns.engine


def main():
    """ Entry point of the command.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t",
        "--type",
        type=str,
        required=False,
        help="Resource record type.")

    parser.add_argument(
        "-c",
        "--count",
        type=int,
        required=False,
        help="Specifies the count of packets to be sent.")

    parser.add_argument(
        "-f",
        "--force",
        default=False,
        action="store_true",
        help="Flood with packages.")

    parser.add_argument(
        "--allow-requests",
        default=True,
        action="store_true",
        help="Allow to send DNS queries.")

    parser.add_argument(
        "--allow-responses",
        default=False,
        action="store_true",
        help="Allow to send DNS responses.")

    parser.add_argument(
        "--local-address",
        required=True,
        help="Ingress package address.")

    parser.add_argument(
        "--remote-address",
        required=True,
        help="Egress package address.")

    args = parser.parse_args()

    engine = nsperf.flood.dns.engine.DomainNameSystemEngine(
        resource_record=args.type,
        local_address=args.local_address,
        remote_address=args.remote_address)

    engine.establish_connection()

    while True:
        try:
            engine.spawn()
            time.sleep(1)
            sys.stdout.write(".")
            sys.stdout.flush()
        except KeyboardInterrupt:
            return

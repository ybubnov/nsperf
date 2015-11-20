# minilinc

minilinc is a another damn simple unility made on a knee to not recall the arguments of the _mn_.

## Get started

By default minilinc creates a Open vSwitch with OpenFlow version 1.3 support apart with three hosts.
Each host will invoke the ```nsperf``` utility to send every second a DNS query request, so you should not care about crafting of the packet-in packages to validate OpenFlow controller.

To launch a ```minilinc``` you should invoke the following commands:
```bash
$ minilinc --address=10.0.0.1 \  # Address of the your OpenFlow controller node.
           --port=6633           # Port which controller is listening on.
```

Note, that ```address``` argument defaulted to ```127.0.0.1``` and port defaulted to ```6633```.

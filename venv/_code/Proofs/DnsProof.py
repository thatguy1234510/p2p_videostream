from .. import Partner
from .. import DNS_local
import sys

if __name__ == '__main__':
    dns = DNS_local.DNS_local()
    dns.begin()

    P = Partner.Partner(verbose = True, name = "school comp")
    P.setDNS_local("localhost", 8000)
    P.set_partner(P.QueryDNS_local("home comp"))

    if not P.connectPartner(): 
        print("connectPartner failed")
        sys.exit(0)
    P.send("hello from {}".format(P.name).encode())
    print(P.recv().decode())

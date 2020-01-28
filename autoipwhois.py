from ipwhois import IPWhois
from ipwhois.utils import ipv4_is_defined
import argparse
import json
import dns.resolver #import the module

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a",
                        help="An IPv4 address to query.",
                        dest="address",
                        required=False)
    parser.add_argument("-f",
                        help="A list of IPv4 addresses, one per line.",
                        dest="filename",
                        required=False)
    parser.add_argument("-t",
                        help="Outputs results to a specified TSV file.",
                        dest="tsvoutfile",
                        required=False)

    return(parser.parse_args())

def print_results(entry):
    print ("%s\t%s\t%s\t%s" % (entry[0].strip(), entry[1].strip(), entry[2].strip(), entry[3]))

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def get_dns(address):
    res = dns.resolver.Resolver()  # create a new instance named 'myResolver'
    req = '.'.join(reversed(address.split("."))) + ".in-addr.arpa"
    try:
        answer = res.query(req, "PTR")
        output = answer[0]
    except:
        output = req
    return (output)



if __name__ == '__main__':

    args = parse_args()
    address = args.address
    filename = args.filename
    tsvoutfile = args.tsvoutfile

    if address:
        output = []
        rfc1918 = ipv4_is_defined(address.strip())

        if rfc1918[0]:
            result = [address.strip(), rfc1918[2], rfc1918[1], 'N/A']

        else:
            obj = IPWhois(address.strip())
            lookup = obj.lookup_rdap(asn_methods=['dns', 'whois', 'http'])
            reversedns = get_dns(address.strip())
            result = [lookup['query'], lookup['asn_cidr'], lookup['asn_description'], reversedns]

        print_results(result)

    elif filename:

        filehandle = open(filename, 'r')
        filelength = file_len(filename)

        if tsvoutfile:
            print ("Writing output to " + tsvoutfile + ".")
            outfilehandle = open(tsvoutfile, 'a')

        output = []
        result = []

        for address in filehandle:
            rfc1918 = ipv4_is_defined(address.strip())
            if rfc1918[0]:
                result = [address, rfc1918[2], rfc1918[1], 'N/A']
            else:
                obj = IPWhois(address.strip())
                lookup = obj.lookup_rdap(asn_methods=['dns', 'whois', 'http'])
                reversedns = get_dns(address.strip())
                result = [lookup['query'], lookup['asn_cidr'], lookup['asn_description'], reversedns]

            output = "%s\t%s\t%s\t%s\n" % (result[0], result[1], result[2], result[3])
            if tsvoutfile:
                outfilehandle.write(output)
            else:
                print(output.strip())


    else:
        print ("[-] No address(es) specified.")







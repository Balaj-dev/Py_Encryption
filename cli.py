import argparse
from encoding import *
from encryption import *

parser = argparse.ArgumentParser(
    prog='Crypto-toolkit',
    description='Encode, encrypt, decrypt text, etc.',
    epilog='Hope this helps! ;)'
)

parser.add_argument(
    'action',
    choices=['encode', 'decode', 'encrypt', 'decrypt'],
    help='What to do with the input text'
)
parser.add_argument(
    'method',
    choices=['32', '64', 'morse', 'hexa'],
    help='Which method to use'
)
parser.add_argument(
    'text',
    help='The text to process'
)

args = parser.parse_args()

if args.action == 'encode':
    if args.method == '32':
        print(base32_encoding(args.text))
    elif args.method == '64':
        print(base64_encoding(args.text))
    elif args.method == 'morse':
        print(encode_to_morse(args.text))
    elif args.method == 'hexa':
        print(encode_hex(args.text))


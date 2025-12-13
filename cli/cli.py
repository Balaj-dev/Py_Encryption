import pyfiglet , argparse
# import encoding as encode


# tool_name = pyfiglet.figlet_format("Crypto-Toolkit", font="Standard")
# print(tool_name)
# print(encode.base64_encoding(input("enter something to encode in Base32 format: ")))

parser = argparse.ArgumentParser(
            prog='cyber-Toolkit',
            description='can turn your data into any from of encryption or hashes')
parser.add_argument('-e','--encode',help='encode the data',
                     choices=["b64", "b32"])




if __name__ == '__main__':
    args = parser.parse_args()

    if args.encode:
        if args.b64:
            print("Base64 encoding")
        elif args.b32:
            print("Base32 encoding")
        else:
            parser.error("-e requires -b64 or -b32")
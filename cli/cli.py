import pyfiglet , argparse
# import encoding as encode


tool_name = pyfiglet.figlet_format("Crypto-Toolkit", font="Standard")
# print(tool_name)
# print(encode.base64_encoding(input("enter something to encode in Base32 format: ")))

def phrases():
    parser = argparse.ArgumentParser(
                    prog='cyber-Toolkit',
                    description='can turn your data into any from of encryption or hashes',
                    epilog='Help here')
    parser.add_argument('filename')           # positional argument
    parser.add_argument('-c', '--count')      # option that takes a value
    parser.add_argument('-v', '--verbose',
                    action='store_true')  # on/off flag

while True:
    phrases()
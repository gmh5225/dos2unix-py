import argparse

def dos2unix(input_file, output_file=None):
    with open(input_file, 'rb') as file:
        content = file.read()

    unix_content = content.replace(b'\r\n', b'\n')

    if output_file is None:
        output_file = input_file

    with open(output_file, 'wb') as file:
        file.write(unix_content)

    print(f"Converted {input_file} to UNIX format.")

def main():
    parser = argparse.ArgumentParser(description="Convert DOS format files to UNIX format.")
    
    parser.add_argument("input_file", help="The input file to be converted.")
    parser.add_argument("-o", "--output_file", help="The output file after conversion. If not specified, the input file will be overwritten.", default=None)
    
    args = parser.parse_args()
    
    dos2unix(args.input_file, args.output_file)

if __name__ == "__main__":
    main()

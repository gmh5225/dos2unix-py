import os
import argparse
from dos2unix import dos2unix

def convert_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            dos2unix(file_path)

def main():
    parser = argparse.ArgumentParser(description="Recursively convert DOS format files to UNIX format in a directory.")
    parser.add_argument("directory", help="The directory containing files to be converted.")
    args = parser.parse_args()
    convert_directory(args.directory)

if __name__ == "__main__":
    main()

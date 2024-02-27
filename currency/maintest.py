import argparse
import sys

def main():
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser()
        parser.add_argument("test_argument")
        args = parser.parse_args()

        if any(args.__dict__.values()):
            print("Command-line arguments provided")
    else:
        print("Running in interactive mode")

if __name__ == "__main__":
    main()
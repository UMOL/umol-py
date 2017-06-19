import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("json_str")
    args = parser.parse_args()
    print(args.json_str)

if __name__ == '__main__':
    main()

import argparse
import json
import yaml


def main():
    parser = argparse.ArgumentParser()
    # parser.add_argument(
    #     "-js",
    #     "--jsonstr",
    #     help="output verbosity",
    #     dest="json_str"
    # )
    parser.add_argument(
        "-yf",
        "--yamlfile",
        help="output verbosity",
        dest="yaml_file",
        default=None
    )


    args = parser.parse_args()
    if args.yaml_file is not None:
        with open(args.yaml_file, "r") as IN:
            data = yaml.load(IN)
        print(type(data), data)

if __name__ == '__main__':
    main()

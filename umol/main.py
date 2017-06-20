import argparse
import json
import yaml


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-js",
        "--jsonstr",
        help="JSON string",
        dest="json_str",
        default=None,
    )

    parser.add_argument(
        "-jf",
        "--jsonfile",
        help="JSON file name",
        dest="json_file",
        default=None,
    )

    parser.add_argument(
        "-yf",
        "--yamlfile",
        help="YAML file name",
        dest="yaml_file",
        default=None
    )


    args = parser.parse_args()

    if args.json_str is not None:
        data = json.loads(args.json_str)
    elif args.json_file is not None:
        data = json.load
    elif args.yaml_file is not None:
        with open(args.yaml_file, "r") as IN:
            data = yaml.load(IN)
    else:
        data = None
    
    print(type(data), data)

if __name__ == '__main__':
    main()
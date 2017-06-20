import argparse

def main():
    parser = argparse.ArgumentParser()
    # parser.add_argument("json_str", help="json string")
    # parser.add_argument("i", type=int, help="some integer")
    parser.add_argument(
        "-v",
        "--verbosity",
        action="count",
        # choices=[0, 1, 2],
        # type=int,
        help="output verbosity",
    )
    parser.add_argument(
        "square",
        type=int,
        help="display a square of some number",
    )
    args = parser.parse_args()
    answer = args.square ** 2
    if args.verbosity == 2:
        print("the square of {} = {}".format(
            args.square, answer))
    elif args.verbosity == 1:
        print("{}^2 == {}".format(args.square, answer))
    else:
        print(answer)

if __name__ == '__main__':
    main()

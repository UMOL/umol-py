import parseArgs
from umol.app import run


def main():
    print(run(*parseArgs.main()))

if __name__ == '__main__':
    main()

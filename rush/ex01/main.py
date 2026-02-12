import sys
from checkmate import checkmate


def main():
    if len(sys.argv) < 2:
        return

    for filename in sys.argv[1:]:
        try:
            with open(filename, "r") as f:
                content = f.read().strip("\n")

            result = checkmate(content)

            if result is None:
                print("Error")
            else:
                print(result)

        except Exception:
            print("Error")


if __name__ == "__main__":
    main()

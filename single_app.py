"""Single-file app combining logic and CLI (minimal)."""

def classify_number(n: int) -> str:
    """Classify an integer with tiny fizzbuzz logic."""
    if n % 15 == 0:
        return "fizzbuzz"
    if n % 3 == 0:
        return "fizz"
    if n % 5 == 0:
        return "buzz"
    return str(n)


def main() -> None:
    """Simple CLI: read ints from stdin and print classification."""
    print("Enter integers (empty line to quit):")
    try:
        while True:
            line = input().strip()
            if line == "":
                break
            try:
                n = int(line)
            except ValueError:
                print("Please enter a valid integer.")
                continue
            print(classify_number(n))
    except (EOFError, KeyboardInterrupt):
        print()


if __name__ == "__main__":
    main()

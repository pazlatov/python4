import sys


def read_archive(filename: str) -> str | None:
    print(f"Accessing file '{filename}'")

    try:
        archive = open(filename, "r", encoding="utf-8")
        try:
            content = archive.read()
        finally:
            archive.close()
    except (OSError, UnicodeError) as error:
        print(f"Error accessing file '{filename}': {error}")
        return None

    print("---")
    print(content, end="" if content.endswith("\n") else "\n")
    print("---")
    print(f"File '{filename}' closed.")
    return content


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    print("=== Cyber Archives Recovery ===")
    read_archive(sys.argv[1])


if __name__ == "__main__":
    main()
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


def transform_content(content: str) -> str:
    transformed: list[str] = []

    for line in content.splitlines(keepends=True):
        if line.endswith("\n"):
            transformed.append(line[:-1] + "#\n")
        else:
            transformed.append(line + "#")

    return "".join(transformed)


def save_archive(filename: str, content: str) -> bool:
    print(f"Saving data to '{filename}'")

    try:
        archive = open(filename, "w", encoding="utf-8")
        try:
            archive.write(content)
        finally:
            archive.close()
    except (OSError, UnicodeError) as error:
        print(f"Error saving file '{filename}': {error}")
        return False

    print(f"Data saved in file '{filename}'.")
    return True


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")
    content = read_archive(sys.argv[1])

    if content is None:
        return

    transformed = transform_content(content)
    print("Transform data:")
    print("---")
    print(transformed, end="" if transformed.endswith("\n") else "\n")
    print("---")

    try:
        destination = input("Enter new file name (or empty): ")
    except (EOFError, KeyboardInterrupt):
        print("\nNot saving data.")
        return

    if not destination:
        print("Not saving data.")
    elif not save_archive(destination, transformed):
        print("Data not saved.")


if __name__ == "__main__":
    main()
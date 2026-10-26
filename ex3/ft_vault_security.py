def secure_archive(
    filename: str,
    action: str = "read",
    content: str = "",
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, "r", encoding="utf-8") as archive:
                data = archive.read()
            return True, data

        if action == "write":
            with open(filename, "w", encoding="utf-8") as archive:
                archive.write(content)
            return True, "Content successfully written to file"

        return False, "Invalid action: use 'read' or 'write'"

    except (OSError, UnicodeError, ValueError) as error:
        return False, str(error)


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("Using 'secure_archive' to read from a protected file:")
    print(secure_archive("/etc/master.passwd"))

    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt")
    print(result)

    success, content = result

    if success:
        print("Using 'secure_archive' to write content to a new file:")
        print(secure_archive("new_fragment.txt", "write", content))
    else:
        print("Copy skipped because the source could not be read.")


if __name__ == "__main__":
    main()
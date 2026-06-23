from dokufmt.cli.parser import parse_cli


def main() -> None:
    options = parse_cli(standalone_mode=False)

    print(options.path)


if __name__ == "__main__":
    main()

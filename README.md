# DokuFmt

DokuFmt is a command-line formatter for DokuWiki files.

The goal of the project is to automatically normalize DokuWiki documents by applying a consistent set of formatting rules, such as blank lines, headers, lists, whitespace and other syntax-specific conventions.

## Project status

This is a personal learning project created while studying Python.

Although the tool is intended to become fully usable, the primary objective is to learn the Python language, its standard library, idioms and best practices by building a real-world application.

For that reason, the project intentionally favors simplicity and incremental development over feature completeness.

## Install

```bash
git clone https://github.com/edu-escritor/dokuFmt.git /your/development/root/dokuFmt
```

## Planned features

* Normalize blank lines
* Normalize headers
* Normalize list indentation
* Remove trailing whitespace
* Normalize leading whitespace
* Optional table alignment
* Configurable rules through `.dokufmt.toml`
* Directory traversal
* Check mode (without modifying files)
* Diff mode

## License

MIT

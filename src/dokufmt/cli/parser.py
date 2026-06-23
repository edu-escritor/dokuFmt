from pathlib import Path

import click

from dokufmt.cli.cli_options import CliOptions


def validate_txt_file(
    context: click.Context,
    parameter: click.Parameter,
    value: Path,
) -> Path:
    if ".txt" != value.suffix.lower():
        raise click.BadParameter("A DokuWiki file must have a .txt extension!")

    return value


@click.command()
@click.argument(
    "path",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        path_type=Path,
    ),
    callback=validate_txt_file,
)
def parse_cli(path: Path) -> CliOptions:
    return CliOptions(path=path)

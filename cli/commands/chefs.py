"""
Module that provides an example for a CLI to create lasagna
"""
import functools
import click

@click.option(
    "--gordon-ramsay",
    default="Gordon Ramsay",
    help="Chef specializing in public image"
)
@click.option(
    "--napoli-matfia",
    default="Napoli Matfia",
    help="Chef from Korea specializing in Italian Cuisine"
)
@click.option(
    "--martha-stewart",
    default="Martha Stewart",
    help="Chef specializing in cross-cultural cuisine",
)
@click.option(
    "--ratatoullie",
    default="Remy from Ratatoullie",
    help="Chef specializing in guidance and sense of smell",
)
@click.group(name="chef")
def chef_cmd(ctx: click.Context) -> None:
    """
    Click CLI group that will have subcommands as the sous chefs
    """
    pass
@click.option(
    "--gordon-ramsay",
    default="Gordon Ramsay",
    help="Chef specializing in public image"
)
@click.option(
    "--napoli-matfia",
    default="Napoli Matfia",
    help="Chef from Korea specializing in Italian Cuisine"
)
@click.option(
    "--martha-stewart",
    default="Martha Stewart",
    help="Chef specializing in cross-cultural cuisine",
)
@click.option(
    "--ratatoullie",
    default="Remy from Ratatoullie",
    help="Chef specializing in guidance and sense of smell",
)

@chef_cmd.command("head-chef")
def head_chef_cmd(ctx: click.Context, ratatoullie: str) -> None:
    """
    Command that outlines the head chef duties.
    """
    click.echo(f"The head chef is {ratatoullie}")

@click.option(
    "--napoli-matfia",
    default="Napoli Matfia",
    help="Chef from Korea specializing in Italian Cuisine"
)
@chef_cmd.command("sous-chef")
def sous_chef_cmd(ctx: click.Context, napoli_matfia: str) -> None:
    """
    Command that outlines the sous chef duties.
    """
    click.echo(f"The sous chef is {napoli_matfia}")
@click.option(
    "--martha-stewart",
    default="Martha Stewart",
    help="Chef specializing in cross-cultural cuisine",
)
@chef_cmd.command("pastry-chef")
def pastry_chef_cmd(ctx: click.Context, martha_stewart: str) -> None:
    """
    Command that outlines the pastry chef duties.
    """
    click.echo(f"The pastry chef is {martha_stewart}")

if __name__ == "__main__":
    chef_cmd()
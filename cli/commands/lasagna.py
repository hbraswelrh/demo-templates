"""

Module for creating lasagna

"""

import click

@click.option(
    "--cheese-type",
    prompt= "Enter your preferred cheese type",
    help="The cheese type is Fontina"
)
@click.option(
    "--cheese-temp",
    prompt= "Enter your preferred cheese temp",
    help="The cheese temp is"
)
@click.option(
    "--sauce-type",
    prompt= "Enter your preferred sauce type",
    help="The sauce type is Tomato"
)
@click.option(
    "--number-of-layers",
    prompt= "Enter your preferred number of lasagna layers",
    help="The number of layers for lasagna"
)
@click.group("lasagna")
def lasagna_cmd(
    ctx: click.Context,
    number_of_layers: str,
    sauce_type: str,
    cheese_temp: str,
    cheese_type: str,
) -> None:
    """
    Module for creating lasagna
    """
    pass
@click.option(
    "--baking-sheet",
    prompt="The type of baking sheet is:",
    help="The baking sheet to use for assembling lasagna",
)
@click.option(
    "--pre-heat-oven",
    prompt="The temperature to preheat the oven to is: ",
    help="Pre-heat oven to desired temperature"
)
@click.option(
    "--number-of-layers",
    prompt= "Enter your preferred number of lasagna layers",
    help="The number of layers for lasagna"
)
@lasagna_cmd.command("setup")
def setup_cmd(
    ctx: click.Context,
    baking_sheet: str,
    pre_heat_oven: str,
    number_of_layers: str,
) -> None:
    """
    Command to assemble lasagna layers
    """
    click.echo(f"The {baking_sheet} has been assembled.")
    click.echo(f"The oven temperature is {pre_heat_oven} degrees.")
    click.echo(f"The number of layers for the lasagna is: {number_of_layers}")

@click.option(
    "--oven-temp",
    prompt= "Enter your oven temperature",
    help="The oven temperature for cooking lasagna",
)
@click.option(
    "--number-of-layers",
    prompt= "Enter your preferred number of lasagna layers",
    help="The number of layers for lasagna",
)
@lasagna_cmd.command("oven")
def oven_cmd(
    ctx: click.Context,
    cheese_type: str,
    oven_temp: str,
    number_of_layers: str
) -> None:
    """
    Command to put lasagna in the oven
    """
    click.echo(f"The lasagna is in the oven with {cheese_type}")
    click.echo(f"The lasagna is in the oven with {number_of_layers}")
    click.echo(f"The lasagna is in the oven with {oven_temp}")

if __name__ == "__main__":
    lasagna_cmd()
"""
Chefs common options
"""
import functools
from typing import Any, Callable, Dict, Optional, Sequence, TypeVar
import click

F = TypeVar("F", bound=Callable[..., Any])

def chef_options(f: F) -> Any:
    """
    Chef options decorator
    """
    @click.pass_context
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
    @functools.wraps(f)
    def wrapper_chef_options(*args: Sequence[Any], **kwargs: Dict[Any, Any]) -> Any:
        return f(*args, **kwargs)
    
    return wrapper_chef_options
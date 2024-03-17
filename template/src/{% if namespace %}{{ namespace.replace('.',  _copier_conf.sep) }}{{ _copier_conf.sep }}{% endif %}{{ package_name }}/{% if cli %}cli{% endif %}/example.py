import typer
import logging

from rich.logging import RichHandler


def setup_logging():
    FORMAT = "%(message)s"
    logging.basicConfig(
        level="DEBUG", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
    )


app = typer.Typer(pretty_exceptions_enable=False)
logger = logging.getLogger(__name__)


@app.command(no_args_is_help=True)
def main(
    a: int = typer.Argument(1, help="The first number"),
    b: int = typer.Option(2, help="The second number"),
):
    setup_logging()
    logger.info("Hello, World!")

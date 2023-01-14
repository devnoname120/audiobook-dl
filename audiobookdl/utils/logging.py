from rich.console import Console
import pkg_resources

debug_mode = False
quiet_mode = False
console = Console(stderr=True)

def debug(msg: str):
    """Print debug msg"""
    if debug_mode:
        log(f"[yellow bold]DEBUG[/] {msg}")

def log(msg: str):
    """Display msg in log"""
    if not quiet_mode:
        console.print(msg)


def read_asset_file(path: str) -> str:
    return pkg_resources.resource_string("audiobookdl", path).decode("utf8")


def print_error(name: str, **kwargs):
    """Print predefined error message"""
    msg = read_asset_file(f"assets/errors/{name}.txt").format(**kwargs)
    console.print(msg)


def print_asset_file(path: str):
    """Read asset file and print it"""
    console.print(read_asset_file(path))


def simple_help():
    """Print basic help information"""
    print_asset_file("assets/simple_help.txt")

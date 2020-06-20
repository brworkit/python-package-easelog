from sys import stdout
from easelog.easelog import *


def test_one():
    setup(
        name="MY APP",
        output_fmt=["asctime", "levelname", "message"],
        sep = " | ",
        datefmt="%d/%m/%Y",
        level=logging.CRITICAL)

    fatal("Fatal message.")
    error("Error message.")
    warning("Warning message.")
    info("Info message.")
    debug("Debug message.")
    c("Critical message.")
    f("Fatal message.")
    e("Error message.")
    w("Warning message.")
    i("Info message.")
    d("Debug message.")

def test_two():
    setup(
        name="MY APP 2",
        output_fmt=["asctime", "levelname", "message", "custom"],
        sep = " > ",
        datefmt="%Y-%m-%d",
        level=logging.INFO)

    _json = {"custom": "CUSTOM VALUE"}

    critical("Critical message.", extra=_json)
    fatal("Fatal message.", extra=_json)
    error("Error message.", extra=_json)
    warning("Warning message.", extra=_json)
    info("Info message.", extra=_json)
    debug("Debug message.", extra=_json)
    c("Critical message.", extra=_json)
    f("Fatal message.", extra=_json)
    e("Error message.", extra=_json)
    w("Warning message.", extra=_json)
    i("Info message.", extra=_json)
    d("Debug message.", extra=_json)



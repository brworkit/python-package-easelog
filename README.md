# easelog

## Description

A python package for easy log formatting and productivity boost.

# Install
    pip install easelog

# Currently Available functions

```

critical(msg, *args, extras)
c(msg, *args, extras) # short name for critical

fatal(msg, *args, extras)
f(msg, *args, extras) # short name for fatal

error(msg, *args, extras)
e(msg, *args, extras) # short name for error

warning(msg, *args, extras)
w(msg, *args, extras) # short name for warning

info(msg, *args, extras)
i(msg, *args, extras) # short name for info

debug(msg, *args, extras)
d(msg, *args, extras) # short name for debug

```

# Usage example

```python

from easelog.easelog import *

setup(
      name="MY APP",
      output_fmt=["asctime", "levelname", "message"],
      sep = " | ",
      datefmt="%d/%m/%Y",
      level=logging.CRITICAL)

critical("Critical message.")
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

2020-06-20 00:36:51 | WARNING | Warning message.
2020-06-20 00:36:51 | INFO | Info message.
2020-06-20 00:36:51 | CRITICAL | Critical message.

2020-06-20 00:36:51 | CRITICAL | Fatal message.
2020-06-20 00:36:51 | ERROR | Error message.
2020-06-20 00:36:51 | WARNING | Warning message.
2020-06-20 00:36:51 | INFO | Info message.

```

## PyPi

[easelog](https://pypi.org/project/easelog)

## Author

[**2020 brworkit**](https://github.com/brworkit).

## License
[MIT License.](https://opensource.org/licenses/MIT)
import logging

_FMT_KS = {
    "process": "(%s)d",
    "processName": "(%s)s",
    "thread": "(%s)d",
    "threadName": "(%s)s",
    "asctime": "(%s)s",
    "levelname": "(%s)s",
    "name": "(%s)s",
    "pathname": "(%s)s",
    "module": "(%s)s",
    "lineno": "(%s)d",
    "message": "(%s)s",
}

_NAME = __name__
_FORMAT = '%(levelname)s - %(asctime)s - %(name)s - %(message)s'
_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
_LEVEL = logging.INFO

def build_fmt(fmt_list, sep=" - "):
    res = ""
    for key in fmt_list:
        if res != "":
            res += sep
        res += "%" + _FMT_KS[key] % (key) if key in _FMT_KS else "%" + "(%s)s" % (key)
    return res

def _extract_fmt(fmt, sep):
    if isinstance(fmt, str):
        return fmt
    return build_fmt(fmt, sep)

def setup(name=_NAME,
          output_fmt=_FORMAT,
          datefmt=_DATETIME_FORMAT,
          sep = " - ",
          level=_LEVEL,
          handler=None):

    global _log

    _log = logging.getLogger(name)
    _log.setLevel(_LEVEL)

    if not handler:
        _sh = logging.StreamHandler()
    else :
        _sh = handler

    _sh.setLevel(_LEVEL)
    _formatter = logging.Formatter(_extract_fmt(output_fmt, sep), datefmt=_DATETIME_FORMAT)
    _sh.setFormatter(_formatter)
    _log.addHandler(_sh)

def set_name(name):
    _log.name = name

def set_format(fmt, datefmt='%Y-%m-%d %H:%M:%S'):
    _formatter = logging.Formatter(fmt, datefmt=datefmt)
    _sh.setFormatter(_formatter)

def set_level(level):
    _log.setLevel(level)
    _log.isEnabledFor(_LEVEL)
    _sh.setLevel(level)

def info(msg, *args, extra=None):
    _log.info(msg, *args, extra=extra)

def debug(msg, *args, extra=None):
    _log.debug(msg, *args, extra=extra)

def error(msg, *args, extra=None):
    _log.error(msg, *args, extra=extra)

def fatal(msg, *args, extra=None):
    _log.fatal(msg, *args, extra=extra)

def critical(msg, *args, extra=None):
    _log.critical(msg, *args, extra=extra)

def warning(msg, *args, extra=None):
    _log.warning(msg, *args, extra=extra)

def i(msg, *args, extra=None):
    info(msg, *args, extra=extra)

def d(msg, *args, extra=None):
    debug(msg, *args, extra=extra)

def e(msg, *args, extra=None):
    error(msg, *args, extra=extra)

def f(msg, *args, extra=None):
    fatal(msg, *args, extra=extra)

def c(msg, *args, extra=None):
    critical(msg, *args, extra=extra)

def w(msg, *args, extra=None):
    warning(msg, *args, extra=extra)

_log = None
_sh = None
_formatter = None

setup(
    name=_NAME,
    output_fmt=_FORMAT,
    datefmt=_DATETIME_FORMAT,
    level=_LEVEL
)
from zish.core import ZishException, dump, dumps, load, loads


try:
    from importlib.metadata import version
except ImportError:
    from importlib_metadata import version

__version__ = version("zish_antlr")

__all__ = [load, loads, dump, dumps, ZishException]

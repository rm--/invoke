import logging
import os
from contextlib import contextmanager


LOG_FORMAT = "%(name)s.%(module)s.%(funcName)s: %(message)s"

def enable_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format=LOG_FORMAT,
    )

# Allow from-the-start debugging (vs toggled during load of tasks module) via
# shell env var.
if os.environ.get('INVOKE_DEBUG'):
    enable_logging()

# Add top level logger functions to global namespace. Meh.
log = logging.getLogger('invoke')
for x in ('debug',):
    globals()[x] = getattr(log, x)


def sort_names(names):
    """
    Sort task ``names`` by nesting depth & then as regular strings.
    """
    return sorted(names, key=lambda x: (x.count('.'), x))


# TODO: Make part of public API sometime
@contextmanager
def cd(where):
    cwd = os.getcwd()
    os.chdir(where)
    try:
        yield
    finally:
        os.chdir(cwd)

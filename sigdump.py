import gc
import os
import signal
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional
    from typing import TextIO

sigdump_signal: 'Optional[str, None]' = os.getenv("SIGDUMP_SIGNAL", None)
sigdump_path: 'Optional[str, None]' = os.getenv("SIGDUMP_PATH", None)


if sigdump_path is None:
    sigdump_path = f"/tmp/sigdump-{os.getpid()}.log"


def print_gc_stats(f: 'TextIO'):
    f.write("GC stat:\n")
    for stat in gc.get_stats():
        f.write(f"  {stat}\n")


def handler(signum, frame):
    with open(sigdump_path, 'a') as f:
        print_gc_stats(f)
        f.flush()


def enable(verbose: bool = True) -> None:
    signal_no: int = signal.SIGCONT
    if sigdump_signal is not None:
        signal_no = getattr(signal, sigdump_signal.upper())
    signal.signal(signal_no, handler)

    if verbose:
        print(f"SIGDUMP is enabled. The result is exported to "
              f"{sigdump_path if sigdump_path != '-' else 'stdout'}.")

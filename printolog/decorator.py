from functools import wraps
import logging
import traceback
import sys


class LogWriter:
    def __init__(
        self,
        fn,
        level=logging.INFO,
        format="[%(asctime)s] [%(levelname)8s] %(fname)s() - %(message)s",
        logfilehandler=None
    ):

        self.n = fn
        self.level = level
        self.l = logging.getLogger(name=self.n)

        logging.basicConfig(
            format=format,
        )

        if logfilehandler:
            formatter = logging.Formatter(format)
            logfilehandler.setFormatter(formatter)
            self.l.addHandler(logfilehandler)

        self.l.setLevel(self.level)

    def __full_exc_info(self):
        """Like sys.exc_info, but includes the full traceback."""
        """Credit to: https://stackoverflow.com/a/58105833/13018929"""

        class TB:
            """Custom Traceback class"""

            def __init__(
                self,
                tb_frame,
                tb_lineno,
                tb_next
            ):
                self.tb_frame = tb_frame
                self.tb_lineno = tb_lineno
                self.tb_next = tb_next

        t, v, tb = sys.exc_info()
        f = sys._getframe(3)
        while f is not None:
            tb = TB(f, f.f_lineno, tb)
            f = f.f_back
        return t, v, tb

    def write(self, text):
        text = text.rstrip()
        if len(text) == 0:
            return
        self.l.log(
            self.level,
            text,
            extra=dict(
                fname=self.n
            )
        )

    def exception_handler(self, e):
        self.l.exception(
            f"Error in function '{self.n}'",
            exc_info=self.__full_exc_info(),
            extra=dict(
                fname=self.n
            )
        )
        raise e


def printolog(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)5s] %(fname)10s() - %(message)s",
    logfilehandler=None
):
    '''Calls to print will be logged instead.'''

    def logwriter(f):

        log_writer = LogWriter(
            fn=f.__name__,
            level=level,
            format=format,
            logfilehandler=logfilehandler
        )

        @wraps(f)
        def printwrapper(*arg, **kwargs):
            old_stdout = sys.stdout
            sys.stdout = log_writer

            try:
                return f(*arg, **kwargs)
            except Exception as e:
                log_writer.exception_handler(e)
            finally:
                sys.stdout = old_stdout

        return printwrapper
    return logwriter

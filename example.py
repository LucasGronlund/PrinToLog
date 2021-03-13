from printolog import printolog
import logging
from logging.handlers import TimedRotatingFileHandler
import os

log_dir = "logs"
os.makedirs(os.path.abspath(log_dir), exist_ok=True)


# Use default settings, Only print to console.
@printolog()
def addition(n1, n2):
    print(f"Adding {n1} and {n2}")
    return n1 + n2


addition(1, 2)
'''Output:
[2021-03-13 14:57:02,533] [ INFO]   addition() - Adding 1 and 2
'''


# Use custom filehandler to save logs to file,
# in addition to console print.
@printolog(
    logfilehandler=logging.handlers.TimedRotatingFileHandler(
        os.path.join(log_dir, "multiply.log"),
        when="d"
    )
)
def multiply(n1, n2):
    print(f"Multiplying {n1} with {n2}")
    return n1*n2


multiply(2, 3)
'''Output in console and logfile:
[2021-03-13 14:57:02,534] [ INFO]   multiply() - Multiplying 2 with 3
'''


# Filehandler will log wrapped function stacktrace (ignoring wrapper functions),
# console will show full stracktrace.
@printolog(
    logfilehandler=logging.handlers.TimedRotatingFileHandler(
        os.path.join(log_dir, "divide.log"),
        when="d"
    )
)
def divide(n1, n2):
    print(f"Divide {n1} by {n2}")
    return n1/n2


divide(1, 0)
'''Output in console:
[2021-03-13 14:59:26,021] [ INFO]     divide() - Divide 1 by 0
[2021-03-13 14:59:26,021] [ERROR]     divide() - Error in function 'divide'
Traceback (most recent call last):
  File "<path_to_project>\example.py", line 50, in <module>
    divide(1, 0)
  File "<path_to_project>\printolog\decorator.py", line 103, in printwrapper
    return f(*arg, **kwargs)
  File "<path_to_project>\example.py", line 47, in divide
    return n1/n2
ZeroDivisionError: division by zero
Traceback (most recent call last):
  File "<path_to_project>\example.py", line 50, in <module>
    divide(1, 0)
  File "<path_to_project>\printolog\decorator.py", line 105, in printwrapper
    log_writer.exception_handler(e)
  File "<path_to_project>\printolog\decorator.py", line 78, in exception_handler
    raise e
  File "<path_to_project>\printolog\decorator.py", line 103, in printwrapper
    return f(*arg, **kwargs)
  File "<path_to_project>\example.py", line 47, in divide
    return n1/n2
ZeroDivisionError: division by zero
'''


'''Output in logfile:
[2021-03-13 15:00:52,191] [ INFO]     divide() - Divide 1 by 0
[2021-03-13 15:00:52,191] [ERROR]     divide() - Error in function 'divide'
Traceback (most recent call last):
  File "<path_to_project>\example.py", line 50, in <module>
    divide(1, 0)
  File "<path_to_project>\printolog\decorator.py", line 103, in printwrapper
    return f(*arg, **kwargs)
  File "<path_to_project>\example.py", line 47, in divide
    return n1/n2
ZeroDivisionError: division by zero
'''

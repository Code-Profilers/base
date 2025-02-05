# Introduction
This is a plugin to register all profilers in it and it will run all registered profilers.

## Settings
These are supported settings
* debug
* environment
* release

These are just an environments that will be shown when profiling code.

## How to use
```python
from code_profilers.main_profiler import MainProfiler

from code_profilers.profilers.postgresql.profiler import PostgreSQLProfiler
from code_profilers.profilers.mysql.profiler import MySQLProfiler

main_profiler = MainProfiler()
main_profiler.register_profiler(PostgreSQLProfiler())
main_profiler.register_profiler(MySQLProfiler())

main_profiler.start()

# Your Code

main_profiler.stop()
main_profiler.report()
```

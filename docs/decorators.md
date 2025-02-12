# Introduction
Decorators is utils functions for helping running profilers for specific functions only

## Available Decorators
* `profile_code`:
    * This a decorator to profile a function
    * Args:
        * main_profiler: Is the `MainProfiler` you need to run or just a simple profiler

## How to use

```python
from code_profilers.main_profiler import MainProfiler
from code_profilers.decorators import profile_code

@profile_code(main_profiler=MainProfiler())
def test_function(param1, param2):
    print(param1, param2)


test_function("Param1", "Param2")
```

Or you can use specific profiler
```python
from code_profilers.profilers.postgresql.profiler import PostgreSQLProfiler
from code_profilers.decorators import profile_code

postgresql_profile = PostgreSQLProfiler()
postgresql_profile.patch()

@profile_code(main_profiler=postgresql_profile)
def test_function(param1, param2):
    print(param1, param2)


test_function("Param1", "Param2")
```
Now you can go.

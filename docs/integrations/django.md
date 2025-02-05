# Introduction
This is a plugin for integrating django with profilers.

## How to use
```python
from code_profilers.profilers.postgresql.profiler import PostgreSQLProfiler
from code_profilers.main_profiler import MainProfiler

####
# Main Profiler Variable Name Must Be Write As Bellow
# So Django Will Look For This Name
####
MAIN_PROFILER = MainProfiler()
MAIN_PROFILER.register_profiler(PostgreSQLProfiler())

MIDDLEWARES = [
    "code_profilers.integrations.django.middlewares.DjangoMiddlewareIntegration",
    ...
]
```
Now you can go.

## Notes
Main Profiler Should be Write as `MAIN_PROFILER` as above example, as Django will consider it as settings and use it in profiling

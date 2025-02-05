# Introduction
This Is a plugin for helping integrating profilers with flask.
It will run the profiler before the requets and will show the result when the request ends.

## To to use
```python
from flask import Flask

from code_profilers.main_profiler import MainProfiler
from code_profilers.integrations.flask import FlaskIntegration

app = Flask(__name__)

main_profiler = MainProfiler()
FlaskIntegration(app, main_profiler)

# Your code
```

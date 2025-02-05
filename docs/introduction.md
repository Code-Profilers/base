# Introduction
This is a package for profiling your code, and use it to better understand what is happening in your code and debug better.
This is availale to use in any python code (no framework specific).


# Profilers
There is `Main Profiler` Which will register all profilers and responsible for handling issues and reporting info.

### Currently Supported Profilers
* PostgreSQLProfiler
* MySQLProfiler

# Integrations
For the ease of development, we added some integrations which will take the `Main Profiler` and handle the integration with other frameworks.
Also you could use profilers without integrations, but you will write more code.


### Currently Supported Integrations
* Flask
* Django

# Examples
This is an example for using MySQL Profiler With Flask
```python
from flask import Flask

from code_profilers.main_profiler import MainProfiler
from code_profilers.profilers.mysql.profiler import MySQLProfiler
from code_profilers.integrations.flask import FlaskIntegration

app = Flask(__name__)

profiler = MainProfiler()
profiler.register_profiler(MySQLProfiler())
FlaskIntegration(app, profiler)
```
Then you are ready to go and test your code.

You can also use it with specific lines of code not just flask

```python
from code_profilers.profilers.postgresql.profiler import PostgreSQLProfiler

postgresql_profiler = PostgreSQLProfiler()
postgresql_profiler.start()

###
# Write Your Code Here
##

postgresql_profiler.stop()
postgresql_profiler.report()
```

You can see the docs in `docs` folder.


# Links
* [Introduction](introduction.md)
* [Main Profiler](main_profiler.md)
* Profilers:
    * [PostgreSQL Profiler](profilers/postgresql.md)
    * [MySQL Profiler](profilers/mysql.md)
* Integrations:
    * [Flask Integration](integrations/flask.md)
    * [Django Integration](integrations/django.md)

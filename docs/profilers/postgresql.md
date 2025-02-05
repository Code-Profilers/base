# Introduction
This is PostgreSQL Database Profiler. It Capture te SQL Queries Beforre executing it in database and show it.


## Settings
These are the supported settings to use in PostgreSQL Profiler
* profile_queries_params
* profile_queries_time
* combine_duplicated_queries
* report_broken_queries

### profile_queries_params
This setting will show the query parameters passed to the execute function when executing query.

Values: [True, False]

Default: True

### profile_queries_params
This setting will Keep track of the time that the database took in executing the query.

Values: [True, False]

Default: True

### combine_duplicated_queries
This setting will combine duplicated queries in one line and will show the `Number Of Duplication: 2`. So to save extra spaces and better debug the values and know which queries are duplicated.

Values: [True, False]

Default: False

### report_broken_queries
This setting will report if the query raised an exception by the database or not.

Values: [True, False]

Default: True


## Formating
You can install (Not required) `sql-formatter` and `pygments` to formate your sql for better readability


## How to use
```python
from code_profilers.profilers.postgresql.profiler import PostgreSQLProfiler

postgresql_profiler = PostgreSQLProfiler()
# You can also add your settings in the init
postgresql_profiler = PostgreSQLProfiler(
    combine_duplicated_queries=True
)

postgresql_profiler.start()

###
# Write Your Code Here
##

postgresql_profiler.stop()
postgresql_profiler.report()
```

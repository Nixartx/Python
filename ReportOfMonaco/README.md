# Report Of Monaco
Show reports of Monaco from files.
link to github project [git.foxminded.com.ua](https://git.foxminded.com.ua/foxstudent100631/foxpy)

## Import
```python
from ReportOfMonaco import CLReportMonaco, ReportMonaco
```

##CountUnique class
ReportMonaco.print_report() the class takes a params and returns report

- folder (string) - path to folder with files
- driver_name (string) - name of driver
- reverse (Bool) - sort the report in asc or desc order
```python
from ReportOfMonaco import ReportMonaco
ReportMonaco.print_report(
        folder='../tests/reports',
        driver_name="Daniel Ricciardo")
```
##CLReportMonaco class
Command line class.</br>
Takes a string or patch to file and print the report from files</br>
- --files (string) - path to folder with files
- driver (string) - name of driver
- --asc/--desc  - sort the report in asc or desc order
```python
from ReportOfMonaco import CLReportMonaco
CLReportMonaco().run(['--files', 'path_to_file'])
CLReportMonaco().run(['--files', 'path_to_file', 'driver', 'Daniel Ricciardo'])
CLReportMonaco().run(['--files', 'path_to_file', '--desc'])
```
- Takes a command line parameters (string or patch to file) and print the number of unique characters in string</br>
```python
from ReportOfMonaco import CLReportMonaco
CLReportMonaco().run()
```
Command line:
> script.py --files path_to_file</br>
or</br>
> script.py --files "path_to_file" driver "Daniel Ricciardo"</br>

# Findunique
Counting unique chars in string.
link to github project [git.foxminded.com.ua](https://git.foxminded.com.ua/foxstudent100631/foxpy)

## Import
```python
from findunique import CountUnique, CLCountUnique
```

##CountUnique class
CountUnique.count() the class takes a string and returns the number of unique characters (int)
```python
from findunique import CountUnique
count=CountUnique.count('Some string here')
```
##CLCountUnique
Command line class.
- Takes a string or patch to file and print the number of unique characters in string</br>
```python
from findunique import CLCountUnique
CLCountUnique().run(['--file', 'text.txt'])
CLCountUnique().run(['--string', 'some string here'])
```
- Takes a command line parameters (string or patch to file) and print the number of unique characters in string</br>
```python
from findunique import CLCountUnique
CLCountUnique().run()
```
Command line:
> script.py --file text.txt</br>
or</br>
> script.py --string "some string here"</br>
- If both parameters is set, --files has priority
# Quake Log Parser
A simple parser for server generated Quake matchs log written in Python

## Dependencies
- [Coverage](https://coverage.readthedocs.io/en/coverage-5.5/)

## Running the Project
First, run the report generator 

```
python3 quakeparser.py games.log
```
Once finished, the program will automatically prompt a localserver at [http://0.0.0.0:8000](http://0.0.0.0:8000)

Open this page to see the report results.

## Testing
You can run unit tests by typing:
```
coverage run tests.py
```
And then run the below command to get test coverage report
```
coverage report
```
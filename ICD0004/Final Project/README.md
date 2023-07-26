**Programming language** <br>
Python 3.8 <br>
With modules: requests, re, json, os, datetime, os for running application <br>
And with additional modules for testing: pytest, sys, os, datetime <br>

**Author** <br>
Vitali Zamorski

**Installation, compilation and building in the command line** <br>
1) Install Python 3.8+ <br>
`https://www.python.org/downloads/release/python-380/ ` <br>
2) Download or import application folder and unzip it to preferred folder <br>
Download zip: <br>
` https://gitlab.cs.ttu.ee/vizamo/icd0004-vizamo-projekt/-/archive/main/icd0004-vizamo-projekt-main.zip ` <br>
3) Install the required packages with: <br>
```python3 -m pip install -r requirements.txt ```<br>

**How to run tests in the command line** <br>
1) Move into application tests dir in terminal: <br>
``` cd /path/to/app/tests/``` <br>
2) Start the testing with: <br>
```pytest --junitxml=report.xml ``` <br>
When testing will be completed, also will be generated report.xml file with testing results <br>

**How to specify inputs without changing code itself** <br>
You can specify the cities in provided to process file <br>
You can specify file with cities when run the app <br>
You can specify does you need output of report into stdout or not when run the app <br>

**How to run the app in the command line** <br>
1) Move into application dir in terminal: <br>
``` cd /path/to/app/app/``` <br>

2) Create new or use default text file with names of cities <br>
Default file is `cities_for_owm.txt` <br>
Each city must be entered on a new line. File extension must be .txt <br>

3) Run the command <br>
```python3 weather_app.py``` <br>

Report for each city will be printed into command line <br>
And also saved in: <br>
`/path/to/app/output/weather_report_for_your-city.json `<br>

A logging messages will be printed into command line <br>
And also saved in: <br>
`/path/to/app/output/log.txt `<br>

CI/CD Pipeline <br>
Tests logs can be review in CI/CD - Pipeline - click on pipeline to review - Tests <br>
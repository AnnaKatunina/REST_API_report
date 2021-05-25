## REST API report of Monaco Racing
A web application using Flask REST API framework that reads data from 3 files start.log, end.log and abbreviation
that contain start and end data of the best lap for each racer of Formula 1 - Monaco 2018 Racing,
saves data in database and has a few routes.
____
### Installing
1\. Clone the repository
```
    git clone https://github.com/AnnaKatunina/REST_API_report.git
```
2\. Create and activate virtualenv
```
    python -m venv venv
    source venv/bin/activate (for Linux/macOS) or venv\Scripts\activate (for Windows)
```
3\. Install packages from requirements.txt
```
    pip install -r requirements.txt
```
____
### Usage

The application has format: json / xml (default format is json) and order: asc / desc (default order is asc) in get parameters.

The application accepts the following GET requests:


- /api/v1/report/?format=json or /api/v1/report/?format=xml

shows common statistic of drivers and their results


- /api/v1/drivers?format=xml&order=desc

shows list of drivers names in descending order in xml format


- /api/v1/drivers/<driver_id>?format=json 

shows information about a driver in json format

____

Also added swagger, you can see it in /apidocs
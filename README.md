## REST API report of Monaco 2018 Racing using database
A web application using Flask REST API framework that reads data from 3 files start.log, end.log and abbreviation
that contain start and end data of the best lap for each racer of Formula 1 - Monaco 2018 Racing and
saves data in database.

The application has format: json / xml (default format is json) and order: asc / desc (default order is asc) in parameters.

The application accepts the following GET requests:


- /api/v1/report/?format=json or /api/v1/report/?format=xml

shows common statistic of drivers and their results


- /api/v1/drivers?format=xml&order=desc

shows list of drivers names in descending order in xml format


- /api/v1/drivers/<driver_id>?format=json 

shows information about a driver in json format



Also added swagger, you can see it in /apidocs

<h1 align="center">OntMetaDatabase</h1>



<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
</p>

<br>

## :dart: About ##

 A Ontology Metadata Database based on PostgreSQl and a REST-API that connects to it written in Python

## :sparkles: Features ##

:heavy_check_mark: Initialize Database
:heavy_check_mark: Three Endpoints
:heavy_check_mark: Add and remove ontologies through the API
:heavy_check_mark: Filter through Database through the API

## :rocket: Technologies ##

The following tools were used in this project:

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/2.3.x/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [webargs](https://webargs.readthedocs.io/en/latest/)

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to install the requirements in the requirements.txt, and have a postgreSQl database running and reachable.

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/SupaaSchnitzel/OntMetaDatabase

# Access
$ cd OntMetaDatabase/app

# Install dependencies
$ pip install -r requirements.txt

# Edit the Information for the Postgres Database
$ nano app.py

# Initialize the database
$ python app.py

# Run the API
$ flask run

# The script will open a reachable api at localhost:5000
```
A prototype json is added inside the repo to test the API functionality.

### Startup with Docker ###
```bash
# Clone this project
$ git clone https://github.com/SupaaSchnitzel/OntMetaDatabase

# Access
$ cd OntMetaDatabase

# Build containers
$ docker-compose build

# Start containers
$ docker-compose up

# The script will open a reachable api at the Endpoint that is shown in the terminal
```

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


&#xa0;

<a href="#top">Back to top</a>

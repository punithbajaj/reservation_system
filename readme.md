# Restaurant Reservation System

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/gocardless/sample-django-app.git
$ cd reservation_system
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ py -m venv venv
$ ./venv/Scripts/activate
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.

Once `pip` has finished downloading the dependencies:
```sh
(venv)$ cd reservation_system
(venv)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

You can find main logic behind the reservation system in
`./reservation_system/restaurant/views.py`

## About

This reservation system follows following specifications :
- Tables can hold either 2, 4, 6, 12 customers
- Reservations can occur between 5 pm to 11 pm
- Cleaning and seating tables require 10 minutes between customers

use any api testing platform to test this apis

- make a `GET` request to `http://localhost:8000/tables/` to get the list of tables and there reservations

```sh
# Example 
GET http://localhost:8000/tables/

## output
{
    "tables_count": 2,
    "table": [
        {
            "table number": 1,
            "reservations": [
                {
                    "checkin": "2022-03-02T18:29:05",
                    "checkout": "2022-03-02T18:39:05"
                },
                {
                    "checkin": "2022-03-02T22:29:05",
                    "checkout": "2022-03-02T22:39:05"
                },
            ]
        },
        {
            "table number": 2,
            "reservations": []
        }
    ]
}

```

- make a `POST` request to `http://localhost:8000/reservation/` and add body with required parameters to make a reservation

```sh
# Example 
POST http://localhost:8000/reservation/

body :
{
    "table number":1,
    "checkin":"2022-03-02 20:29:05",
    "checkout":"2022-03-02 20:30:05",
    "people_count":4
}

## output
{
    "message": "sucessfully created the reservation"
}

```

- Also, you can also check the Django Admin page by navigating to `http://localhost:8000/admin` and using username `admin` and password `admin`
( Note: this project is for demo purpose, so i have share admin username and password)
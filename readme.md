# HaE Challenge Project

## Requirements

TimeEntry CRUD with fields:

* Time spent, in minutes
* Date of entry
* Summary of work completed
* Associated job (via UUID)

Job CRUD with fields:

* Title
* Hourly rate
* Tax rate

Dynamic creation of "Invoice" parameterized on job and date range returning the folliwing fields:

* Job
* Date range
* Time entries in range
* $ subtotal (hourly rate * total minutes / 60)
* $ tax (subtotal * tax rate)
* $ total

Front-end must allow for interaction via JSON dictionaries


## Installation

Create a new virtual environment with python2.7 and activate it

Install requirements.txt with pip

Run migrations > `python manage.py migrate`

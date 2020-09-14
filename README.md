# tyba
Framework: Python Eve (Python 3.7+)
Database: Mongo
Tables: users, transactions

To make Register:

POST - http://localhost:5000/users/register

DATA:

{
    "first_name": "user 1",
    "last_name": "last 1",
    "email": "somemail@hotmail.com",
    "password": "123456"
}

To make login:

POST - http://localhost:5000/users/login
DATA:

{
    "email": "somemail@hotmail.com",
    "password": "123456"
}

To search restaurants by locations or city name. You need to send the query with *city* or *lat* and *lon* 

Examples:
GET http://localhost:5000/restaurants?city=new york

GET http://localhost:5000/restaurants?lat=40.7223277778&lon=-73.9873500000



TO run application, simply cd into tyba and type:
python app.py

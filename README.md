fibonacci-api
=============

The REST API for generating [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence).


To install requirements:

`pip install -r requirements.txt`

To run tests:

`nosetests`

To run the application:

`python resources.py`

Test in your browser:

[http://localhost:5000/fibonacci/10](http://localhost:5000/fibonacci/10)

Test using curl command:

`curl -i -X GET "http://localhost:5000/fibonacci/10"`

invalid path parameter with number greater than upper boundary - returns 400:

`curl -i -X GET "http://localhost:5000/fibonacci/10000"`

invalid path parameter with negative number - returns 400:

`curl -i -X GET "http://localhost:5000/fibonacci/-10"`

invalid http method - returns 405:

`curl -i -X POST "http://localhost:5000/fibonacci/10000"`

invalid path - returns 404:

`curl -i -X POST "http://localhost:5000/fibonacci/bad/bad"`

Running tests on different Python versions using Tox. Currently configured to run against py27 and py34:

`tox`

# Order Service

This repo contains the code that allows a customer to make an order and get an alert. The SMS alert is send using the African's Talking API. 

# Requirements
* Python (3.11.8)

Please install the dependencies via the `requirements.txt` file using 
```commandline
pip install -r requirements.txt
```
If you don't have Pip installed please follow instructions online on how to do it.

# How To Run the Unit Tests
To run the Unit Tests, from the root of the repo run
```commandline
coverage run -m pytest  -v -s
```

If you have any questions about the project please raise an Issue on GitHub. 

[![Coverage Status](coverage.svg)](https://github.com/OkothPius/Order-Service)

# Coding Challenge
This repository contains the solution for the coding task given by Adnymics GmbH. The coding challenge involves mainly two tasks where the 1st task is related to the Linux command and the second task is related to the python coding challenge. 

### Repository structure

The structure of the repository is as follows-

``` 
├── docs
│   ├── Task_1_solution.docx    # solution to the  Task_1 
│   └── Task_2_solution.docx    #  Approach and  assumption of the Task_2  
├── source
│   ├── fibonacci.py   # script generates the combination of fibonnaci  numbers for a  given number
│   ├── __init__.py
│   ├── main.py   #  A Flask-RESTful API is implemented  with health endpoint.        
├── requirements.txt   #  list of dependencies to run the source code.
├──  README.md   # README file of the  project repository.
└── tests    # This directory contains the  test scripts.
``` 

### Steps to Run the scripts

#### Environment setup  (for linux): 

Firstly, create a virtual environment (useful to manage independently packages dependencies).
All the below commands need to be issued at the root directory of the project. 

Install the virtualenv tool using your package manager:

    sudo apt install virtualenv

Now, create a Python virtual environment and choose 3.6 as the Python version. 

    virtualenv --python=python3 venv
Activate the newly created virtual environment:

    source venv/bin/activate
     
Now, install the dependencies of the project. 

    pip install -r requirements.txt


#### Run the Flask API
From the root directory of the project, issue the following command from the terminal. 

    python source/main.py

Now issue the following command from another terminal window

    curl http://0.0.0.0:5000/fib/6

Then the response of the API (sample output) is shown below

        {
        "result":   [
                        [
                            3,
                            3
                        ],
                        [
                            2,
                            2,
                            2
                        ]
                    ]
        }


The response code of the request can be seen on console output (refer to the last line) as 
 
      * Serving Flask app "main" (lazy loading)
      * Environment: production
      WARNING: This is a development server. Do not use it in a production deployment.
      Use a production WSGI server instead.
     * Debug mode: on
     * Running on http://0.0.0.0:5000/fib/6 (Press CTRL+C to quit)
     * Restarting with stat
     * Debugger is active!
     * Debugger PIN: 693-829-374
     0.0.0.0 - - [27/Sep/2020 10:22:56] "GET /fib/6 HTTP/1.1" 200 -


To check the health status of the API, issue the following command from the terminal window. 

    curl  http://0.0.0.0:5000/health/   

Then the response given by the API is shown below-

    {
    "health_status ": " Feel free to make the API requests to find the Fibonacci combinations"
    }

### Bonus point Tasks
#### Dockerising the service. 
Make sure you have docker and docker-compose installed. From root directory of project run the following command 
      
    docker-compose up

Issue the following command from another terminal window to make request to the API  

     curl http://localhost:5000/fib/6 


To stop API, issue the following command, issue the below command

    docker-compose down

#### Unit testing
To perform the unit testing of the API, Please **switch to the tests directory** from root directory of the project. 

    cd tests/ 

Now run the main_test.py script to test the API. 

     python main_test.py



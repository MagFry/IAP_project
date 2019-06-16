# IAP_project-hq-backend

## Development
Build a docker image:
```
./tasks docker_build
```

Deploy the application locally (2 docker containers):
```
./tasks up
```

Verify that API Server listens and answers:
```
$ curl -i -L localhost:8000/api/branch_offices/list
```

Add an employee:
```
$ curl -i -L localhost:8000/api/employees/list/2
# returns an empty list
$ cat my-emp.json
# {
#       "employee_id": 4,
#       "first_name": "Mag",
#       "last_name": "Fry",
#       "email": "mag123@wp.pl",
#       "date_of_birth": "1996-01-01",
#       "pay": 30,
#       "branch_office_id": 2
# }
$ curl -i -X POST localhost:8000/api/employees -d @my-emp.json -H 'Content-Type: text/json; charset=utf-8'
$ curl -i -L localhost:8000/api/employees/list/2
[
  {"employee_id": 1, "first_name": "Mag", "last_name": "Fry",
   "email": "mag123@wp.pl", "date_of_birth": "1996-01-01",
    "pay": 30.0, "branch_office_id": 2}
]
```

Delete the local application:
```
./tasks down
```
## Windows database link configuration

In file C:\Windows\System32\drivers\etc\hosts add line
127.0.0.1       db

##How to build project
1. pip install -r requirements.txt
2. python src/manage.py makemigrations
3. python src/manage.py migrate 
4. python src/manage.py runserver 8000
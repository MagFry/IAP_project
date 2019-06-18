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
#       "name": "Mag Fry",
#       "email": "mag123@wp.pl",
#       "date_of_birth": "1996-01-01",
#       "pay": 30,
#       "branch_office_id": 2,
#       "isManager": "false"
# }
$ curl -i -X POST localhost:8000/api/employees -d @my-emp.json -H 'Content-Type: text/json; charset=utf-8'
$ curl -i -L localhost:8000/api/employees/list/2
[
  {"employee_id": 1, "name": "Mag Fry", 
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

## How to build project
```
1. pip install -r requirements.txt
2. python src/manage.py makemigrations
3. python src/manage.py migrate 
4. python src/manage.py runserver 8000
```

## Implemented endpoints

###### BranchOffice
```
GET /api/branch_offices/list [Gets a collection of BranchOffice objects]
POST /api/branch_offices [Adds new Branch Office object]
GET /api/branch_offices/{branchOfficeId} [Gets a one Branch Office object]
DELETE /api/branch_offices/{branchOfficeId} [Delets a one Branch Office object]
PUT /api/branch_offices/{branchOfficeId} [Updates a one Branch Office object]
```

###### Employee
```
GET /api/employees/list/{branchOfficeId} [Gets a collection of Employees objects for given Branch Office]
GET /api/employees/all [Gets a collection of Employees objects]
POST /api/employees [Adds a new Employee object]
GET /api/employees/{employeeId} [Gets one Employees object]
DELETE /api/employees/{employeeId} [Deletes an Employee object]
PUT /api/employees/{employeeId} [Updates an existing Employee object]
```
###### Salary and Hours
```
[TODO]GET /api/salaries/list [Gets a collection of Salary objects]
GET /api/branch_offices/{branchOfficeId}/employee/{employeeId}/employee_hours [Gets a collection of Hours objects for given employee in given branch office]
```

## API Server endpoints examples

#### Branch Office part
Gets a collection of BranchOffice objects
```
curl -i -L localhost:8000/api/branch_offices/list
```
To add branch office 
```
curl -i -X POST localhost:8000/api/branch_offices -d "{""branch_office_name"": ""French_school"", ""branch_office_location"": ""Wawa""}"
curl -i -X POST localhost:8000/api/branch_offices -d "{""branch_office_name"": ""English_school"", ""branch_office_location"": ""Lodz""}"
```
To show branch office with id=1
```
curl -i -L localhost:8000/api/branch_offices/1
```
To delete branch office with id=2
```
curl -X DELETE localhost:8000/api/branch_offices/2
```
To update branch office with id=1 (changing name from English_school to Spanish_school)
```
curl -X PUT -d "{""branch_office_name"": ""Spanish_school"", ""branch_office_location"": ""Lodz""}" localhost:8000/api/branch_offices/1
```

#### Employee part
To show list of all employees
```
curl -i -L localhost:8000/api/employees/all
```
To add employee to a given branch_office
```
curl -i -X POST localhost:8000/api/employees -d "{""employee_id"": 4,""name"": ""Mag Fry"",""email"": ""mag123@wp.pl"",""date_of_birth"": ""1996-01-01"",""pay"": 30,""branch_office_id"": 2,""isManager"": ""false""}"
```
To show employee of branch_office with id=2
```
curl -i -L localhost:8000/api/employees/list/2
```
To delete employee with id = 4
```
curl -X DELETE localhost:8000/api/employees/4
```
To update employee with id = 4 (changing pay value from 30 to 50)
```
curl -X PUT -d "{""employee_id"": 4,""name"": ""Mag Fry"",""email"": ""mag123@wp.pl"",""date_of_birth"": ""1996-01-01"",""pay"": 50,""branch_office_id"": 2,""isManager"": ""false""}" localhost:8000/api/employees/4
```

#### Synchronization in HQ from BO
1. Checking the content of employee_hours in HQ
```
curl -i -L http://127.0.0.1:8000/api/employee_hours/list
```
2. Add an hours in BO
```
curl -i -X POST localhost:8080/api/employee_hours -d "{""value"": ""60"", ""employeeId"": ""2"", ""timePeriod"": ""20.06.2019-26.05.2019"" }" -H 'Content-Type:text/json;charset=utf-8'
```
3. Check that it was added in BO
```
curl -i  localhost:8080/api/employee_hours/list_all
```
4. Checking if added hours in BO exists in HQ
```
curl -i -L http://127.0.0.1:8000/api/employee_hours/list
```
5. Returning hours for given employee (id = 1) in given branch office (id=1) which were retrieved from BO
```
curl -i -L http://localhost:8000/api/branch_offices/1/employees/1/employee_hours
```

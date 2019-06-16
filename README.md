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
curl -i -L localhost:8000/api/branch_offices/list
curl -i -L localhost:8000/api/employees/list/0
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
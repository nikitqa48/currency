### START PROJECT
````
docker-compose -f docker-compose.yml up --build -d 
````

### DOCS
http://localhost:8000/docs/


### Alembic create migrations
don't turn off container and run
```
docker-compose run web alembic revision --autogenerate -m 'migration name'
```
### apply migration
```
docker-compose run web alembic upgrade head 
```

### example API


### GET /refresh/

http://localhost:8000/refresh/

### Response
HTTP/1.1 200 ok
Date: Thu, 24 Feb 2011 12:36:30 GMT
Status: 200 ok
Connection: close
Content-Type: application/json
Content-Length: 4


### POST /convert/

http://localhost:8000/convert/

BODY: 
```
{
    "original": "USD",
    "target": "RUB",
    "amount": 10000
}
```
### Response
HTTP/1.1 200 ok
Date: Thu, 24 Feb 2011 12:36:30 GMT
Status: 200 ok
Connection: close
Content-Type: application/json
Content-Length: 4

109.6513


### GET /last_update/

http://localhost:8000/last_update/

### Response
HTTP/1.1 200 ok
Date: Thu, 24 Feb 2011 12:36:30 GMT
Status: 200 ok
Connection: close
Content-Type: application/json
Content-Length: 4

"2024-02-28T22:57:45.836333+00:00"
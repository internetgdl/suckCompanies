# Shitty Companies api v0.0.0.1-beta

Para acceder a los recursos de la API es necesario obtener un token.
Para obtener un token lo pueden realizar de la siguiente manera:

### Url api
```json
http://13.84.176.27
```

### Path Autenticacion
```json
/o/token/
```

HTTP POST
```http
POST /o/token/ HTTP/1.1
Host: 13.84.176.27:8000
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache
Postman-Token: 0d5cbbb5-c21c-8034-97e7-57f510ab8e76

username=demo1&password=demo123ABCD&grant_type=password&client_id=k0JDpdJ7mR9blVZ4YK7yiAdtvqMWFbJEf72tC6p6&client_secret=ReOqMLbMZCgjNvx8ytLGT1fp4LcKbbVpJJyqlmNMrmAwGnQCq9KmEOmPNxYITK1IcFlZKQsqmADEqzhFoFLGA5b02JHkGLcFwkI4EmHrOzdemwddKrzOGaHuu5PVW51Q
```

Javascript Jquery AJAX
```javascript
var settings = {
  "async": true,
  "crossDomain": true,
  "url": "http://13.84.176.27:8000/o/token/",
  "method": "POST",
  "headers": {
    "content-type": "application/x-www-form-urlencoded",
    "cache-control": "no-cache",
    "postman-token": "635e87b9-0456-3470-23b0-5648c4afb346"
  },
  "data": {
    "username": "demo1",
    "password": "demo123ABCD",
    "grant_type": "password",
    "client_id": "k0JDpdJ7mR9blVZ4YK7yiAdtvqMWFbJEf72tC6p6",
    "client_secret": "ReOqMLbMZCgjNvx8ytLGT1fp4LcKbbVpJJyqlmNMrmAwGnQCq9KmEOmPNxYITK1IcFlZKQsqmADEqzhFoFLGA5b02JHkGLcFwkI4EmHrOzdemwddKrzOGaHuu5PVW51Q"
  }
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

Uno de los recursos de la Api es la consulta de compañias.
Puedes filtrar u obtener todas las compañias registradas en la aplicación.


### Path Consulta Compañias
```http
/app/api/companies/
```
### Consulta completa de compañias registradas.

HTTP GET
```http
GET /app/api/companies/ HTTP/1.1
Host: 13.84.176.27:8000
Authorization: bearer XhwXwHUKtOmGfXBxJr8pI7vEI6PddH
```

Javascript AJAX
```javascript
var settings = {
  "async": true,
  "crossDomain": true,
  "url": "http://13.84.176.27:8000/app/api/companies/",
  "method": "GET",
  "headers": {
    "authorization": "bearer XhwXwHUKtOmGfXBxJr8pI7vEI6PddH"
  }
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

### Consulta de compañias registradas utilizando un filtro.

HTTP GET
```http
GET /app/api/companies/?filter=lalo HTTP/1.1
Host: 13.84.176.27:8000
Authorization: bearer XhwXwHUKtOmGfXBxJr8pI7vEI6PddH
```

Javascript AJAX
```javascript
var settings = {
  "async": true,
  "crossDomain": true,
  "url": "http://13.84.176.27:8000/app/api/companies/?filter=lalo",
  "method": "GET",
  "headers": {
    "authorization": "bearer XhwXwHUKtOmGfXBxJr8pI7vEI6PddH"
  }
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

### Path Alta de Compañias
```http
/app/api/companies/
```

### Alta de Compañias

HTTP POST
```json
POST /app/api/companies/ HTTP/1.1
Host: 13.84.176.27:8000
Authorization: bearer XhwXwHUKtOmGfXBxJr8pI7vEI6PddH
Content-Type: application/json

{
	"name":"lalo123",
	"complain": "chido",
	"category":"liro"
}
```
Javascript AJAX
```javascript
var settings = {
  "async": true,
  "crossDomain": true,
  "url": "http://13.84.176.27:8000/app/api/companies/",
  "method": "POST",
  "headers": {
    "authorization": "bearer XhwXwHUKtOmGfXBxJr8pI7vEI6PddH",
    "content-type": "application/json",
  },
  "processData": false,
  "data": "{\n\t\"name\":\"lalo123\",\n\t\"complain\": \"chido\",\n\t\"category\":\"liro\"\n}"
}

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

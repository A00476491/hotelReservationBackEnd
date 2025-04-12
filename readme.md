# Hotel Reservation Backend

This is the backend part of a hotel reservation system, built with Django. The application allows users to browse available hotels and make reservations through a simple and intuitive interface.

## Author

**Pengyao Zhao** (English name: Max)  
**Student ID:** A00476491

## Data Models

### Hotels

| Field     | Type               | Description                  |
|-----------|--------------------|------------------------------|
| id        | AutoField (PK)     | Hotel ID                     |
| name      | CharField(500)     | Hotel name                   |
| price     | DecimalField       | Hotel price                  |
| available | BooleanField       | Availability (True/False)    |

### Reservation

| Field               | Type                   | Description                       |
|--------------------|------------------------|-----------------------------------|
| reservation_id     | BigAutoField (PK)      | Reservation ID                    |
| hotel              | ForeignKey to Hotels   | Linked hotel                      |
| checkin            | DateField              | Check-in date                     |
| checkout           | DateField              | Check-out date                    |
| confirmation_number| CharField(16)          | Default: TEMPCONFIRM123456        |

### Guest

| Field       | Type                     | Description                  |
|-------------|--------------------------|------------------------------|
| guest_id    | BigAutoField (PK)        | Guest ID                     |
| reservation | ForeignKey to Reservation| Linked reservation           |
| name        | CharField(200)           | Guest name                   |
| gender      | CharField(20)            | Guest gender                 |

## APIs

The backend includes four APIs:
- `get_all_hotels` – Get all hotel data  
- `get_all_reservations` – Get all reservation data  
- `get_all_guests` – Get all guest data  
- `create_reservation` – Create a reservation and return a confirmation number  

## Frontend Repository

The corresponding frontend can be found at:  
[https://github.com/A00476491/hotelResevationFrontEnd.git](https://github.com/A00476491/hotelResevationFrontEnd.git)

## How to Run

### Local

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Use Postman to test:

- http://127.0.0.1:8000/api/hotels/  
- http://127.0.0.1:8000/api/guests/  
- http://127.0.0.1:8000/api/reservations/  

### Cloud

```bash
ssh -i "./hotel_back_end.pem" ubuntu@13.58.53.22
source venv/bin/activate
cd ./hotelReservationPlatformBackEnd
gunicorn --workers 3 hotel_project.wsgi:application --bind 0.0.0.0:8000
```

Use Postman to test:

- http://13.58.53.22/api/hotels/  
- http://13.58.53.22/api/guests/  
- http://13.58.53.22/api/reservations/
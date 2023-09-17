from django.db import models

# Create your models here.
class accounts(models.Model):
    fname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 20)
    username = models.CharField(max_length = 15)
    password = models.CharField(max_length = 20)
    confirm_password = models.CharField(max_length = 20)
    email=models.EmailField(max_length=30)
    contact = models.IntegerField()
    
class events(models.Model):
    event_type = models.CharField(max_length=20)
    capacity = models.IntegerField()
    pricing = models.IntegerField()

class venue(models.Model):
    address = models.CharField(max_length=20)
    contact = models.IntegerField()

class booking(models.Model):
    email = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    contact = models.IntegerField()
    date = models.DateField()
    event_type = models.CharField(max_length=20)
    date_of_event = models.DateField()
    event_time = models.TimeField()
    event_location = models.CharField(max_length=20)

class booked(models.Model):
    client_email = models.CharField(max_length=20)
    client_name = models.CharField(max_length=20)
    client_contact = models.IntegerField()
    booking_date = models.DateField()
    booked_event_type = models.CharField(max_length=20)
    booked_date_of_event = models.DateField()
    booked_event_time = models.TimeField()
    booked_event_location = models.CharField(max_length=20)
    status = models.CharField(max_length=30)

class payment(models.Model):
    payment_type = models.CharField(max_length=20)
    payment_status = models.CharField(max_length=20)
    transaction_id = models.IntegerField(max_length=20)
    amount = models.IntegerField(max_length=11)
    transaction_date = models.DateField(max_length=20)
    transaction_time = models.TimeField(max_length=20)

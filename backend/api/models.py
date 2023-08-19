from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from datetime import datetime
import uuid
import os

class User(AbstractUser):
    def get_path(instance, filename):
        ext = filename.split('.')[-1]
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f'{timestamp}_{uuid.uuid4().hex}.{ext}'
        return os.path.join('images/profilepicture/', filename)
    
    ROLES = (
        ('customer', 'Customer'),
        ('event_organizer', 'Event Organizer'),
        ('administrator', 'Administrator'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=150, unique=True, blank=False)
    email = models.EmailField(unique=True, blank=False)
    phone_number = models.CharField(max_length=15, unique=True, blank=False,default='0812')
    # password = models.CharField(max_length=128)
    image = models.ImageField(upload_to=get_path, blank=True)
    role = models.CharField(max_length=15, choices=ROLES, default='customer', blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)

    def __repr__(self):
        return f'{self.username}, {self.email}, {self.role}'

class Event(models.Model):
    def get_path(instance, filename):
        ext = filename.split('.')[-1]
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f'{timestamp}_{uuid.uuid4().hex}.{ext}'
        return os.path.join('images/eventpicture/', filename)
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    title = models.CharField(max_length=255, blank=False)
    image = models.ImageField(upload_to=get_path, blank=True)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.TextField()
    category = models.CharField(max_length=255)
    ticket_quantity = models.IntegerField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    is_verified = models.BooleanField(default=True)
    message = models.TextField()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_events')
    created_at = models.DateTimeField(auto_now_add=True)

class Ticket(models.Model):
    title = models.CharField(max_length=255)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class UserTicket(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class EventOrganizerProposal(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class SalesData(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

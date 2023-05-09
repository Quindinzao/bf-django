from django.db import models

class Ticket(models.Model):
    id_ticket = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255)
    years_old = models.IntegerField()
    email = models.TextField(max_length=255)
    cpf = models.TextField(max_length=11)
    card_number = models.TextField(max_length=16)
    cvv = models.TextField(max_length=3)

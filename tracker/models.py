from django.db import models
from django.contrib.auth.models import User

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)  # Link income to a user
    amount = models.FloatField()                               # Amount of income
    source = models.CharField(max_length=100)                 # Source description
    date = models.DateField(auto_now_add=True)                # Auto set date when created

    def __str__(self):
        return f"{self.source} - {self.amount}"              # Human-readable representation

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)  # Link expense to a user
    amount = models.FloatField()                               # Amount of expense
    category = models.CharField(max_length=100)               # Category description
    date = models.DateField(auto_now_add=True)                # Auto set date when created

    def __str__(self):
        return f"{self.category} - {self.amount}"            # Human-readable representation
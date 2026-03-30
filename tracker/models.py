from django.db import models
from django.contrib.auth.models import User

# Income Model
class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    amount = models.FloatField()
    source = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.amount)

# Expense Model
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    amount = models.FloatField()
    category = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.amount)
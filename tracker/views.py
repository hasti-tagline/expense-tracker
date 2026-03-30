from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Income, Expense
from django.db.models import Sum
from django.db.models.functions import TruncMonth

@login_required
def dashboard(request):
    income = Income.objects.filter(user=request.user).aggregate(Sum('amount'))['amount__sum'] or 0
    expense = Expense.objects.filter(user=request.user).aggregate(Sum('amount'))['amount__sum'] or 0

    balance = income - expense

    return render(request, 'dashboard.html', {
        'income': income,
        'expense': expense,
        'balance': balance
    })


@login_required
def monthly_report(request):
    income_data = Income.objects.filter(user=request.user)\
        .annotate(month=TruncMonth('date'))\
        .values('month')\
        .annotate(total=Sum('amount'))

    expense_data = Expense.objects.filter(user=request.user)\
        .annotate(month=TruncMonth('date'))\
        .values('month')\
        .annotate(total=Sum('amount'))

    return render(request, 'report.html', {
        'income_data': income_data,
        'expense_data': expense_data
    })
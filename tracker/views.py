from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Income, Expense
from .forms import IncomeForm, ExpenseForm
from django.db.models import Sum

@login_required
def dashboard(request):
    income_total = Income.objects.filter(user=request.user).aggregate(Sum('amount'))['amount__sum'] or 0
    expense_total = Expense.objects.filter(user=request.user).aggregate(Sum('amount'))['amount__sum'] or 0

    context = {
        'income_total': income_total,
        'expense_total': expense_total,
    }
    return render(request, 'tracker/dashboard.html', context)

@login_required
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('dashboard')
    else:
        form = IncomeForm()
    return render(request, 'tracker/add_income.html', {'form': form})

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('dashboard')
    else:
        form = ExpenseForm()
    return render(request, 'tracker/add_expense.html', {'form': form})

@login_required

def monthly_report(request):
    # Aggregate income per month
    income_qs = (
        Income.objects.filter(user=request.user)
        .values('date__year', 'date__month')
        .annotate(total=Sum('amount'))
        .order_by('date__year', 'date__month')
    )
    # Add a "month" key in YYYY-MM format for JS/chart
    income_data = [
        {
            'month': f"{item['date__year']}-{str(item['date__month']).zfill(2)}",
            'total': item['total']
        }
        for item in income_qs
    ]

    # Aggregate expense per month
    expense_qs = (
        Expense.objects.filter(user=request.user)
        .values('date__year', 'date__month')
        .annotate(total=Sum('amount'))
        .order_by('date__year', 'date__month')
    )
    expense_data = [
        {
            'month': f"{item['date__year']}-{str(item['date__month']).zfill(2)}",
            'total': item['total']
        }
        for item in expense_qs
    ]

    return render(request, 'tracker/report.html', {
        'income_data': income_data,
        'expense_data': expense_data
    })
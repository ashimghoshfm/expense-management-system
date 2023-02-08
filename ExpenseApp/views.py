from django.shortcuts import render
from django.views.generic import ListView  # for class based function

from .models import DailyExpense

# Create your views here.


# class ExpenseView(ListView):
#     model = DailyExpense
#     template_name = 'index.html'


def home(request):
#================== date filter start ======================#
    if request.method == 'POST':
        date = request.POST.get('date')
        all_data = DailyExpense.objects.filter(date__exact=date)
        return render(request, 'index.html',{'alldata':all_data})
#================== date filter end ======================#


    all_data = DailyExpense.objects.all()
    return render(request, 'index.html',{'alldata':all_data})







#================== Class based function method ======================#

# def filterdate(request):
#     if request.method=='POST':
#         dd =request.POST.get('date')
#         print(dd)
#     return render(request, 'index.html')

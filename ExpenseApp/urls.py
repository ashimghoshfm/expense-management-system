from django.urls import path

from . import views

urlpatterns = [
    # path('', views.ExpenseView.as_view(), name='ExpenseHome'),
    path('', views.home, name='home'),
    # path('filterdate/', views.filterdate, name='filterdate'),
]

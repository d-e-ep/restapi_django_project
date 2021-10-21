from django.conf.urls import urls
from django.conf.urls import url
from crud import views

urlpattern=[
    url(r'^employee$',views.Employeeapi),
    url(r'^employee/([0-9]+)$',views.views.Employeeapi)
]
"""Airport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Technician/', views.TechnicianView.as_view()),
    path('Technician/<int:ssn>/', views.TechnicianView.as_view()),
    path('Airplane/', views.AirplaneView.as_view()),
    path('Airplane/<int:regnum>/', views.AirplaneView.as_view()), # all airplan
    path('Employee/', views.EmployeeView.as_view()),
    path('Employee/<int:ssn>/', views.EmployeeView.as_view()), # Employee Details
    path('Test/', views.TestView.as_view()),
    path('Test/<int:mno>/', views.TestView.as_view()), # ffa test record by model num
    path('TestRec/', views.TestRecordsView.as_view()),
    path('TestRec/<int:regnum>/', views.TestRecordsView.as_view()), # get test record for regnum
    path('Monitor/', views.MonitorView.as_view()),
    path('Monitor/<int:regnum>/', views.MonitorView.as_view()),  # get monitor by regnum
    path('MonitorATC/<int:ssn>/', views.MonitorATCView.as_view()), # get monitor by ssn
    path('PlanTestSch/<int:ssn>/', views.PlanTestSchView.as_view()), # get the test record by ssn
    path('Add/<int:ssn>/', views.PlanTestSchView.as_view()),
]

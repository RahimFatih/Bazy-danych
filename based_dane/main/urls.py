from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="login"),
    path('home', views.home, name="home"),
    path('report', views.report, name="report"),
    path('report_view/<int:pk>', views.report_view, name="report_view"),
    path('report_list', views.report_list, name="report_list"),
    path('logout/',views.logoutUser, name='logout'),
]
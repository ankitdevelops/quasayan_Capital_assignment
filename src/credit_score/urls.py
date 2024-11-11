from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("submit/", views.sumbit_form, name="submit"),
    path("result/", views.result_page, name="result"),
]

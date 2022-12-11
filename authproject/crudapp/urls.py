from django.urls import path
from . import views

urlpatterns=[
    path("",views.home),
    path("delete/<int:id>",views.delete),
    path('save',views.save)
]
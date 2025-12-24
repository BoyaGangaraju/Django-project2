from django.urls import path
from .views import about,login

urlpatterns=[

    path("about/",about),
    path("login/",login)
]
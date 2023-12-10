import json

from django.http import HttpResponse
from django.urls import path

from . import views


def hello(request):
    print("hello")
    return HttpResponse(
        json.dumps(dict(status="ok", message="pong")), content_type="application/json"
    )


urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("health/", hello, name="health"),
]

from django.conf.urls import url
from test_app import views

urlpatterns=[
    url(r'^machine$',views.machineApi),
    url(r'^machine/([0-9]+)$',views.machineApi)
]
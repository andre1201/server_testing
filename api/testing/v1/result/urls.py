from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list/', views.ListView.as_view()),
    url(r'^one/(?P<pk>\d+)/', views.SingleView.as_view()),
]

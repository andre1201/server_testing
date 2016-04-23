from django.conf.urls import include, url

urlpatterns = [
    url(r'^testing/', include('api.testing.urls', namespace='testing')),
]
from django.conf.urls import include, url

urlpatterns = [
    url(r'^v1/', include('api.testing.v1.urls', namespace='testing')),
]
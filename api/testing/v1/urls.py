from django.conf.urls import include, url

urlpatterns = [
    url(r'^test/', include('api.testing.v1.test.urls')),
    url(r'^question/', include('api.testing.v1.question.urls')),
    url(r'^answer/', include('api.testing.v1.answer.urls')),
    url(r'^result/', include('api.testing.v1.result.urls')),
]

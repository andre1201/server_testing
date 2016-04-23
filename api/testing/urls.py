from django.conf.urls import include, url

urlpatterns = [
    url(r'^test/', include('api.testing.test.urls')),
    url(r'^question/', include('api.testing.question.urls')),
    url(r'^answer/', include('api.testing.answer.urls')),
    url(r'^result/', include('api.testing.result.urls')),
]

from django.urls import path

from .views import IndexView, RedirectionView, InfoView

app_name = 'shortener'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<slug:slug>/info', InfoView.as_view(), name='info'),
    path('<slug:slug>', RedirectionView.as_view(), name='redirection'),
]

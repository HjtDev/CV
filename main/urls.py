from django.urls import path
from . import views


app_name = 'main'


urlpatterns = [
    path('', views.index_view, name='index'),
    path('contact/', views.contact_view, name='contact'),
    path('ajax/<portfolio>/', views.get_portfolio_view, name='get_portfolio'),
]
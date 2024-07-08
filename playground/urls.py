from django.urls import path
from . import views

urlpatterns = [
    path('', views.site, name='home'),
    path('member/', views.member),
    path('member/details/<int:id>', views.details)
]

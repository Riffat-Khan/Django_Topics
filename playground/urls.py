from django.urls import path
from . import views

urlpatterns = [
    path('', views.site, name='home'),
    path('models/', views.get_all_data),
    path('queries/', views.queries),
    path('member/', views.member),
    path('member/details/<int:id>', views.details)
]

from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register', views.register.as_view(), name='register'),
    path('login/',obtain_auth_token, name='login'),

    path('book/', views.BookAPIView.as_view(), name='book'),
    path('detail/<int:id>', views.BookDetails.as_view(), name="details")
]
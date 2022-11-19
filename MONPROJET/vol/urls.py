from django.urls import path
from vol import views
urlpatterns = [
    path('', views.home),
    path('list/', views.compagnie_view),

]

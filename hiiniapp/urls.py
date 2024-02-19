
from django.contrib import admin
from django.urls import path
from hiiniapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home ),
    path('',views.images ),
    path('About/',views.about ),
    path('collection/',views.collection ),
]

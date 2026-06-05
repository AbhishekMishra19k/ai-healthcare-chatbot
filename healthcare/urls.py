from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chatbot.urls')),
    path('appointments/', include('appointments.urls')),
    path('medicines/', include('medicines.urls')),
    path('accounts/', include('accounts.urls')),
]
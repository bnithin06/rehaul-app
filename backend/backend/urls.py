from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('home.urls')),
    path('auth/',include('accounts.urls')),
    path('driver/',include('driver.urls')),
    path('lorry-owners/', include('lorry_owners.urls')),
    path('businesses/', include('businesses.urls')),
    path('admin/', admin.site.urls),
]

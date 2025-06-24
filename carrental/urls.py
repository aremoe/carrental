from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from cars import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', include('cars.urls')),
    path('', views.all_cars, name='all_cars'),
    path('available/', views.available_cars, name='available_cars'),
    path('<int:car_id>/', views.car_detail, name='car_detail'),
    path('add/', views.add_car, name='add_car'),
    path('<int:car_id>/edit/', views.edit_car, name='edit_car'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

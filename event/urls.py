from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.login, name="Login"),
  path('home/', views.home, name="Home"),
  path('event/<int:no>', views.event_description, name="event"),
  path('add_event/', views.add_event, name="Add_event"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

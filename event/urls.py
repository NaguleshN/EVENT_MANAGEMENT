from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
  path('login/', views.login, name="login"),
  path('logout/', views.logout_view , name="logout"),
  path('', views.home, name="Home"),
  path('event/<int:no>', views.event_description, name="event"),
  path('add_event/', views.add_event, name="Add_event"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

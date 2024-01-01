from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
  path('login/', views.login, name="login"),
  path('logout/', views.logout_view , name="logout"),
  path('home/', views.home, name="Home"),
  path('event/<int:no>', views.event_description, name="event"),
  path('add_event/', views.add_event, name="Add_event"),
  path('', views.index, name='index'),
  path('description/<int:id>/', views.description, name='description'),
  path('admin_view/', views.admin, name="admin"),
  path('accept_order/<int:order_id>/', views.accept_order, name='accept_order'),
  path('reject_order/<int:order_id>/', views.reject_order, name='reject_order'),
  path('accepted_events/', views.accepted_event, name="accepted_event"),
  path('add_da_member/', views.add_da_member, name="add_da_member"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

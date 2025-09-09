
from django.contrib import admin
from django.urls import path,include
from core.views import home,no_permission
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('event/',include('events.urls')),
    path('user/',include('event_users.urls')),
    path('',home,name='home'),
    path("no_parmission/",no_permission,name="no_permission")
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

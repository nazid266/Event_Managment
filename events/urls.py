from django.urls import path
from events.views import main_dashboard,detail,creat_event,event_category,event_delete,event_update,delete_category,update_category,rsvp_event,participant_dashboard,dashboar
urlpatterns = [
    path('main_dashboard/',main_dashboard,name='main_dashboard'),
    path('event_detail/<int:id>',detail,name='event_detail'),
    path('create_event/',creat_event,name='create_event'),
    path('category_event/',event_category,name='category_event'),
    path('event_detail/<int:id>',detail,name='event_detail'),
    path("delete_event/<int:id>",event_delete,name="delete_event"),
    path("update_event/<int:id>",event_update,name="update_event"),
    path('delete_category/<int:id>',delete_category,name='delete_category'),
    path('update_category/<int:id>',update_category,name='update_category'),
    path("rsvp_event/<int:id>",rsvp_event,name="rsvp_event"),
    path('participant_dashboard/',participant_dashboard,name="participant_dashboard"),
    path("dashboard/",dashboar,name="dashboard")
    
    
]


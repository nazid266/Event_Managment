from django.urls import path
from events.views import main_dashboard,detail,creat_event,event_category,event_participant,event_delete,event_update,delete_category,update_category,delete_participant,update_participant
urlpatterns = [
    path('main_dashboard/',main_dashboard,name='main_dashboard'),
    path('event_detail/<int:id>',detail,name='event_detail'),
    path('create_event/',creat_event,name='create_event'),
    path('category_event/',event_category,name='category_event'),
    path('participant_event/',event_participant,name='participant_event'),
    path("delete_event/<int:id>",event_delete,name="delete_event"),
    path("update_event/<int:id>",event_update,name="update_event"),
    path('delete_category/<int:id>',delete_category,name='delete_category'),
    path('update_category/<int:id>',update_category,name='update_category'),
    path('delete_participant/<int:id>',delete_participant,name='delete_participant'),
    path('update_participant/<int:id>',update_participant,name='update_participant')
    
]


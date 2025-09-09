from django.urls import path
from event_users.views import sing_up,sing_in,sing_out,activate_user,role_assign,create_group,admin_dashboard,group_list,delete_perticipant


urlpatterns = [
    path('sing_up/',sing_up,name='sing_up'),
    path('sing_in/',sing_in,name='sing_in'),
    path('sing_out/',sing_out,name='sing_out'),
    path('activate/<int:user_id>/<str:token>/',activate_user,name='activate_user'),
    path('assign_role/<int:id>/',role_assign,name="assign_role"),
    path("admin/create_group/",create_group,name="create_group"),
    path("admin/dashboard/",admin_dashboard,name="admin_dashboard"),
    path("admin/group_list/",group_list,name="group_list"),
    path("delete_participants/<int:id>/",delete_perticipant,name="delete_participants")
    
    
]

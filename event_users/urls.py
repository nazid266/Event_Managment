from django.urls import path
from event_users.views import sing_up,sing_in,sing_out,activate_user,role_assign,create_group,admin_dashboard,group_list,delete_perticipant,UserProfile,ChangePassword,PasswordResetView,PasswordResetConfirmView,EditProfile
from django.contrib.auth.views import PasswordChangeDoneView

urlpatterns = [
    path('sing_up/',sing_up,name='sing_up'),
    path('sing_in/',sing_in,name='sing_in'),
    path('sing_out/',sing_out,name='sing_out'),
    path('activate/<int:user_id>/<str:token>/',activate_user,name='activate_user'),
    path('assign_role/<int:id>/',role_assign,name="assign_role"),
    path("admin/create_group/",create_group,name="create_group"),
    path("admin/dashboard/",admin_dashboard,name="admin_dashboard"),
    path("admin/group_list/",group_list,name="group_list"),
    path("delete_participants/<int:id>/",delete_perticipant,name="delete_participants"),
    path('profile/',UserProfile.as_view(),name='profile'),
    path('change_password/',ChangePassword.as_view(),name='change_password'),
    path('change_password_done/',PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),name='password_change_done'),
    path('password_reset/',PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('edit_profile/',EditProfile.as_view(),name='edit_profile')
    
    
]

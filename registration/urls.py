from django.urls import path,include
from .import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/',views.register, name='register'),
    path('user_login/',views.UserLoginView.as_view(), name='user_login'),
    path('user_logout/',views.user_logout, name='user_logout'),
    # path('profile/edit',views.edit_profile, name='edit_profile'),
    path('edit_profile/', views.EditProfileView.as_view(), name='edit_profile'),
    path('profile/pass_change',views.pass_change, name='pass_change'),
    path('pass_change/', views.newPasswordChangeView.as_view(), name='pass_change'),
]

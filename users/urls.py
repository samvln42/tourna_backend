from django.urls import path
from users import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login_page"),
    path('signup/', views.SignupView.as_view(), name='signup_page'),
    path("userviewpage/", views.UserView.as_view(), name="my_page"),
    path("userviewpage-profile/", views.ChangeUserProfile.as_view(), name="ChangeUserProfile"),
    # Email Authentication
    path("send-email", views.SendEmail.as_view(), name="send_email"),
    path("check-email", views.CheckEmailView.as_view(), name="check_email"),
    path("check-token", views.CheckToken.as_view(), name="CheckToken"),
    path('admin-management/', views.AdminManagementView.as_view(), name='admin-management'),
    path('admin-management/<int:id>/', views.AdminManagementView.as_view(), name='admin-detail'),
    path('user-management/', views.UserManagementView.as_view(), name='user-management'),
    path('user-management/<int:id>/', views.UserManagementView.as_view(), name='user-delete'),
]

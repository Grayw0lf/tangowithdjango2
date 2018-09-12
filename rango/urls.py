from django.urls import path
from rango import views


app_name = 'rango'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('add-category/', views.add_category, name='add_category'),
    path('category/<category_name_slug>/add-page/', views.add_page, name='add_page'),
    path('category/<category_name_slug>/', views.show_category, name='show_category'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('goto/', views.track_url, name='goto'),
    path('restricted/', views.restricted, name='restricted'),
    path('register-profile/', views.register_profile, name='register_profile'),
    path('profile/<username>/', views.profile, name='profile'),
    path('profiles/', views.list_profiles, name='list_profiles'),
    path('like/', views.like_category, name='like_category'),
    path('suggest/', views.suggest_category, name='suggest_category'),
    path('add/', views.auto_add_page, name='auto_add_page'),
]

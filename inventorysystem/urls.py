from django.conf.urls import url
from . import views
from django.urls import path, re_path
from django.contrib.auth import views as auth_views

app_name = 'inventorysystem'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('store_list', views.store_list, name='store_list'),
    path('inventory_list', views.inventory_list, name='inventory_list'),
    path('store/<int:pk>/edit/', views.store_edit, name='store_edit'),
    path('inventory/<int:pk>/edit/', views.inventory_edit, name='inventory_edit'),
    path('store/<int:pk>/delete/', views.store_delete, name='store_delete'),
    path('inventory/<int:pk>/delete/', views.inventory_delete, name='inventory_delete'),
    path('store/<int:pk>/summary/', views.summary, name='summary'),
    path('inventory/create/', views.inventory_new, name='inventory_new'),
    path('store/create/', views.store_new, name='store_new'),
    path('password_change/',
         auth_views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('register/', views.register, name='register'),
]

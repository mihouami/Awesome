from django.contrib import admin
from django.urls import path, include
from a_posts.views import *
from a_users.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # ALL AUTH
    path('accounts/', include('allauth.urls')),
    
    # A_POSTS VIEWS
    path('', home_view, name='home'),
    path('category/<tag>/', home_view, name='category'),
    path('post/create/', post_create_view, name='post-create'),
    path('post/delete/<pk>/', post_delete_view, name='post-delete'),
    path('post/edit/<pk>/', post_edit_view, name='post-edit'),
    path('post/<pk>/', post_page_view, name='post'),
    
    # A_USERS VIEWS
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', profile_edit_view, name='profile-edit'),
    path('profile/<username>/', profile_view, name='userprofile'),
    path('profile/delete/profile/', profile_delete_view, name='profile-delete'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

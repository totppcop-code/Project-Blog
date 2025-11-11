from . import views
from django.urls import path 
from django.contrib.auth import views as auth_view

urlpatterns=[
    #文章
    path('',views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/',views.PostDetailView.as_view(), name='post-detail'),
    path('create/',views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/',views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/',views.PostDeleteView.as_view(), name='post-delete'),
    #留言 
    path('comment/',views.CommentListView.as_view(), name='comment-list'),
    path('comment/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),
    path('post/<int:pk>/comment/create/',views.CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
    #登入
    path('accounts/login/',auth_view.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/',auth_view.LogoutView.as_view(next_page='login'), name='logout' ),
    #讚 收藏 分享
    path('<int:pk>/like/', views.ToggleLikeView.as_view(), name='toggle-like'),
    path('<int:pk>/favorite/', views.ToggleFavoriteView.as_view(), name='toggle-favorite'),
    path('<int:pk>/share/',views.ToggleShareView.as_view(), name='toggle-share'),
]
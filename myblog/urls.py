from . import views
from django.urls import path 

urlpatterns=[
    path('',views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/',views.PostDetailView.as_view(), name='post-detail'),
    path('create/',views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/',views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/',views.PostDeleteView.as_view(), name='post-delete'),

    path('comment/',views.CommentListView.as_view(), name='comment-list'),
    path('comment/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),
    path('post/<int:pk>/comment/create/',views.CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
]
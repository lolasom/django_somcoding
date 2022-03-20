from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view()),  # 자동으로 post_detail.html로 연결해줌
    path('', views.PostList.as_view()),  # 자동으로 post_list.html로 연결해줌
    # path('<int:pk>/', views.single_post_page),
    # path('', views.index),
]
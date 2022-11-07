from django.urls import path, include
from feedback import views

app_name = 'feedback'
urlpatterns = [
    path('', views.FeedBackView.as_view(), name='feed_back'),
    path('success/', views.SuccessView.as_view(), name='feed_back_success'),
]

from django.urls import path
from .views import StatusAPIView
# StatusCreateAPIView,StatusUpdateAPIView,StatusDeleteAPIView,StatusDetailAPIViewStatusSearchAPIView,
urlpatterns = [
    # path('',StatusSearchAPIView.as_view(),name='search' ),
    path('',StatusAPIView.as_view(),name='search' ),
    # path('create/',StatusCreateAPIView.as_view(),name='search' ),
    # path('<int:id>',StatusDetailAPIView.as_view(),name='search' ),
    # path('<int:pk>/update',StatusUpdateAPIView.as_view(),name='search' ),
    # path('<int:pk>/delete',StatusDeleteAPIView.as_view(),name='search' ),
    # path('update/<int:pk>/', views.snippet_detail),
    # path('delete/<int:pk>/', views.snippet_detail),
    # path('u', views.snippet_detail),
]
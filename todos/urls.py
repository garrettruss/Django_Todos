from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('create/', views.CreateTodo.as_view(), name='create'),
    path('<int:pk>/update/', views.UpdateTodo.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteTodo.as_view(), name='delete'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls'))
]

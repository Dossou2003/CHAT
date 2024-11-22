
    from django.urls import path
    from . import views

    urlpatterns = [
        path('groups/', views.group_list, name='group_list'),
        path('chat/<str:room_name>/', views.chat_room, name='chat_room'),
    ]
  </boltAction
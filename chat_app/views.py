
    from django.shortcuts import render
    from django.contrib.auth.decorators import login_required
    from .models import Group, Message

    @login_required
    def group_list(request):
        groups = Group.objects.all()
        return render(request, 'chat_app/group_list.html', {'groups': groups})

    @login_required
    def chat_room(request, room_name):
        group = Group.objects.get(name=room_name)
        messages = Message.objects.filter(group=group)
        return render(request, 'chat_app/chat_room.html', {'group': group, 'messages': messages})
  </boltAction
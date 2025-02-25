from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from . models import chatGroup
from . forms import chatModelForm


@login_required
def chat_view(request):
    chat_group = get_object_or_404(chatGroup, group_name="Main_Group")
    chat_messages = chat_group.chat_messages.all()[:30]
    form = chatModelForm()

    if request.htmx:
        form = chatModelForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_group
            message.save()
            context = {
                'message' : message,
                'user' : request.user,
            }
            return render(request, 'a_rtchat/partials/chat_message_p.html', context)
    
    return render(request, 'a_rtchat/chat.html', { 'chat_messages' : chat_messages, 'form' : form })
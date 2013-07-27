# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from lbforum.models import Forum, Topic, Post
from django.contrib.auth.models import User


@csrf_exempt
def new_post(request, forum_id):
    ip = '127.0.0.1'
    subject = request.POST['subject']
    user_id = 2
    message = request.POST['message']
    response = HttpResponse('ok')
    forum = get_object_or_404(Forum, pk=forum_id)
    user = get_object_or_404(User, pk=user_id)
    topic = Topic(forum=forum, posted_by=user, subject=subject)
    topic.save()
    post = Post(topic=topic, posted_by=user, poster_ip=ip,
                message=message, topic_post=True)
    post.save()
    return response


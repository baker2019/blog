from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from house.models import CommentForm, Comment


def index(request):
    return HttpResponse("House Page")


@login_required(login_url='/login')
def addcomment(request, id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            current_user = request.user
            data = Comment()
            data.user_id = current_user.id
            data.house_id = id
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Your comment was sent successfully.")
            url = request.META.get('HTTP_REFERER')
            return HttpResponseRedirect(url)

    messages.warning(request, "Your comment was not saved. Please check.")
    return HttpResponse("Save operation did not occur.")


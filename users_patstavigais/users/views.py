from django.shortcuts import render

from .models import User
from .forms import CreateUserForm

users = []


def get_users(request):

    context = {
        'users': users,
    }

    return render(
        request,
        template_name='users.html',
        context=context,
    )


def add_user(request):

    form = CreateUserForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            user = User(
                username=form.cleaned_data['username'],
                e_mail=form.cleaned_data['e_mail'],
            )

            users.append(user)

            context = {
                'user': user,
            }

            return render(
                request,
                template_name='user.html',
                context=context,
            )

    context = {
        'form': form,
    }

    return render(
        request,
        template_name='add_user.html',
        context=context,
    )

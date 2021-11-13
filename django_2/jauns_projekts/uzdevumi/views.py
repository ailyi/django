from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random


# vienmēr funkcijas parametrs ir request
# skats = view
def show_hello(request):
    # pie return ir tas, ko mēs redzēsim
    # tekstu
    return HttpResponse('Hello!')


# skats
def show_html(request):
    # render = html dokumentu
    return render(
        request,
        template_name='hello.html'
    )


def show_datetime(request):
    return HttpResponse(datetime.today())


def motivate(request):
    motivations = (
        '1',
        '2',
        '3',
        '4',
    )

    motivation = random.choice(motivations)
    return HttpResponse(motivation)


# Izveidot Django aplikāciju.
#
# “/university” atbild ar  formu, kas prasa lietotājam ievadīt savu vārdu un vērtējumu matemātikas, latviešu valodas un svešvalodas  vidusskolas eksāmenos (0–100).

# Kad forma tiek iesniegta, tiek parādīts, vai cilvēks var stāties universitātē. Cilvēks var stāties universitāte, ja visos eksāmenos ir ne mazāk kā 40 balles.

def university(request):
    return render(
        request,
        template_name='university.html'
    )


def university_check(request):
    fname = request.POST.get('fname')
    math = request.POST.get('math')
    LV = request.POST.get('LV')
    FL = request.POST.get('FL')
    allowed = [math, LV, FL]
    for subject in allowed:
        if int(subject) < 40:
            return HttpResponse(fname + ' can not apply to university')
    return HttpResponse(fname + ' can apply to university')


# Izveidot Django aplikāciju. “/add_user” atvēr formu, kurā ir jāievada lietotājvārds un e-pasts. Nospiežot “Submit” tiek veidots User klases objekts, kura instances atribūti ir username un email. Lietotājs redz uzrakstu ievadīto lietotajvādu un e-pastu.

def add_user(request):
    return render(
        request,
        template_name='add_user.html'
    )


psc = []


def add_user_check(request):
    fname = request.POST.get('fname')
    mail = request.POST.get('mail')
    psc.append(User(fname, mail))
    return render(
        request,
        template_name='testuser.html',
        context={'test': fname, 'test2': mail}
    )


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


def users(request):
    return render(
        request,
        template_name='users.html',
        context={'users': psc}
    )

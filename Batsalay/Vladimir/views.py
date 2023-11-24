from django.http import HttpResponse

def index(request, name, surname, age, hobby):
    first = f'<h1> Меня зовут - {name}, Моя фамилия - {surname}. </h1>'\
            f'<h2>Мне {age} лет </h2>'\
            f'<h2>Я увлекаюсь {hobby}</h2>'
    return HttpResponse(first)

def about(request, place, grades, like):
    about = f'<h1> Я из {place}.</h1>' \
            f'<h2> Мой средний балл {grades}.</h2>' \
            f'<h2> Я люблю {like} </h2>'
    return HttpResponse(about)

def contacts(request, tel):
    contacts = f'<h2> Мой телеграм - {tel}</h2>'
    return HttpResponse(contacts)
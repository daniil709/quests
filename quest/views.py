from django.http import HttpResponse
from .models import Employee, Quest, Event
from django.shortcuts import render

CATALOG_LIST = {
    'Шепот старого маяка': {
        'cost': 1000,
        'description': 'В маяке зажигается призрачный свет ночью. Разгадайте шифр и успокойте дух до рассвета.',
        'image': 'img/1q.png',
        'time': ['11:00', '13:00', '15:00', '17:00', '19:00'],
        'duration': '2,5h',
        'employees': []
    },
    'Сбой в Матрице Сада': {
        'cost': 1200,
        'description': 'Кибер-сад взбесился и атакует всех. Найдите чужой код и перепрограммируйте ИИ до краха.',
        'image': 'img/2q.png',
        'time': ['11:00', '13:00', '15:00', '17:00', '19:00'],
        'duration': '2,5h',
        'employees': []
    },
    'Дело о молчащем оркестре': {
        'cost': 1250,
        'description': 'Оркестр исчез, инструменты в инее. Найдите музыкантов по странной ноте до бала.',
        'image': 'img/3q.png',
        'time': ['11:00', '13:00', '15:00', '17:00', '19:00'],
        'duration': '2,5h',
        'employees': []
    },
    'Пепел Вавилона': {
        'cost': 1560,
        'description': 'Врата в забытый город запечатаны кровью. Соберите пять артефактов и назовите имя царя.',
        'image': 'img/4q.png',
        'time': ['11:00', '13:00', '15:00', '17:00', '19:00'],
        'duration': '2,5h',
        'employees': []
    },
    'Экзамен для бессмертных': {
        'cost': 1900,
        'description': 'Студенты заперты в лабиринте со временем. Растопите стены логикой, иначе память пропадёт.',
        'image': 'img/5q.png',
        'time': ['11:00', '13:00', '15:00', '17:00', '19:00'],
        'duration': '2,5h',
        'employees': []
    },
    'Груз № 731': {
        'cost': 1150,
        'description': 'Корабль дрейфует в космосе с мёртвым экипажем. Выясните природу груза и заглушите сигнал.',
        'image': 'img/6q.png',
        'time': ['11:00', '13:00', '15:00', '17:00', '19:00'],
        'duration': '2,5h',
        'employees': []
    }
}

def home(request):
    return render(request, 'quest/index.html')

def catalog(request):
    context = {
        'catalog_list': Quest.objects.all(),

    }

    return render(request, 'quest/quest_list.html', context)

def event_list(request):
    events = Event.objects.all()
    context = {'event_list': events}

    return render(request, 'quest/homework.html', context)

def quest_detail(request, pk):
    quest = Quest.objects.get(id=pk)
    context = {'quest': quest}
    return render(request, 'quest/quest_detail.html', context)

def books(request):
    return HttpResponse("Hello, world. You're at the books page.")


def employee_info(request):
    return HttpResponse("Здесь будет полезная информация о сотрудниках")


def employee_detail(request, employee_id):
    employee = Employee.objects.get(id=employee_id)

    return render(request, 'quest/employee_detail.html', {'employee': employee})

from django.http import HttpResponse
from .models import Employee, Quest, Event
from django.shortcuts import render


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
    context = {'quest': quest,
               'times': quest.TIMES, # в шаблон передается список со временем
               }
    return render(request, 'quest/quest_detail.html', context)


def books(request):
    return HttpResponse("Hello, world. You're at the books page.")


def employee_info(request):
    return HttpResponse("Здесь будет полезная информация о сотрудниках")


def employee_detail(request, employee_id):
    employee = Employee.objects.get(id=employee_id)

    return render(request, 'quest/employee_detail.html', {'employee': employee})

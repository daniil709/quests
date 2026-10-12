from django.db.models import Q
from django.http import HttpResponse
from .models import Employee, Quest, Event, Book
from django.shortcuts import render


def home(request):
    return render(request, 'quest/index.html')


def catalog(request):
    quest_query = request.GET.get('quest_name', '').strip()

    if quest_query:
        quests = Quest.objects.filter(
            Q(title__icontains=quest_query) |
            Q(description__icontains=quest_query)
        )
    else:
        quests = Quest.objects.all()

    context = {
        'catalog_list': Quest.objects.all(),
        'quests': quests,
        'quest_query': quest_query,
    }

    return render(request, 'quest/quest_list.html', context)


def event_list(request):
    events = Event.objects.all()
    context = {'event_list': events}

    return render(request, 'quest/homework.html', context)


def quest_detail(request, pk):
    quest = Quest.objects.get(id=pk)
    context = {'quest': quest,
               'times': quest.TIMES,  # в шаблон передается список со временем
               }
    return render(request, 'quest/quest_detail.html', context)


def get_books(request):
    book_title_or_author = request.GET.get('book_title', '').strip()
    max_price = request.GET.get('max_price', '').strip()

    books = Book.objects.all()

    if book_title_or_author:
        books = books.filter(
            Q(title__icontains=book_title_or_author) |
            Q(author__icontains=book_title_or_author)
        )

    if max_price:
        try:
            books = books.filter(price__lte=float(max_price))
        except ValueError:
            pass  # если ввели не число — игнорируем фильтр

    context = {
        'books': books,
        'book_query': book_title_or_author,
        'max_price': max_price,
    }
    return render(request, 'quest/booksearch.html', context)


def employee_info(request):
    return HttpResponse("Здесь будет полезная информация о сотрудниках")


def employee_detail(request, employee_id):
    employee = Employee.objects.get(id=employee_id)

    return render(request, 'quest/employee_detail.html', {'employee': employee})

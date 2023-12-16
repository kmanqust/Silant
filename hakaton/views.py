from django.shortcuts import render
from .models import TO_output, Machine
from .forms import MachineFilterForm


def search_view(request):
    form = MachineFilterForm(request.GET)
    data = Machine.objects.all()
    if form.is_valid():
        filters = {key: value for key, value in form.cleaned_data.items() if value is not None}
        if filters:
            data = data.filter(**filters)

    search_term = request.GET.get('search_term', '')
    if search_term:
        data = Machine.objects.filter(
            Zav_number_machine__exact=search_term,
        )
        result_message = f'Результаты поиска для: {search_term}'
    else:
        data = Machine.objects.all()
        result_message = 'Вся таблица'
    return render(request, 'gg.html', {'data': data, 'search_term': search_term, 'result_message': result_message, 'form': form})

def search_view_v0(request):
    search_term = request.GET.get('search_term', '')
    if search_term:
        data = Machine.objects.filter(
            Zav_number_machine__exact=search_term,
        )
        result_message = f'Результаты поиска для: {search_term}'
    else:
        data = Machine.objects.all()
        result_message = 'Вся таблица'
    return render(request, 'gg.html', {'data': data, 'search_term': search_term, 'result_message': result_message})

def gg(request):
    data = Machine.objects.all()

    return render(request, 'gg.html', {'data': data})


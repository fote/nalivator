from django.shortcuts import render
from django.http import HttpResponseServerError
from .models import CurrentPumpSet, Beverage, Cocktail, CurrentCoctailSet
from django.shortcuts import get_object_or_404, get_list_or_404, redirect, HttpResponse
from .forms import PumpForm

# Create your views here.

def home(request):
    if CurrentPumpSet.objects.get(active=True):
        return redirect('/nalivator')
    else:
        return redirect('/choose_pumps')

def in_progress(request):
    context = {}
    cocktail_in_progress = Cocktail.objects.get(name=request.POST.get('cocktail'))
    print(cocktail_in_progress)
    return render(request, "in_progress.html", context)

def nalivator(request):
    context = {}
    cocktails = get_list_or_404(CurrentCoctailSet)
    context = { 'cocktails': cocktails }
    return render(request, "nalivator.html", context)


def choose_pumps(request):
    # current_pump_set = get_object_or_404(CurrentPumpSet.objects.filter(active=True))
    # pumps = (str(current_pump_set).split('.'))
    pump_form = PumpForm()
    # берем список всех напитков
    bevereges = get_list_or_404(Beverage)

    # передаем в качестве контекста в темплейт и там рисуем их в dropdown-менюшке
    context = { 'bevereges': bevereges, 'pump_form': pump_form }
    return render(request, "pump_set.html", context)


def choose_cocktails(request):
    # если пришли с ПОСТом с предыдущего шага
    if request.method == 'POST':
        # вытаскиваем из ПОСТа значения каждого насоса
        pumps = [ request.POST.get('pump1'), request.POST.get('pump2'), request.POST.get('pump3') ]
        # создаем модельный объект с напитками и сохраняем в базу
        CurrentPumpSet.objects.all().delete()
        CurrentPumpSet(active=True, pump1=Beverage.objects.get(name=pumps[0]), pump2=Beverage.objects.get(name=pumps[1]), pump3=Beverage.objects.get(name=pumps[2])).save()
        # хз что это
        for p in pumps:
            beverage_on_pump = get_object_or_404(Beverage, name=p)

        possible_cocktails = []
        # берем все коктейли из базы
        cocktails = Cocktail.objects.all()
        # выбираем те, которые могут быть налиты при выбранных напитках
        for c in cocktails:
            if (c.ing1 is None or str(c.ing1) in pumps) and (c.ing2 is None or str(c.ing2) in pumps) and (c.ing3 is None or str(c.ing3) in pumps):
                possible_cocktails.append(c)

        context = {'pumps': pumps, 'all_cocktails': cocktails, 'cocktails': possible_cocktails}

        return render(request, 'choose_cocktails.html', context)
    else:
        return redirect('/')


def final_step(request):
    if request.method == 'POST':
        # очищаем предыдущие настройки коктейлей
        CurrentCoctailSet.objects.all().delete()
        current_cocktails = []
        # дергаем из базы объект типа Cocktail
        for key in request.POST.keys():
            if request.POST[key] == 'on':
                current_cocktails.append(Cocktail.objects.get(name=key))

        # сохраняем выбранные коктейли в базу
        for c in current_cocktails:
            CurrentCoctailSet(cocktail_in_set=c).save()
        pumps = get_object_or_404(CurrentPumpSet, active=True)

        context = {'pump1': pumps.pump1, 'pump2': pumps.pump2, 'pump3': pumps.pump3, 'cocktails_set': current_cocktails }

        return render(request, 'final_step.html', context)


    else:
        return redirect('/')


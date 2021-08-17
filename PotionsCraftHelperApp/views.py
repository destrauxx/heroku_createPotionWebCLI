from django.shortcuts import render
from django.http import Http404
from .forms import CreatePotionModelForm
from .models import Potion
# Create your views here.

def index(request, *args, **kwargs):
    return render(request, 'index.html')

def create_potion_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = CreatePotionModelForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return render(request, 'forms.html', {'form': form, 'obj': obj})
    form = CreatePotionModelForm(request.POST or None)
    return render(request, 'forms.html', {'form': form})

def potions_view(request, *args, **kwargs):
    list_of_potions = Potion.objects.all()
    context = {'potions_list': list_of_potions}
    return render(request, 'potions.html', context)

def craft_potion_view(request, pk):
    try:
        potion = Potion.objects.get(id=pk)
        potion.ingredients = potion.ingredients.split(sep=', ')
    except Potion.DoesNotExist():
        raise Http404
    return render(request, 'craft.html', {'potion': potion})
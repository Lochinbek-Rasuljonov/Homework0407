from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Food
from .forms import FoodForm, MessageForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import permission_required, login_required
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q



def home(request):
    foods = Food.objects.all()
    return render(request, 'home.html', {'foods': foods})

def all_foods(request):
    foods = Food.objects.all()
    return render(request, 'all_food.html', {'foods': foods})

def food_detail(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    return render(request, 'food_detail.html', {'food': food})

def category_foods(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    foods = Food.objects.filter(category=category)
    return render(request, 'category_foods.html', {'category': category, 'foods': foods})

@login_required
@permission_required('app.add_food', raise_exception=True)
def add_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_foods')
    else:
        form = FoodForm()
    return render(request, 'add_food.html', {'form': form})

@login_required
@permission_required('app.change_food', raise_exception=True)
def edit_food(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES, instance=food)
        if form.is_valid():
            form.save()
            return redirect('food_detail', food_id=food.id)
    else:
        form = FoodForm(instance=food)
    return render(request, 'edit_food.html', {'form': form, 'food': food})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['lochinbekrasuljonovdev@gmail.com'],
            )
            return render(request, 'message_sent.html')
    else:
        form = MessageForm()

    return render(request, 'send_message.html', {'form': form})


def search_foods(request):
    query = request.GET.get('q')
    foods = Food.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)) if query else []
    return render(request, 'search_results.html', {'foods': foods, 'query': query})
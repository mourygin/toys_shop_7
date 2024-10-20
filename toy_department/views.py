from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DjangoRegForm, LoginForm
from .models import Toy, Buyer, Basket
import hashlib

current_user = 0
current_user_name = ''
# Create your views here.
def main_page(request):
    global current_user, current_user_name
    pn = 'Добро пожаловать в наш игрушечный магазин игрушек!'
    context = {'pn': pn, 'current_user':current_user}
    return render(request, 'main_page.html', context)
def shop_page(request):
    global current_user, current_user_name
    pn = 'Выбери игрушку по своему вкусу!'
    Toys = Toy.objects.all()
    context = {'pn':pn, 'Toys':Toys, 'current_user':current_user, 'current_user_name':current_user_name}
    return render(request, 'toy_selection.html', context)
def basket_page(request):
    global current_user, current_user_name
    pn ='Корзина'
    toys = Basket.objects.filter(buyer_id=current_user)
    all_toys = Toy.objects.all()
    context = {'pn': pn, 'current_user':current_user, 'current_user_name':current_user_name, 'toys':toys, 'all_toys':all_toys}
    return render(request,'basket.html',context)
def logout_page(request):
    global current_user, current_user_name
    current_user = 0
    current_user_name = ''
    pn = 'Добро пожаловать в наш игрушечный магазин игрушек!'
    context = {'pn': pn, 'current_user': current_user}
    return render(request, 'main_page.html', context)
def login_page(request):
    global current_user, current_user_name
    pn ='Мы рады Вас видеть!'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            pwd_enc = password.encode()
            pwd_hash = hashlib.md5(pwd_enc)
            buyers = Buyer.objects.all()
            user_presents = False
            for buyer in buyers:
                if buyer.name == username:
                    user_presents = True
                    if buyer.psw == pwd_hash.hexdigest():
                        current_user = buyer.id
                        current_user_name = buyer.name
                        pn = 'Выбери игрушку по своему вкусу!'
                        Toys = Toy.objects.all()
                        context = {'pn': pn, 'Toys': Toys, 'current_user': current_user, 'current_user_name':current_user_name}
                        return render(request, 'toy_selection.html', context)
                    else:
                        response = 'Ошибка логина или пароля!'
                        return HttpResponse(response)
                    break
            if not user_presents:
                response = 'Данный пользователь не зарегистрирован.'
                return HttpResponse(response)
    else:
        form = LoginForm()
    context = {'pn': pn, 'form':form, 'current_user':current_user}
    return render(request, 'login_page.html', context)

def show_ignatiy(request):
    global current_user
    return render(request, 'show_ignatiy.html',{'current_user':current_user})
def show_teddy_bear(request):
    global current_user
    return render(request, 'show_teddy_bear.html',{'current_user':current_user})
def show_cat(request):
    global current_user
    return render(request, 'show_cat.html',{'current_user':current_user})
def show_pafnutiy(request):
    global current_user
    return render(request, 'show_pafnutiy.html',{'current_user':current_user})
def show_piglet_1(request):
    global current_user
    return render(request, 'show_piglet_1.html', {'current_user': current_user})

def registration(request):
    global current_user, current_user_name
    pn = 'Use this form for registration.'
    if request.method == 'POST':
        form = DjangoRegForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            password = form.cleaned_data['password']
            re_password = form.cleaned_data['re_password']
            result = False
            if int(age) < 18:
                response = 'Вы слишком молоды для этого сайта!'
            elif password != re_password:
                response = 'Не совпадают введенные пароли!'
            else:
                result = True
            if result:
                buyers = Buyer.objects.all()
                for buyer in buyers:
                    if buyer.name == username:
                        response = 'Пользователь с этим именем уже зареристрирован!'
                        return HttpResponse(response)
                pwd_enc = password.encode()
                pwd_hash = hashlib.md5(pwd_enc)
                Buyer.objects.create(name=username,balance=100,age=age,psw=pwd_hash.hexdigest())
                new_buyer = Buyer.objects.get(name=username)
                current_user = new_buyer.id
                current_user_name = new_buyer.name
                return redirect('http://127.0.0.1:8000/toys/')
            else:
                return HttpResponse(response)

    else:
        form = DjangoRegForm()
    contest = {'pn': pn, 'form':form, 'current_user':current_user}
    return render(request, 'django_reg.html', contest)

def buying(request):
    global current_user
    toy_id = request.GET.get('toy', 0)
    print('!!!!!!!!!!!', current_user,toy_id)
    if Buyer.objects.get(id=current_user).age > 18 or Toy.objects.get(id=toy_id).age_limited == False:
        Basket.objects.create(buyer_id = current_user, toy_id = toy_id)
    pn = 'Выбери игрушку по своему вкусу!'
    Toys = Toy.objects.all()
    context = {'pn': pn, 'Toys': Toys, 'current_user': current_user, 'current_user_name': current_user_name}
    return render(request, 'toy_selection.html', context)

def buy_toy(request):
    if request.method == 'POST':
        toy_id = request.POST.get('toy_id')
        if toy_id:
            # Логика обработки покупки игрушки
            if Buyer.objects.get(id=current_user).age > 18 or Toy.objects.get(id=toy_id).age_limited == False:
                Basket.objects.create(buyer_id=current_user, toy_id=toy_id, toy_name=Toy.objects.get(id=toy_id).title, toy_descr=Toy.objects.get(id=toy_id).description)
            pn = 'Выбери игрушку по своему вкусу!'
            Toys = Toy.objects.all()
            context = {'pn': pn, 'Toys': Toys, 'current_user': current_user, 'current_user_name': current_user_name}
            return render(request, 'toy_selection.html', context)
    else:
        return HttpResponse('!!! No toy_id !!!')
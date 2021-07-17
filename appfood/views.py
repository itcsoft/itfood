from django.shortcuts import render, redirect
from django.contrib import messages

from .models import FoodCategory, Food

def home(request):
    # Из базы получаем все категории еды
    foodCategories = FoodCategory.objects.all()
    foods = Food.objects.all()

    # Показываем шаблон home.html и передаем ему foodCategories
    return render(request, 'home.html', {
        'foodCategories': foodCategories,
        'foods': foods
    })


# показывает список блюд по категорию
def get_foods_by_category(request, category_id):
    # мы получаем весь список блюд по категорию
    foods = Food.objects.all().filter(food_category_id = category_id)
    
    # получаем категорию еды по id
    category = FoodCategory.objects.get(id=category_id)
    
    # Из базы получаем все категории еды
    foodCategories = FoodCategory.objects.all()

    return render(request,
        'foods_by_category.html',
        {
            'foods': foods,
            'category': category,
            'foodCategories': foodCategories
        }
    )


def food_detail_view(request, food_id):
    # получаем еду по id
    food = Food.objects.get(id = food_id)

    # Из базы получаем все категории еды (нужен для header)
    foodCategories = FoodCategory.objects.all()

    # Рендерим на шаблон food_detail.html
    return render(request,
        'food_detail.html',
        {
            'food': food,
            'foodCategories': foodCategories
        }
    )


# функция обрабатывает на добавление корзину
def add_to_card(request, food_id):
    cards = request.session.get('food_cards', [])
    # временно сохраняем товар в сессию пользователя
    cards.append(food_id)
    request.session['food_cards'] = cards

    # перенаправляем пользователя обратно на свою страницу 
    # после добавление еды на корзину

    prev = request.GET.get('prev')
    return redirect(prev)


# функция обрабатывает блюдо уменьшение в корзине
def del_to_card(request, food_id):
    cards = request.session.get('food_cards', [])
    # временно сохраняем товар в сессию пользователя
    cards.remove(food_id)
    request.session['food_cards'] = cards

    # перенаправляем пользователя обратно на свою страницу 
    # после уменьшение блюдо на корзину
    prev = request.GET.get('prev')
    return redirect(prev)


# удаляем блюдо из корзины вообще
def remove_to_card(request, food_id):
    cards = request.session.get('food_cards', [])
    # временно сохраняем товар в сессию пользователя
    # удаляем из корзины блюдо
    new_cards = []
    for card in cards:
        if card != food_id:
            new_cards.append(card)

    request.session['food_cards'] = new_cards
    # перенаправляем пользователя обратно на свою страницу 
    # после очищение блюдо из корзины
    prev = request.GET.get('prev')
    return redirect(prev)


# обработчик показа блюд в корзине
def card_view(request):
    # Из базы получаем все категории еды (нужен для header)
    foodCategories = FoodCategory.objects.all()

    # id блюд которые находятся в корзине
    foods_ids = request.session.get('food_cards', [])
    
    # получаем все блюда и базы по списку food_ids
    card_foods = Food.objects.filter(id__in = foods_ids)
    for card_food in card_foods:
        card_food.count = foods_ids.count(card_food.id)
        card_food.sum = card_food.count * card_food.sale_price

    return render(request,
        'card_view.html',
        {
            'foods_ids': foods_ids,
            'card_foods': card_foods,
            'foodCategories': foodCategories
        }
    )


def order_add(request):
    if request.method == 'POST':
        # id блюд которые находятся в корзине
        foods_ids = request.session.get('food_cards', [])
        # проверяем не пустая ли наша корзина
        if len(foods_ids) == 0:
            # Если наша корзина пустая отправляем сообщение клиенту об ошибке: Ваша корзина пустая
            messages.error(request, 'Ваша корзина пустая', extra_tags='danger')
            prev = request.POST.get('prev_url')
            return redirect(prev)
        else:
            # принимаем данные клиента для добавление в базу
            client_name = request.POST.get('client_name')
            client_phone = request.POST.get('client_phone')
            client_address = request.POST.get('client_address')
        
        




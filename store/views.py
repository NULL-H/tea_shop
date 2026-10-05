from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    html = """
    <h1>Интернет-магазин китайского чая — Главная</h1>
    <p>Добро пожаловать в чайный магазин! Здесь представлены лучшие сорта чая из Китая (Пуэр, Да Хун Пао, Те Гуаньинь).</p>
    <ul>
        <li><a href="/catalog/">Перейти в каталог чая</a></li>
        <li><a href="/cart/">Моя корзина</a></li>
        <li><a href="/orders/">Мои заказы</a></li>
    </ul>
    """
    return HttpResponse(html)

def catalog_view(request):
    html = """
    <h1>Каталог чая и чайной посуды</h1>
    <p>Список доступных категорий: Пуэр, Улун, Зеленый чай, Белый чай, Чайная посуда.</p>
    <ul>
        <li><a href="/product/1/">Товар №1: Да Хун Пао (Улун, Уишань)</a></li>
        <li><a href="/product/2/">Товар №2: Шэн Пуэр 2018 (Юньнань)</a></li>
    </ul>
    <p><a href="/">← На главную</a></p>
    """
    return HttpResponse(html)

def product_detail_view(request, product_id):
    html = f"""
    <h1>Карточка товара #{product_id}</h1>
    <p><b>Категория:</b> Китайский чай | <b>Регион:</b> Юньнань / Уишань</p>
    <p><b>Описание:</b> Натуральный чай ручного сбора, фасовка 100г, яркий аромат и долгое послевкусие.</p>
    <p><b>Цена:</b> 1200 руб. | <b>В наличии:</b> 25 шт.</p>
    <button>Добавить в корзину</button>
    <p><a href="/catalog/">← Вернуться в каталог</a></p>
    """
    return HttpResponse(html)

def cart_view(request):
    html = """
    <h1>Корзина покупок</h1>
    <p>Список выбранных товаров и расчет предварительной стоимости.</p>
    <ul>
        <li>Да Хун Пао (100г) — 1 шт. — 1200 руб.</li>
    </ul>
    <p><b>Итого к оплате:</b> 1200 руб.</p>
    <p><a href="/checkout/"><b>Перейти к оформлению заказа →</b></a></p>
    <p><a href="/catalog/">← Продолжить покупки</a></p>
    """
    return HttpResponse(html)

def checkout_view(request):
    html = """
    <h1>Оформление заказа</h1>
    <p>Заполните данные для доставки:</p>
    <form>
        <p>Имя получателя: <input type="text" placeholder="Иван Иванов" /></p>
        <p>Телефон: <input type="text" placeholder="+7 (999) 000-00-00" /></p>
        <p>Адрес доставки: <input type="text" placeholder="г. Владимир, ул. Горького, д. 87" /></p>
        <p>Способ получения: 
            <select>
                <option>Курьерская доставка</option>
                <option>СДЭК / ПВЗ</option>
                <option>Самовывоз</option>
            </select>
        </p>
        <button type="button">Подтвердить заказ</button>
    </form>
    <p><a href="/cart/">← Назад в корзину</a></p>
    """
    return HttpResponse(html)

def orders_view(request):
    html = """
    <h1>Личный кабинет: История заказов</h1>
    <table border="1" cellpadding="5">
        <tr>
            <th>№ Заказа</th>
            <th>Дата</th>
            <th>Состав</th>
            <th>Сумма</th>
            <th>Статус</th>
        </tr>
        <tr>
            <td>#1001</td>
            <td>2026-10-05</td>
            <td>Да Хун Пао (100г) x1</td>
            <td>1200 руб.</td>
            <td><b>Оплачен / В обработке</b></td>
        </tr>
    </table>
    <p><a href="/">← На главную</a></p>
    """
    return HttpResponse(html)
Задание по теме "Сайт администрирования":
=========================================
Заполнение таблиц:
(Выполнение запросов производилось при помощи приложения "DB Browser")

INSERT INTO toy_department_basket (buyer_id, toy_id, toy_name,toy_descr)  VALUES (2, 1, 'Кукла Игнат','Забавная кукла');
INSERT INTO toy_department_basket (buyer_id, toy_id, toy_name,toy_descr)  VALUES (2, 3, (SELECT title FROM toy_department_toy WHERE id=3),(SELECT description FROM toy_department_toy WHERE id=3));

Создание объектов и изменение их значений средствами DJANGO:

>>> from toy_department.models import Buyer, Toy, Basket
>>> Toy.objects.create(title='Поросенок-1', articul='754121001', cost=1500, weight=310, description='Он поросенок и зовут его Ниф-ниф.', age_limited=False, in_stock=4, picture_min='piglet-1.png', picture_max='piglet-1.gif')
>>> a=Toy.objects.get(title='Поросенок-1')
>>> a.picture_min='/static/piglet-1.png'
>>> a.picture_max='http://127.0.0.1:8000/piglet_1/'
>>> a.save()

Получение всех объектов и удаление:

>>> from toy_department.models import Buyer, Toy, Basket
>>> a=Toy.objects.all()
>>> a
<QuerySet [<Toy: Кукла Игнат>, <Toy: Медвежонок Тэдди>, <Toy: Наглый кот>, <Toy: Заяц Пафнутий>, <Toy: Поросенок-1>]>
>>> a=Toy.objects.get(title='Поросенок-1')
>>> a.delete()
(1, {'toy_department.Toy': 1})
>>> a=Toy.objects.all()
>>> a
<QuerySet [<Toy: Кукла Игнат>, <Toy: Медвежонок Тэдди>, <Toy: Наглый кот>, <Toy: Заяц Пафнутий>]>
>>>

Фильтрация объектов:

>>> a=Basket.objects.all()
>>> a
<QuerySet [<Basket: Basket object (23)>, <Basket: Basket object (24)>, <Basket: Basket object (25)>, <Basket: Basket object (26)>, <Basket: Basket object (27)>, <Basket: Basket object (28)>, <Basket: Basket object (29)>, <Basket: Basket object (30)>, <Basket: Basket object (31)>, <Basket: Basket object (32)>]>
>>> b=a.filter(buyer_id=14)
>>> b
<QuerySet [<Basket: Basket object (23)>, <Basket: Basket object (24)>, <Basket: Basket object (25)>]>

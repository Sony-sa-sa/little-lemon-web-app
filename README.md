# Little Lemon — Django сайт

## Запуск проекта

1. Создайте виртуальное окружение и активируйте его:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Примените миграции (они уже включены в проект, менять модель не нужно):
   ```bash
   cd littlelemon
   python manage.py migrate
   ```

4. Создайте суперпользователя, чтобы зайти в Django Admin:
   ```bash
   python manage.py createsuperuser
   ```

5. Запустите сервер разработки:
   ```bash
   python manage.py runserver
   ```

6. Откройте сайт: http://127.0.0.1:8000/
   Админка: http://127.0.0.1:8000/admin/ — там добавляйте блюда (MenuItem).

## Структура

```
littlelemon/
├── manage.py
├── requirements.txt
├── littlelemon/          # настройки проекта
│   ├── settings.py       # + MEDIA_URL, MEDIA_ROOT для картинок
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── menu/                 # приложение
    ├── models.py          # модель MenuItem (name, price, description, image)
    ├── admin.py           # регистрация модели в админке
    ├── views.py            # home, about, menu, menu_item, book
    ├── urls.py
    ├── migrations/         # готовая миграция 0001_initial
    └── templates/
        ├── base.html       # навигация + футер (на всех страницах)
        ├── home.html
        ├── about.html
        ├── menu.html        # список блюд, сортировка по алфавиту
        ├── menu_item.html   # детали блюда: название, цена, описание, картинка
        └── book.html        # заглушка бронирования
```

## Как проверяется функциональность задания

1. Главная (`/`) содержит ссылку на Menu — есть в шапке `base.html` и на самой странице.
2. `/menu/` показывает все блюда из БД (`MenuItem.objects.all()`).
3. Сортировка по алфавиту задана и на уровне модели (`Meta.ordering = ['name']`),
   и явно во view (`order_by('name')`).
4. У каждого блюда в списке видна цена (`{{ item.price }}`).
5. Клик по названию блюда ведёт на `/menu_item/<id>/`.
6. Страница блюда показывает название, цену, описание и картинку.
7. Футер выведен в `base.html` и наследуется всеми страницами.

Изображения для блюд добавляются только через Django Admin (поле `image`
в форме модели), они сохраняются в `media/menu_images/` и раздаются
благодаря `MEDIA_URL`/`MEDIA_ROOT` в `settings.py`.

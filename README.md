# Обрезание ссылок и подсчёт кликов по битлинку

## Описание
Обрезка ссылок с помощью Битли.
При введении обычной ссылки в консоль, выводит битлинк, а при введении битлинк считывает количество кликов по нему
## Как установить
### Зависимости
Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```python
pip install -r requirements.txt
```
### Переменные окружения
Создайте файл .env без расширения.
Вставьте этот код в файл, заменив текст на свой токен
```python
BITLY_TOKEN="Вставьте сюда свой токен"
```
#### Как получить токен
  Зайдите на сайт битли, после чего создайте аккаунт.
  на сайте https://app.bitly.com/settings/api создайте апи токен
## Запуск
откройте консоль, введите команду cd "Вставьте сюда путь до проекта".
Введите в консоль python main.py "Ваша ссылка или битлинк"
## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
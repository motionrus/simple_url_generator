# Simple URL Generator

Простой генератор, для создания коротких ссылок 

### Установка

```python
pip install -r requirements.txt
```

### Функционал
Endpoint ```link/``` умеет создавать и удалять записи коротких ссылок
На создание нужно отправить ```POST``` с ```long_link``` ссылкой. API вернет
```json
{
    "id": 9,
    "long_link": "http://habrahabr.ru",
    "short_link": "http://localhost:8000/L2zxH0WkpT"
}
``` 
Удаление через ```DELETE``` по объекту ```link/9/```

Ссылка ```short_link``` вернет 301 с переходом на сайт.

### TODO

1. Добавить время жизни ссылки
2. Вести счетчик переходов
3. Добавить редактирование ссылок

# Скрипт для создания карты сайта

### Описание
Скрипт проходит по всем ссылкам на сайте, и если они находятся на этом домене, то добавляет их в дерево в формате json

### Технологии

beautifulsoup4==4.11.1
bs4==0.0.1
certifi==2022.6.15
charset-normalizer==2.1.0
idna==3.3
lxml==4.9.1
requests==2.28.1
soupsieve==2.3.2.post1
urllib3==1.26.10

### Для запуска выполните в папке с работой (Windows):

    python -m venv venv
    source venv/Scripts/activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    
    python main.py

### В скрипт изначально внесены следующие url:

    http://google.com/
    http://crawler-test.com/
    https://vk.com
    https://yandex.ru
    https://stackoverflow.com

При необходимости проверить другой сайт, необходимо внести его в список в скрипте main.py

логи с информацией о работе скрипта находятся в папке с скриптом с названием map.log

# Автор: Паша Калинин
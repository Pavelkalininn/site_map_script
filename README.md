# Script for creating a site map

### Description
The script goes through all the links on the site, and if they are on this domain, it adds them to the tree in json format

### Technologies

beautifulsoup4==4.11.1
bs4==0.0.1
certifi==2022.6.15
charset-normalizer==2.1.0
idna==3.3
lxml==4.9.1
requests==2.28.1
soupsieve==2.3.2.post1
urllib3==1.26.10

### To start, run in the work folder (Windows):

    python -m venv venv
    source venv/Scripts/activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    
    python main.py

### The following urls were initially added to the script:
    http://google.com/
    http://crawler-test.com/
    https://vk.com
    https://yandex.ru
    https://stackoverflow.com

If you need to check another site, you need to add it to the list in the script main.py

logs with information about the script are located in a folder with a script called map.log

# Author: Pavel Kalinin

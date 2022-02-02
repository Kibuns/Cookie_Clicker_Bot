# Python Selenium Cookie Clicker Bot Project
In this project I am making a bot that plays the game [Cookie Clicker](https://orteil.dashnet.org/cookieclicker/) using Selenium. Which
is an open-source web-based automation tool. Selenium is primarily used for testing in the industry but It can also be used for web scraping.

This project was actually meant as a way to learn selenium, but may be expanded because so far it's really fun to work on. 

![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/77112006/152077422-5af87f36-c5fe-44e2-b87c-f2bbe4b47d2e.gif)

## Features
The bot it currently able to:
- Click the cookie (duh)
- It looks if it can buy buildings from bottom to top
- It buys an upgrade if it can.

## Use
This bot is only used on Chrome so be sure you change the ```PATH = "C:\Program Files (x86)\chromedriver.exe")``` where your chromedriver.exe is.

Selenium documentation : https://selenium-python.readthedocs.io/index.html

[This is the chrome driver you need to download to put in your C:\Program Files (x86)](https://sites.google.com/a/chromium.org/chromedriver/downloads)

install selenium with ```pipenv install selenium```

then just run cookieclicker.py, if it doesn't work, try ```python -m pipenv run python cookieclicker.py``` in the console



## Possible Features
- Click FASTER (it's kinda slow now, idk why)
- Not start from scratch everytime (maybe load a save on startup? or just use cookies(the virtual ones(the ones you can't eat))
- A more sophisticated algorithm that actually buys something based on its cost to cps(cookies per second) ratio and see if it's the best thing to buy
- Click Golden Cookies
- Ascend (and buy ascension upgrades and stuff)




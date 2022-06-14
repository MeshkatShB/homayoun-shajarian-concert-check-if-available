import sched
import time
import os
from bs4 import BeautifulSoup
from telegram import send_telegram_message

import requests as req

TIWALL_URL = 'https://www.tiwall.com/'
SALE_URL = 's/'
PRODUCT_URL = 'p/'
HOMAYOUN_URL = TIWALL_URL + SALE_URL + 'homayoun.shajarian'
INTERVALS = 3
PRIORITY = 1


def check_if_reserve_open(sc, response):
    """
    Checks if reserve option is available or not
    :param sc: scheduler to dispatch which is activated in each INTERVALS
    :param response: Response of request to the URL
    :return: None
    """

    soup = BeautifulSoup(response.content, 'html.parser')
    div = soup.find_all('select', attrs={'class': 'session', })

    if len(div[0]) != 23:
        print('GO GO GO!', )
        os.system('spd-say "You Can Get Your Concert Ticket Now"')
        send_telegram_message()
    else:
        print("just chill & flex bro. Not Now!!!")

    sc.enter(INTERVALS, PRIORITY, check_if_reserve_open, (sc, response))


def main(response):
    """
    Set Scheduler to Dispatch check_if_reserve_open function at  Intervals
    :param response: Response of request to the URL
    :return: None
    """
    s = sched.scheduler(time.time, time.sleep)
    s.enter(INTERVALS, PRIORITY, check_if_reserve_open, (s, response, ))
    s.run()


if __name__ == '__main__':
    resp = req.get(HOMAYOUN_URL, )
    main(resp)

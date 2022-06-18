import sched
import time
import os
import requests as req

from bs4 import BeautifulSoup
from telegram import send

TIWALL_URL = 'https://www.tiwall.com/'
SALE_URL = 's/'
PRODUCT_URL = 'p/'
HOMAYOUN_URL = TIWALL_URL + SALE_URL + 'homayoun.shajarian'
INTERVALS = 3
PRIORITY = 1

response = req.get(HOMAYOUN_URL, )


def check_if_reserve_open(sc):
    """
    Checks if reserve option is available or not
    :param sc: scheduler to dispatch which is activated in each INTERVALS
    :return: None
    """
    soup = BeautifulSoup(response.content, 'html.parser')
    div = soup.find_all('select', attrs={'class': 'session', })
    print(div, len(div))

    if div:
        print('GO GO GO!', )
        os.system('spd-say "You Can Get Your Concert Ticket Now"')
        send()
    else:
        print('You Should Wait Longer! ROFL!')
        pass

    sc.enter(INTERVALS, PRIORITY, check_if_reserve_open, (sc, ))


def main():
    """
    Set Scheduler to Dispatch check_if_reserve_open function at  Intervals
    :return: None
    """
    s = sched.scheduler(time.time, time.sleep)
    s.enter(INTERVALS, PRIORITY, check_if_reserve_open, (s, ))
    s.run()


if __name__ == '__main__':
    main()

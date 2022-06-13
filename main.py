import sched
import time
import os

import requests as req

is_reserve_time_open = False
URL = 'https://www.tiwall.com/s/homayoun.shajarian'
INTERVALS = 60
PRIORITY = 1


def main(response):
    """
    Set Scheduler to Dispatch check_if_reserve_open function at  Intervals
    :param response:
    :return:
    """
    s = sched.scheduler(time.time, time.sleep)
    s.enter(INTERVALS, PRIORITY, check_if_reserve_open, (s, response, ))
    s.run()


def check_if_reserve_open(sc, response):
    if 'reserve-config' in response.text:
        # is_reserve_time_open = True
        print('GO GO GO!', )
        os.system('spd-say "You Can Get Your Concert Ticket Now"')
    else:
        print("just chill & flex bro. Not Now!!!")

    # You can also check it with response.history in regard of response being redirected or not
    # if len(response.history) < 2:
    #     print(response.is_redirect)
    #     print("JESUS, MOVE IT! Go Reserve Bro!", response.history[0].url)
    #     os.system('spd-say "You Can Get Your Concert Ticket Now"')

    sc.enter(60, 1, check_if_reserve_open, (sc,))


if __name__ == '__main__':
    resp = req.get(URL, )
    main(resp)

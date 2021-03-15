import schedule
import time
from datetime import datetime

def myscheduler():
    print('\n')
    print('=' * 40)
    print('Heure actuelle :', datetime.now().strftime("%H:%M:%S"))
    print('=' * 40)
    print('\n')

# Configuration du Scheduler
schedule.every(5).seconds.do(myscheduler)
# schedule.every().minute.do(myscheduler)
# schedule.every().hour.do(myscheduler)
# schedule.every().day.at("10:30").do(myscheduler)
# schedule.every(5).to(10).minutes.do(myscheduler)
# schedule.every().monday.do(myscheduler)
# schedule.every().wednesday.at("13:15").do(myscheduler)
# schedule.every().minute.at(":17").do(myscheduler)


if __name__ == '__main__':

    while True:
        schedule.run_pending()
        time.sleep(1) # préférable



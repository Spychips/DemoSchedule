import schedule
import time
from datetime import datetime

def myscript():
    print('\n')
    print('=' * 40)
    print('Heure actuelle :', datetime.now().strftime("%H:%M:%S"))
    print('=' * 40)
    print('\n')

# Configuration du Scheduler
schedule.every(5).seconds.do(myscript)
# schedule.every().minute.do(myscript)
# schedule.every().hour.do(myscript)
# schedule.every().day.at("10:30").do(myscript)
# schedule.every(5).to(10).minutes.do(myscript)
# schedule.every().monday.do(myscript)
# schedule.every().wednesday.at("13:15").do(myscript)
# schedule.every().minute.at(":17").do(myscript)


if __name__ == '__main__':

    while True:
        schedule.run_pending()
        time.sleep(1) # préférable



import schedule
import time
import subprocess
from src.util import script_path

def myscheduler():
    print('\n')
    print('=' * 40)
    subprocess.call(script_path,shell=True)
    print('=' * 40)
    print('\n')


# CONFIGURATION DU SCHEDULER
schedule.every(5).seconds.do(myscheduler)
# schedule.every().minute.do(myscheduler)
# schedule.every().hour.do(myscheduler)
# schedule.every().day.at("10:30").do(myscheduler)
# schedule.every(5).to(10).minutes.do(myscheduler)
# schedule.every().monday.do(myscheduler)
# schedule.every().wednesday.at("13:15").do(myscheduler)
# schedule.every().minute.at(":17").do(myscheduler)


# LANCEMENT DU SCHEDULER
if __name__ == '__main__':

    while True:
        schedule.run_pending()
        time.sleep(1) # préférable



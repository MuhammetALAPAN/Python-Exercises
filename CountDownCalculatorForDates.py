from datetime import datetime
import time


def countdown(total_sec):
    """
    Running a CountDown for given seconds
    """
    while total_sec:
        minutes, seconds = divmod(total_sec, 60)
        print("{} minutes, {} seconds".format(minutes, seconds), end='\r')
        total_sec -= 1
        time.sleep(1)
    print("Ended!")


print("Please enter dates as (dd.mm.yyyy hh:mm:ss). Example Date: 08.05.1993 10:32:00")
t1 = input("First Date: ")
t2 = input("Second Date: ")
t1_datetime = datetime.strptime(t1, "%d.%m.%Y %H:%M:%S")
t2_datetime = datetime.strptime(t2, "%d.%m.%Y %H:%M:%S")
t3_datetime = t2_datetime - t1_datetime
countdown(int(t3_datetime.total_seconds()))

# testing inputs
# 23.06.1995 09:35:00
# 28.07.2021 16:02:30

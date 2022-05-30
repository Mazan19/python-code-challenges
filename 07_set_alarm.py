import sched
import time
from playsound import playsound

# My solution
def set_an_alarm_my_way(alarm_time, sound_file, message):
    # Problems: calc the time, not async execution (do not return environment til the end)
    wait = int(alarm_time - time.time())
    time.sleep(wait)
    print(message)
    playsound(sound_file)

# Solution by author
def set_an_alarm(alarm_time, sound_file, message):
    # Using scheduler, but the main problem is the same: it is not async
    s = sched.scheduler(time.time,time.sleep)
    s.enterabs(alarm_time, 1, print, argument=(message,))
    s.enterabs(alarm_time, 1, playsound, argument=(sound_file,))
    print("done")
    s.run()

set_an_alarm(time.time()+5, '/System/Library/Sounds/Funk.aiff', 'Alarming message')

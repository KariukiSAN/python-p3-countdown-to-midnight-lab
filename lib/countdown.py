# your code goes here!

import time

def countdown(seconds):
    while seconds > 0:

        print (f'{seconds} SECOND (S)!')
        seconds -=1
        if seconds == 0:
            print ('HAPPY NEW YEAR!')

    pass

countdown (5)

def countdown_with_sleep(seconds):
    while seconds > 0:
        print(f'{seconds} SECOND(S)!')
        seconds -=1
        time.sleep(1)
        if seconds == 0:
            print ('HAPPY NEW YEAR!')

countdown_with_sleep (3)












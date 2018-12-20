import winsound
from time import sleep, localtime


def beep():
    if m == 59:
        winsound.Beep(1000, 500)  # one long beep
    elif m == 5:
        winsound.Beep(1000, 200)  # two short beep
        winsound.Beep(1000, 200)  # two short beep
    elif m == 10:
        winsound.Beep(1000, 200)  # two short beep
        winsound.Beep(1000, 200)  # two short beep
    elif m == 15:
        winsound.Beep(1000, 200)  # two short beep
        winsound.Beep(1000, 200)  # two short beep
    elif m == 20:
        winsound.Beep(1000, 200)  # two short beep
        winsound.Beep(1000, 200)  # two short beep
    elif m == 25:
        winsound.Beep(1000, 200)  # two short beep
        winsound.Beep(1000, 200)  # two short beep
    elif m == 30:
        winsound.Beep(1000, 500)  # one long beep
    elif m == 35:
        winsound.Beep(1000, 200)  # two short beep
        winsound.Beep(1000, 200)  # two short beep
    elif m == 40:
        winsound.Beep(1000, 200)  # two short beep
        winsound.Beep(1000, 200)  # two short beep
    elif m == 45:
        winsound.Beep(1000, 200)  # two short beep
        winsound.Beep(1000, 200)  # two short beep
    elif m == 50:
        winsound.Beep(1000, 200)  # two short beep
        winsound.Beep(1000, 200)  # two short beep
    elif m == 55:
        winsound.Beep(1000, 200)  # two short beep
        winsound.Beep(1000, 200)  # two short beep        
if __name__ == "__main__":
    while True:
        now = localtime()
        m = now.tm_min
        s = now.tm_sec
        sleep(60 - s)  # refresh every minute.
        beep()
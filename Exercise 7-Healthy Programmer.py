#EXERCISE 7
#Healthy Programmer
from time import time
from datetime import datetime
from pygame import mixer

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user=input()
        if input_of_user==stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__=='__main__':
    init_water=time()
    init_eyes=time()
    init_exercise=time()
    watersecs=5
    exsecs=10
    eyessecs=20

    while True:
        if time()-init_water>watersecs:
            print("Water drinking time.Enter 'drank' to stop the alarm")
            musiconloop('water.wav','drank')
            init_water=time()
            log_now("Drank water at")

        if time()-init_eyes>eyessecs:
            print("Eye exercise time.Enter 'eyesdone' to stop the alarm")
            musiconloop('eyes.wav','eyesdone')
            init_eyes=time()
            log_now("Did eye exercise at")

        if time()-init_exercise>exsecs:
            print("Physical exercise time.Enter 'phydone' to stop the alarm")
            musiconloop('physical.wav','phydone')
            init_exercise=time()
            log_now("Did physical exercise at")



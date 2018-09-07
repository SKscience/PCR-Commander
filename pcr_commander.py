from gtts import gTTS
import time
from pygame import mixer
mixer.init()

experiment_name = input("Name of experiment:  ")
t_95 = int(input("Duration of 95 degree step [s]:  "))
t_60 = int(input("Duration of 60 degree step [s]:  "))
t_72 = int(input("Duration of 72 degree step [s]:  "))
number_cycles = int(input("Number of cycles:  "))


start_pcr_audio = "audio/start_pcr.mp3"
start_pcr = gTTS(text="Die PCR startet in 30 sec mit dem 95 grad celcius Schritt. Mach dich bereit!", lang="de")
start_pcr.save(start_pcr_audio)

start_now_audio = "audio/start_now.mp3"
start_now = gTTS(text="Start", lang="de")
start_now.save(start_now_audio)

change_audio = "audio/change.mp3"
change = gTTS(text="5 Sekunden", lang="de")
change.save(change_audio)

now_change_audio = "audio/change_now.mp3"
now_change = gTTS(text="Jetzt wechseln", lang="de")
now_change.save(now_change_audio)

temp1_audio = "audio/temp1.mp3"
temp1 = gTTS(text="95 Grad Celcius fuer " + str(t_95) + " sec", lang="de")
temp1.save(temp1_audio)

temp2_audio = "audio/temp2.mp3"
temp2 = gTTS(text="60 Grad Celcius fuer " + str(t_60) + " sec", lang="de")
temp2.save(temp2_audio)

temp3_audio = "audio/temp3.mp3"
temp3 = gTTS(text="72 Grad Celcius fuer " + str(t_72) + " sec", lang="de")
temp3.save(temp3_audio)

for i in range(1,number_cycles + 1):
    step_audio = "audio/step" + str(i) + ".mp3"
    step = gTTS(text="Zyclus " + str(i), lang="de")
    step.save(step_audio)

# Save chosen program:
prog = open("programs/" + experiment_name + "_pcr_prot.txt","w")
prog.write("Number of cycles:" + "\t" + str(number_cycles) + "\n")
prog.write("Step" + "\t" + "Temp:" + "\t" + "Time [s]:" + "\n")
prog.write("1" + "\t" + "95" + "\t" + str(t_95) + "\n")
prog.write("2" + "\t" + "60" + "\t" + str(t_60) + "\n")
prog.write("3" + "\t" + "72" + "\t" + str(t_72) + "\n")

prog.close()


mixer.music.load(start_pcr_audio)
mixer.music.play()
while mixer.music.get_busy() == 1:
    continue
time.sleep(25)
mixer.music.load(change_audio)
mixer.music.play()
while mixer.music.get_busy() == 1:
    continue
time.sleep(5)
mixer.music.load(start_now_audio)
mixer.music.play()
while mixer.music.get_busy() == 1:
    continue

print("START")
for i in range(0,number_cycles):
    step = "audio/step" + str(i+1) + ".mp3"
    print("##########")
    print("Step:  " + str(i+1))
    print("##########")
    print("95 grad Celcius")
    mixer.music.load(step)
    mixer.music.play()
    while mixer.music.get_busy() == 1:
        continue
    mixer.music.load(temp1_audio)
    mixer.music.play()
    while mixer.music.get_busy() == 1:
        continue
    time.sleep(t_95-4-2-5)
    mixer.music.load(change_audio)
    mixer.music.play()
    while mixer.music.get_busy() == 1:
        continue
    time.sleep(5)
    mixer.music.load(now_change_audio)
    mixer.music.play()
    while mixer.music.get_busy() == 1:
        continue

    print("60 grad celcius")
    mixer.music.load(temp2_audio)
    mixer.music.play()
    while mixer.music.get_busy() == 1:
        continue
    time.sleep(t_60-4-2-5)
    mixer.music.load(change_audio)
    mixer.music.play()
    while mixer.music.get_busy() == 1:
        continue
    time.sleep(5)
    mixer.music.load(now_change_audio)
    mixer.music.play()
    while mixer.music.get_busy() == 1:
        continue
    
    print("72 grad celcius")
    mixer.music.load(temp3_audio)
    mixer.music.play()
    while mixer.music.get_busy() == 1:
        continue
    time.sleep(t_72-4-2-5)
    mixer.music.load(change_audio)
    mixer.music.play()
    while mixer.music.get_busy() == 1:
        continue
    time.sleep(5)
    mixer.music.load(now_change_audio)
    mixer.music.play()
    while mixer.music.get_busy() == 1:
        continue


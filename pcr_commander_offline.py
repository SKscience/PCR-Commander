from gtts import gTTS
import time
from pygame import mixer
mixer.init()

experiment_name = input("Name of experiment:  ")
t_95 = int(input("Duration of 95 degree step [s]:  ")) # 35
t_60 = int(input("Duration of 60 degree step [s]:  ")) # 40
t_72 = int(input("Duration of 72 degree step [s]:  ")) # 50
number_cycles = int(input("Number of cycles:  ")) # 45


# Save chosen program:
prog = open("programs/" + experiment_name + "_pcr_prot.txt","w")
prog.write("Number of cycles:" + "\t" + str(number_cycles) + "\n")
prog.write("Step" + "\t" + "Temp:" + "\t" + "Time [s]:" + "\n")
prog.write("1" + "\t" + "95" + "\t" + str(t_95) + "\n")
prog.write("2" + "\t" + "60" + "\t" + str(t_60) + "\n")
prog.write("3" + "\t" + "72" + "\t" + str(t_72) + "\n")

prog.close()

# Set audio paths
start_pcr_audio = "audio_offline/start_pcr.mp3"
change_audio = "audio_offline/change.mp3"
start_now_audio = "audio_offline/start_now.mp3"
temp1_audio = "audio_offline/temp1.mp3"
temp2_audio = "audio_offline/temp2.mp3"
temp3_audio = "audio_offline/temp3.mp3"


mixer.music.load(start_pcr_audio)
mixer.music.play()
while mixer.music.get_busy() == 1:
    continue
time.sleep(15)
mixer.music.load(change_audio)
mixer.music.play()
while mixer.music.get_busy() == 1:
    continue
time.sleep(3)
mixer.music.load(start_now_audio)
mixer.music.play()
while mixer.music.get_busy() == 1:
    continue

print("START")
for i in range(0,number_cycles):
    print("##########")
    print("Step:  " + str(i+1))
    print("##########")
    print("95 grad Celcius")


    mixer.music.load(temp1_audio)
    mixer.music.play()
    while mixer.music.get_busy() == 1:
        continue
    time.sleep(t_95-7)
    mixer.music.load(change_audio)
    mixer.music.play()
    while mixer.music.get_busy() == 1:
        continue
    time.sleep(5)

    print("60 grad celcius")
    mixer.music.load(temp2_audio)
    mixer.music.play()
    while mixer.music.get_busy() == 1:
        continue
    time.sleep(t_60-7)
    mixer.music.load(change_audio)
    mixer.music.play()
    while mixer.music.get_busy() == 1:
        continue
    time.sleep(5)
    
    print("72 grad celcius")
    mixer.music.load(temp3_audio)
    mixer.music.play()
    while mixer.music.get_busy() == 1:
        continue
    time.sleep(t_72-7)
    mixer.music.load(change_audio)
    mixer.music.play()
    while mixer.music.get_busy() == 1:
        continue
    time.sleep(5)


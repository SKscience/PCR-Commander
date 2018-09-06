import subprocess
from gtts import gTTS
import time

experiment_name = raw_input("Name of experiment:  ")
t_95 = int(raw_input("Duration of 95 degree step [s]:  "))
t_60 = int(raw_input("Duration of 60 degree step [s]:  "))
t_72 = int(raw_input("Duration of 72 degree step [s]:  "))
number_cycles = int(raw_input("Number of cycles:  "))


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


subprocess.call(["afplay", start_pcr_audio])
time.sleep(25)
subprocess.call(["afplay", change_audio])
time.sleep(5)
subprocess.call(["afplay", start_now_audio])


print("START")
for i in range(0,number_cycles):
    step = "audio/step" + str(i+1) + ".mp3"
    print("##########")
    print("Step:  " + str(i+1))
    print("##########")
    print("95 grad Celcius")
    subprocess.call(["afplay", step])
    subprocess.call(["afplay", temp1_audio])
    time.sleep(t_95-4-2-5)
    subprocess.call(["afplay", change_audio])
    time.sleep(5)
    subprocess.call(["afplay", now_change_audio])

    print("60 grad celcius")
    subprocess.call(["afplay", temp2_audio])
    time.sleep(t_60-4-2-5)
    subprocess.call(["afplay", change_audio])
    time.sleep(5)
    subprocess.call(["afplay", now_change_audio])
    
    print("72 grad celcius")
    subprocess.call(["afplay", temp3_audio])
    time.sleep(t_72-4-2-5)
    subprocess.call(["afplay", change_audio])
    time.sleep(5)
    subprocess.call(["afplay", now_change_audio])

#return_code = subprocess.call(["afplay", audio_file])

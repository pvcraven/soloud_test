import time

import soloud


audiolib = soloud.Soloud()
audiolib.init()
audiolib.set_global_volume(10)

wav = soloud.Wav()
wav.load("sounds/laser1.ogg")
audiolib.play(wav)
time.sleep(1)
audiolib.deinit()

print ("Bye")
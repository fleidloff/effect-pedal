import pyo
from settings import audioSource

s = pyo.Server(audio=audioSource, nchnls=1).boot()
s.start()

a = pyo.Input(chnl=0).out()

delay = pyo.Delay(a, delay=.5, feedback=.5)
delay.out()

while True:
    s = raw_input('Delay');
    if s == "q":
        quit()
    delay.setDelay(float(s))

#s.gui(locals())
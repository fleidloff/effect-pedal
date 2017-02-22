import pyo

s = pyo.Server(audio='jack', nchnls=1).boot()
s.start()

a = pyo.Input(chnl=0).out()

delay = pyo.Delay(a, delay=.1, feedback=.5)
delay.out()

while True:
    s = raw_input('Delay');
    if s == "q":
        quit()
    delay.setDelay(float(s))

#s.gui(locals())
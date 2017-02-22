import pyo
from settings import audioSource

s = pyo.Server(audio=audioSource, nchnls=1).boot()
s.start()

a = pyo.Input(chnl=0)
chorus = pyo.Chorus(a, depth=.9, feedback=0.5, bal=0.5).out()

s.gui()
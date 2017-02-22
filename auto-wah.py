import pyo

s = pyo.Server(audio='jack', nchnls=1).boot()
s.start()

a = pyo.Input(chnl=0)
fol = pyo.Follower(a, freq=30, mul=4000, add=400)
f = pyo.Biquad(a, freq=fol, q=5, type=2).out()

s.gui()
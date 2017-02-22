from pyo import *

s = Server(audio='jack', nchnls=1).boot()
s.start()
s.amp = 0.1

# Creates a sine wave as the source to process.
a = Sine()

# Passes the sine wave through an harmonizer.
hr = Harmonizer(a).out()

# Also through a chorus.
ch = Chorus(a).out()

# And through a frequency shifter.
sh = FreqShift(a).out()

s.gui(locals())
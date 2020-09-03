import sys
sys.path.insert(1,"dsp-modulo")

from thinkdsp import SinSignal
from thinkdsp import decorate

import matplotlib.pyplot as plt

seno = SinSignal(freq=10, amp=1, offset=0)

wave_seno = seno.make_wave(duration=1.0, start=0, framerate=22050)
wave_seno_frecuencia_muestreo_baja = seno.make_wave(duration=1.0, start=0, framerate=21)

decorate(xLabel="Tiempo (s)")
decorate(yLabel="Amplitud")
wave_seno.plot()
wave_seno_frecuencia_muestreo_baja.plot()
plt.show()

decorate(xLabel="Tiempo (s)")
decorate(yLabel="Amplitud")
wave_seno_frecuencia_muestreo_baja.plot()
plt.show()
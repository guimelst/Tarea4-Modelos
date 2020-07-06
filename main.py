#Guímel Madrigal Uecker
#B54060

import numpy as np
from scipy import stats
from scipy import signal
from scipy import integrate
import matplotlib.pyplot as plt


#Lectura de los datos:
bits = []
f = open("bits10k.csv")
for line in f:
    bits.append(int(line))
f.close()



#Parte1------------------------------------------------------------------


f = 5000 # Frecuencia
N = len(bits)#Cantidad de bits
T = 1/f # Duración del período de cada símbolo
p = 50#Puntos de muestreo por período
tp = np.linspace(0, T, p)#Puntos de muestreo para cada período
sinus = np.sin(2*np.pi * f * tp)# Creación de la forma de onda de la portadora

plt.plot(tp, sinus)
plt.xlabel('Tiempo (ms)')
plt.title('Onda portadora')
plt.savefig('Onda Portadora')



fs = p/T# Frecuencia de muestreo

t = np.linspace(0, N*T, N*p)# Creación de la línea temporal para toda la señal Tx


senal = np.zeros(t.shape)# Inicio del vector de la señal

# Creación de la señal modulada BPSK
for k, b in enumerate(bits):
    senal[k*p:(k+1)*p] = sinus if b else -sinus

# Visualización de los primeros bits (pb) modulados
pb = 10
tp = np.linspace(0, pb*T, pb*p)
plt.figure()
plt.plot(tp, senal[0:pb*p])
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud de la señal")
plt.title("Muestra de los primeros " + str(pb) + " periodos de la señal modulada")
plt.ticklabel_format(axis = "x", style = "sci", scilimits=(0,0))
plt.savefig('Primeros bits Modulados')
plt.show()

#Parte2-------------------------------------------------------------------------


Pinst = senal**2# Energía instantánea


Ps = integrate.trapz(Pinst, t) / (N * T)# Potencia promedio (W)

print("La potencia promedio de la señal modulada generada tiene un valor numérico de:", Ps)

#Parte3--------------------------------------------------------------------------

# Potencia con Welch antes del canal ruidoso
fw, PSD = signal.welch(senal, fs)
plt.figure()
plt.semilogy(fw, PSD)
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Densidad espectral de potencia')
plt.savefig("Densidad espectral de potencia")
plt.show()

# Listas para la graficación de BER vs SNR

BER = [] # Lista para obtener los valores de BER con cada dB de SNR
snrVals = list(range(-2,4)) # Rango de valores de SNR deseados, con 1 dB entre cada uno

# Relación señal ruido deseada
for SNR in snrVals:
 # señal recibida con cada SNR
  nameRxPlot = "Ruido" + str(SNR) 
    
# Método de Welch para cada SNR
# Potencia del ruido
Pn = Ps / (10**(SNR / 10))

# Desviación estándar del ruido
sigma = np.sqrt(Pn)

# Crear ruido

ruido = np.random.normal(0, sigma, senal.shape)

# canal señal recibida
Rx = senal + ruido

# Visualización de los primeros bits recibidos
plt.figure()
plt.plot(tp, Rx[0:pb*p])
plt.ticklabel_format(axis = "x", style = "sci", scilimits=(0,0))
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud de la señal recibida")
plt.title("Forma de Rx con SNR = " + str(SNR) + " dB")
plt.savefig("Forma de Rx con SNR = " + str(SNR) + " dB" + nameRxPlot)
plt.show()


Es = np.sum(sinus**2)# Pseudo-energía de la onda original


bitsRx = np.zeros(bits.shape)#bits recibidos

# Decodificación de la señal
for k, b in enumerate(bits):
  Ep = np.sum(Rx[k*p:(k+1)*p] * sinus) 

bitsRx[k] = 1 if (Ep > 0) else 0


#Parte4------------------------------------------------------------------------------------
#Potencia con Welch después del canal ruidoso
fw, PSD = signal.welch(Rx, fs)
plt.figure()
plt.semilogy(fw, PSD)
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Densidad espectral de potencia')
plt.title("Densidad espectral de potencia con SNR de " + str(SNR) + " dB")
plt.savefig("Densidad espectral de potencia con SNR de " + str(SNR) + " dB")
plt.show()

#Parte5----------------------------------------------------------------------------------
#bits erróneros en la señal recibida
err = np.sum(np.abs(bits - bitsRx))
BER.append(err/N)

for n in range(0,11):
print(bitsRx[n])

#Parte6---------------------------------------------------------------------
# Graficación de BER vs SNR
plt.figure()
plt.plot(snrVals, BER)
plt.xlabel("SNR (dB)")
plt.ylabel("BER")
plt.title("Bit Error Rate en función del SNR")
plt.savefig("Bit Error Rate en función del SNR")
plt.show
# Tarea4-Modelos Guímel Madrigal B54060


Parte #1

Se generó la señal portadora de amplitud unitaria normalizada

![img](https://github.com/guimelst/Tarea4-Modelos/blob/master/ondaportadora.png)

Luego se concatenó las diferentes formas de onda

![img]

#Parte 2

Dado que la potyencia promedio de la señal esta dada con la siguiente fórmula, se calcula:

<img src="https://latex.codecogs.com/gif.latex?Psin&space;=&space;\frac{1}{2T}\int_{-T}^{T}{sen}^2(\frac{2\pi&space;t}{T})dt" title="Psin = \frac{1}{2T}\int_{-T}^{T}{sen}^2(\frac{2\pi t}{T})dt" /></a>

Se obtiene:

<img src="https://latex.codecogs.com/gif.latex?P(T)\approx&space;0.49" title="P(T)\approx 0.49" /></a>

#Parte 3

Desviación Estandar, para modelar el ruido.

<img src="https://latex.codecogs.com/gif.latex?\sigma&space;=&space;\sqrt{P_{n}}" title="\sigma = \sqrt{P_{n}}" /></a>

Donde <img src="https://latex.codecogs.com/gif.latex?P_{n}" title="P_{n}" /></a> es la potencia del ruido

<img src="https://latex.codecogs.com/gif.latex?P_{n}=\frac{P_{s}}{10^{\frac{SNR_{dB}}{10}}}" title="P_{n}=\frac{P_{s}}{10^{\frac{SNR_{dB}}{10}}}" /></a>

Donde <img src="https://latex.codecogs.com/gif.latex?P_{s}" title="P_{s}" /></a> e s la potencia promedio de la onda modulada.

Se obtuvo la desviación estandar, con diferentes SNR:

Con -2 dB:

![img](https://github.com/guimelst/Tarea4-Modelos/blob/master/R-1.png)

Con -1 dB:

![img](https://github.com/guimelst/Tarea4-Modelos/blob/master/R-2.png)

Con 0 dB:

![img](https://github.com/guimelst/Tarea4-Modelos/blob/master/R00.png)

Con 1 dB:

![img](https://github.com/guimelst/Tarea4-Modelos/blob/master/R1.png)

Con 2 dB:

![img](https://github.com/guimelst/Tarea4-Modelos/blob/master/R2.png)

Con 3 dB:

![img](https://github.com/guimelst/Tarea4-Modelos/blob/master/R33.png)

#Parte 4

PDS -2 dB:

![img]

PDS -1 dB:

![img]

PDS 0 dB:

![img]

PDS 1 dB:

![img]

PDS 2 dB:

![img]

PDS 3 dB:

#Parte 5

Sabiendo que para demular y decodificar se ocupan los productos internos de dos funciones:

<img src="https://latex.codecogs.com/gif.latex?f,g&space;=\int_{a}^{b}f(t)g(t)dt" title="f,g =\int_{a}^{b}f(t)g(t)dt" /></a>

Teniendo a f(t) como la señal transmitida y g(t) como la señal portadora, se obtiene que:

<img src="https://latex.codecogs.com/gif.latex?f(t)g(t)&space;=sen^2(2\pi&space;f_{c}t)" title="f(t)g(t) =sen^2(2\pi f_{c}t)" /></a>

con el bit 1 relacionado con f(t), cuando el bit relacionado con f(t) es 0, entonces:

<img src="https://latex.codecogs.com/gif.latex?f(t)g(t)&space;=-sen^2(2\pi&space;f_{c}t)" title="f(t)g(t) =-sen^2(2\pi f_{c}t)" /></a>

#Parte 6

![img](https://github.com/guimelst/Tarea4-Modelos/blob/master/BERvsSNR.png?raw=true)

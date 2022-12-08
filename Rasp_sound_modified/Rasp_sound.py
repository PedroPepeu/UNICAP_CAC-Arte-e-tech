import RPi.GPIO as GPIO
import vlc
import time

#Definindo pins e setando GPIO:
trigger_pin = 16
echo_pin = 18
GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

#Metodo setup:
def default():
    GPIO.output(trigger_pin, False)
    time.sleep(2)
    volume = 0
    iniciar_musica = False
    musica = vlc.MediaPlayer("./Music/como-uma-onda.mp3")

#Definindo setup:
default()

#Metodo para calcular distancia:
def calcularDistancia():
    #Ativando trigger:
    GPIO.output(trigger_pin, True)
    time.sleep(0.00001)
    GPIO.output(trigger_pin, False)

    #Definindo tempos inicial/final
    while GPIO.input(echo_pin) == 0:
        tempo_inicial = time.time()
    while GPIO.input(echo_pin) == 1:
        tempo_final = time.time()

    #Calculando delta tempo
    variacao_tempo = tempo_final - tempo_inicial

    #Distancia = Vm * Dtempo, Vm = 343m/s(som); Dtempo = variacao/2(pois o som percorre a distancia 2x)
    distancia = (variacao_tempo * 34300)/2

    #Arredondar
    distancia = round(distancia, 2)
    return distancia

#Tratar excessoes:





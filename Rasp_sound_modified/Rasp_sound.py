import RPi.GPIO as GPIO
import vlc
import time

#Definindo pins e setando GPIO:
trigger_pin = 16
echo_pin = 18
GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

#Metodo setup:
GPIO.output(trigger_pin, False)
time.sleep(2)
volume = 0
distancia_maxima = 80
parar_musica = True
tempo_iniciar_som = 10
tempo_encerrar_som = 20
musica = vlc.MediaPlayer("./Music/como-uma-onda.mp3")

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
try:
    distancia = calcularDistancia()
    
    #Alguem se aproxima:
    if distancia <= distancia_maxima:
        parar_musica = False
        musica.play()
        for i in range(1, tempo_iniciar_som):
            volume = (round(i/tempo_iniciar_som))*100
            musica.audio_set_volume(volume)
            time.sleep(1)

    #Nao ha ninguem:
    if distancia > distancia_maxima and (not parar_musica):
        parar_musica = True
        for j in range(tempo_encerrar_som, 1, -1):
            volume = (round(i/tempo_encerrar_som))*100
            musica.audio_set_volume(volume)
            time.sleep(1)
        musica.stop()
        
except KeyboardInterrupt():
    GPIO.cleanup()




import RPi.GPIO as GPIO
import vlc
import time

#Definindo pins e setando GPIO:
GPIO.setmode(GPIO.BOARD)
trigger_pin = 16
echo_pin = 18
GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

#Metodo setup:
GPIO.output(trigger_pin, False)
time.sleep(2)
tempo_iniciar_som = 10
tempo_encerrar_som = 20
volume = 0
distancia_maxima = 80
musica_tocando = False
musica = vlc.MediaPlayer("./Music/como-uma-onda.mp3")

#Metodo para calcular distancia:
def calcularDistancia():
    tempo_inicial = 0
    tempo_final = 0
    #Ativando trigger:
    GPIO.output(trigger_pin, True)
    time.sleep(0.00001)
    GPIO.output(trigger_pin, False)

    #Definindo tempos inicial/final
    while GPIO.input(echo_pin) == 0:
        tempo_inicial = time.time()
        time.sleep(0.00001)
    while GPIO.input(echo_pin) == 1:
        tempo_final = time.time()
        time.sleep(0.00001)

    #Calculando delta tempo
    variacao_tempo = tempo_final - tempo_inicial

    #Distancia = Vm * Dtempo, Vm = 343m/s(som); Dtempo = variacao/2(pois o som percorre a distancia 2x)
    distancia = (variacao_tempo * 34300)/2

    #Arredondar
    distancia = round(distancia, 2)
    return distancia

#Tratar excessoes:
while True:
    try:
        distancia = calcularDistancia()
        
        #Alguem se aproxima:
        if distancia <= distancia_maxima and (not musica_tocando):
            print('Musica começou a tocar!')
            musica.play()
            
            for i in range(1, tempo_iniciar_som+1):
                volume = round(i/tempo_iniciar_som*100)
                print('Volume: ', volume)
                musica.audio_set_volume(volume)
                time.sleep(1)
            
            musica_tocando = True
        
        #Ainda há presença:
        if distancia <= distancia_maxima and musica_tocando:
            time.sleep(1)

        #Nao ha ninguem:
        if distancia > distancia_maxima and musica_tocando:
            musica_tocando = False
            for j in range(tempo_encerrar_som, -1, -1):
                volume = round(j/tempo_encerrar_som*100)
                print('Volume: ', volume)
                musica.audio_set_volume(volume)
                time.sleep(1)
            musica.stop()
            print('Musica parou a tocar!')

    except KeyboardInterrupt():
        GPIO.cleanup()




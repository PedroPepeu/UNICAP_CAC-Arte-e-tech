import RPi.GPIO as GPIO
import vlc
import time

#Definindo pins e setando GPIO:
GPIO.setmode(GPIO.BOARD)
trigger_pin = 16
echo_pin = 18
arduino = 4
GPIO.setup(arduino, GPIO.IN)
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
musica = vlc.MediaPlayer("./")

if arduino == 1:
    if (not musica_tocando):
        print('Musica começou a tocar!')
        musica.play()
        for i in range(1, tempo_iniciar_som+1):
            volume = round(i/tempo_iniciar_som*100)
            print('Volume: ', volume)
            musica.audio_set_volume(volume)
            time.sleep(1)
            
            musica_tocando = True
else:
    if musica_tocando:
        musica_tocando = False
        for j in range(tempo_encerrar_som, -1, -1):
            volume = round(j/tempo_encerrar_som*100)
            print('Volume: ', volume)
            musica.audio_set_volume(volume)
            time.sleep(1)
        musica.stop()
        print('Musica parou a tocar!')


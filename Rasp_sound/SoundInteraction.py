import RPi.GPIO as GPIO
import vlc
import time


GPIO.setmode(GPIO.BOARD)

TRIG = 16
ECHO = 18
i=0

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
time.sleep(2)
volume = 100
musicStop = True

music = vlc.MediaPlayer("./Music/como-uma-onda.mp3")

try:
    while True:
       GPIO.output(TRIG, True)
       time.sleep(0.00001)
       GPIO.output(TRIG, False)

       while GPIO.input(ECHO)==0:
          pulse_start = time.time()

       while GPIO.input(ECHO)==1:
          pulse_end = time.time()

       pulse_duration = pulse_end - pulse_start

       distance = pulse_duration * 17150

       distance = round(distance+1.15, 2)
       
       music.audio_set_volume(100)

       if distance < 10:
           music.play()
           musicStop = False
           time.sleep(10)
    
       if distance > 10 and (not musicStop):
               while i < 5:
                   volume = volume - (volume/2)
                   music.audio_set_volume(round(volume))
                   time.sleep(1)
                   i += 1
               music.stop()
               musicStop = True
               i = 0
                
        
       volume = 100
except KeyboardInterrupt:
     GPIO.cleanup()
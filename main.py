import weatherbit 
#from math import *
from serial import * 

from tkinter import *
#from threaded import *
from time import *
#from logging import *



def on_button_pressed_a():
    global item
    item = not (item)
#input.on_button_pressed(Button.A, on_button_pressed_a)

current_WindDirection_List = ""
current_WindSpeed = 0
tempC = 0
item = False
log.set_labels('wind', 'dir', 'STemp', 'Temp', 'humidity', 'pressure')
#serial.redirect_to_usb()
#Serial.redirect(SerialPin.P15, SerialPin.P14, BaudRate.BAUD_RATE9600)
weatherbit.start_wind_monitoring()
weatherbit.start_weather_monitoring()
item = True
"""

Note: If "???" is displayed, direction is unknown!

"""

def on_forever():
    global current_WindSpeed, current_WindDirection_List
    global tempC

    # -------- wind --------
    current_WindSpeed = weatherbit.wind_speed() * 3600 / 1000
    current_WindDirection_List = weatherbit.wind_direction()

    # -------- temperature --------
    StempC = (weatherbit.soil_temperature() / 100)
    tempC = (weatherbit.temperature()/ 100)
    # -------- humidity --------

    humid = (weatherbit.humidity()/ 1024)
    # -------- pressure --------
    pressure = (weatherbit.pressure()/ 25600)

  
    log.add({'ws': current_WindSpeed, 'wd': current_WindDirection_List,
             'stc': StempC, 'tc': tempC, 'hmd' : humid, 'prs' : pressure})
#    Serial.write_line("" + str(Math.round(current_WindSpeed)) + "," + current_WindDirection_List + "," + StempC+"," + tempC+"," + humid+"," + pressure)

    
    time.sleep(3000)
    
while True:
    on_forever()

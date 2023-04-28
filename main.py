
def on_button_pressed_a():
    global item
    item = not (item)
input.on_button_pressed(Button.A, on_button_pressed_a)

current_WindDirection_List = ""
current_WindSpeed = 0
tempC = 0
item = False
serial.redirect_to_usb()
weatherbit.start_wind_monitoring()
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
#    if item:
#        basic.show_string("Sp")
#        basic.show_number(Math.round(current_WindSpeed))
#    else:
#        basic.show_string("Dir")
#        basic.show_string(current_WindDirection_List)

    # -------- temperature --------
    tempC = Math.idiv(weatherbit.soil_temperature(), 100)
#    if item:
#        basic.show_string("Ground Temp: ")
#        basic.show_number(tempC)
#    else:
#        if tempC < 12:
#            basic.show_string("Don't Plant!")
#        else:
#            basic.show_string("Plant")

    serial.write_line("" + str(Math.round(current_WindSpeed)) + "," + current_WindDirection_List + "," +tempC)
    basic.pause(1 * 3000)
    
basic.forever(on_forever)

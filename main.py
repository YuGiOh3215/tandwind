
def on_button_pressed_a():
    global item
    item = not (item)
input.on_button_pressed(Button.A, on_button_pressed_a)

current_WindDirection_List = ""
current_WindSpeed = 0
item = False
serial.redirect_to_usb()
weatherbit.start_wind_monitoring()
item = True
"""

Note: If "???" is displayed, direction is unknown!

"""

def on_forever():
    global current_WindSpeed, current_WindDirection_List
    current_WindSpeed = weatherbit.wind_speed() * 3600 / 1000
    current_WindDirection_List = weatherbit.wind_direction()
    if item:
        basic.show_string("Sp")
        basic.show_number(Math.round(current_WindSpeed))
    else:
        basic.show_string("Dir")
        basic.show_string(current_WindDirection_List)
    serial.write_line("" + str(current_WindSpeed) + "," + current_WindDirection_List)
basic.forever(on_forever)

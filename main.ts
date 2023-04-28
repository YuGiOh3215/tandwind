input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    item = !item
})
let current_WindDirection_List = ""
let current_WindSpeed = 0
let tempC = 0
let item = false
serial.redirectToUSB()
weatherbit.startWindMonitoring()
item = true
/** Note: If "???" is displayed, direction is unknown! */
basic.forever(function on_forever() {
    
    
    //  -------- wind --------
    current_WindSpeed = weatherbit.windSpeed() * 3600 / 1000
    current_WindDirection_List = weatherbit.windDirection()
    //     if item:
    //         basic.show_string("Sp")
    //         basic.show_number(Math.round(current_WindSpeed))
    //     else:
    //         basic.show_string("Dir")
    //         basic.show_string(current_WindDirection_List)
    //  -------- temperature --------
    tempC = Math.idiv(weatherbit.soilTemperature(), 100)
    //     if item:
    //         basic.show_string("Ground Temp: ")
    //         basic.show_number(tempC)
    //     else:
    //         if tempC < 12:
    //             basic.show_string("Don't Plant!")
    //         else:
    //             basic.show_string("Plant")
    serial.writeLine("" + ("" + Math.round(current_WindSpeed)) + "," + current_WindDirection_List + "," + tempC)
    basic.pause(1 * 3000)
})

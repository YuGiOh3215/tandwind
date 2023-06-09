input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    item = !item
})
let current_WindDirection_List = ""
let current_WindSpeed = 0
let tempC = 0
let item = false
// serial.redirect_to_usb()
serial.redirect(SerialPin.P15, SerialPin.P14, BaudRate.BaudRate9600)
weatherbit.startWindMonitoring()
weatherbit.startWeatherMonitoring()
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
    let StempC = Math.idiv(weatherbit.soilTemperature(), 100)
    tempC = Math.idiv(weatherbit.temperature(), 100)
    let humid = Math.idiv(weatherbit.humidity(), 1024)
    let pressure = Math.idiv(weatherbit.pressure(), 25600)
    //     if item:
    //         basic.show_string("Ground Temp: ")
    //         basic.show_number(tempC)
    //     else:
    //         if tempC < 12:
    //             basic.show_string("Don't Plant!")
    //         else:
    //             basic.show_string("Plant")
    serial.writeLine("" + ("" + Math.round(current_WindSpeed)) + "," + current_WindDirection_List + "," + StempC + "," + tempC + "," + humid + "," + pressure)
    basic.pause(1 * 3000)
})

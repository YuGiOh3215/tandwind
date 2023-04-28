input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    item = !item
})
let current_WindDirection_List = ""
let current_WindSpeed = 0
let item = false
serial.redirectToUSB()
weatherbit.startWindMonitoring()
item = true
/** Note: If "???" is displayed, direction is unknown! */
basic.forever(function on_forever() {
    
    current_WindSpeed = weatherbit.windSpeed() * 3600 / 1000
    current_WindDirection_List = weatherbit.windDirection()
    if (item) {
        basic.showString("Sp")
        basic.showNumber(Math.round(current_WindSpeed))
    } else {
        basic.showString("Dir")
        basic.showString(current_WindDirection_List)
    }
    
    serial.writeLine("" + ("" + current_WindSpeed) + "," + current_WindDirection_List)
})

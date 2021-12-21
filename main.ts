basic.forever(function on_forever() {
    let USB = 15000
    basic.showNumber(USB)
    basic.showString("W")
    basic.pause(1000)
    basic.showString("BUY USB FOR ME")
    basic.showString("ok is A, no is B")
    
})
function on_button_pressed_b() {
    basic.showString("I hate you fuck you ssiballuma")
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showString("I love you bro")
    
})

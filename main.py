def on_forever():
    USB = 15000
    basic.show_number(USB)
    basic.show_string("W")
    basic.pause(1000)
    basic.show_string("BUY USB FOR ME")
    basic.show_string("ok is A, no is B")
    pass

basic.forever(on_forever)

def on_button_pressed_a():
    basic.show_string("I love you bro")
    pass
def on_button_pressed_b():
    basic.show_string("I hate you fuck you ssiballuma")

input.on_button_pressed(Button.A, on_button_pressed_a)
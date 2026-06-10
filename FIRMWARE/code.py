import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())


keyboard.matrix = KeysScanner(
    pins=[
        board.GP29,  
        board.GP28,  
        board.GP27,  
        board.GP26,  
        board.GP25,  
        board.GP24,  
        board.GP23,  
    ],
    value_when_pressed=False,
)


keyboard.keymap = [
    [
        KC.VOLU,   
        KC.VOLD,  
        KC.VOLU,   
        KC.KP_SLASH,  
        KC.KP_ASTERISK,  
        KC.KP_MINUS,  
        KC.KP_PLUS,   
    ]
]

keyboard.go()
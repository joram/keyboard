from keycode import Keycode
import board

ROW_PIN_1=board.A3
ROW_PIN_2=board.A2
ROW_PIN_3=board.A1
ROW_PIN_4=board.A0
ROW_PIN_5=board.CLK
ROW_PIN_6=board.MISO

COL_PIN_1=board.D2
COL_PIN_2=board.D3
COL_PIN_3=board.D4
COL_PIN_4=board.D5
COL_PIN_5=board.D6
COL_PIN_6=board.D7

VARIABLE_NAMES = {
    board.A3: "ROW_PIN_1",
    board.A2: "ROW_PIN_2",
    board.A1: "ROW_PIN_3",
    board.A0: "ROW_PIN_4",
    board.CLK: "ROW_PIN_5",
    board.MISO: "ROW_PIN_6",

    board.D2: "COL_PIN_1",
    board.D3: "COL_PIN_2",
    board.D4: "COL_PIN_3",
    board.D5: "COL_PIN_4",
    board.D6: "COL_PIN_5",
    board.D7: "COL_PIN_6",
}

class BaseKey():

    def _keycode_to_name(self, keycode):
        return {
            Keycode.A: "A",
            Keycode.B: "B",
            Keycode.C: "C",
            Keycode.D: "D",
            Keycode.E: "E",
            Keycode.F: "F",
            Keycode.G: "G",
            Keycode.H: "H",
            Keycode.I: "I",
            Keycode.J: "J",
            Keycode.K: "K",
            Keycode.L: "L",
            Keycode.M: "M",
            Keycode.N: "N",
            Keycode.O: "O",
            Keycode.P: "P",
            Keycode.Q: "Q",
            Keycode.R: "R",
            Keycode.S: "S",
            Keycode.T: "T",
            Keycode.U: "U",
            Keycode.V: "V",
            Keycode.W: "W",
            Keycode.X: "X",
            Keycode.Y: "Y",
            Keycode.Z: "Z",
            Keycode.ONE: "1",
            Keycode.TWO: "2",
            Keycode.THREE: "3",
            Keycode.FOUR: "4",
            Keycode.FIVE: "5",
            Keycode.SIX: "6",
            Keycode.SEVEN: "7",
            Keycode.EIGHT: "8",
            Keycode.NINE: "9",
            Keycode.ZERO: "0",
            Keycode.ENTER: "Enter",
            Keycode.SPACE: "Space",
            Keycode.BACKSPACE: "Backspace",
            Keycode.TAB: "Tab",
            Keycode.ESCAPE: "Esc",
            Keycode.PAGE_UP: "Page Up",
            Keycode.PAGE_DOWN: "Page Down",
            Keycode.HOME: "Home",
            Keycode.END: "End",
            Keycode.INSERT: "Insert",
            Keycode.DELETE: "Delete",
            Keycode.LEFT_CONTROL: "Left Control",
            Keycode.RIGHT_CONTROL: "Right Control",
            Keycode.LEFT_SHIFT: "Left Shift",
            Keycode.RIGHT_SHIFT: "Right Shift",
            Keycode.LEFT_ALT: "Left Alt",
            Keycode.RIGHT_ALT: "Right Alt",
            Keycode.LEFT_GUI: "Left GUI",
            Keycode.RIGHT_GUI: "Right GUI",
            Keycode.LEFT_ARROW: "Left Arrow",
            Keycode.RIGHT_ARROW: "Right Arrow",
            Keycode.UP_ARROW: "Up Arrow",
            Keycode.DOWN_ARROW: "Down Arrow",
            Keycode.LEFT_BRACKET: "Left Bracket",
            Keycode.RIGHT_BRACKET: "Right Bracket",
            Keycode.BACKSLASH: "Backslash",
            Keycode.SEMICOLON: "Semicolon",
            Keycode.QUOTE: "Quote",
            Keycode.COMMA: "Comma",
            Keycode.PERIOD: "Period",
            Keycode.FORWARD_SLASH: "Forward Slash",
            Keycode.MINUS: "Minus",
            Keycode.EQUALS: "Equals",
            Keycode.CAPS_LOCK: "Caps Lock",
            Keycode.POUND: "Pound",
            Keycode.APPLICATION: "Super",
            Keycode.SHIFT: "Shift",
            Keycode.CONTROL: "Control",
            Keycode.LEFT_ALT: "Alt",
        }[keycode]
    
    def __init__(self, keycode, row_pin, col_pin):
        self.name = self._keycode_to_name(keycode)
        self.keycode = keycode
        self.row_pin = row_pin
        self.col_pin = col_pin


    def keypress(self, hid_keyboard):
        print(f"Key pressed: {self.name}")
        # Check if this is a modifier key that should be held
        is_modifier = (self.keycode in [
            Keycode.LEFT_SHIFT, Keycode.RIGHT_SHIFT,
            Keycode.LEFT_CONTROL, Keycode.RIGHT_CONTROL,
            Keycode.LEFT_ALT, Keycode.RIGHT_ALT,
            Keycode.LEFT_GUI, Keycode.RIGHT_GUI,
            Keycode.SHIFT, Keycode.CONTROL,
        ])
        
        if is_modifier:
            # Modifier key: press and hold
            hid_keyboard.press(self.keycode)
        else:
            # Regular key: press and release immediately
            hid_keyboard.send(self.keycode)

    def keyrelease(self, hid_keyboard):
        print(f"Key released: {self.name}")
        # Check if this is a modifier key
        is_modifier = (self.keycode in [
            Keycode.LEFT_SHIFT, Keycode.RIGHT_SHIFT,
            Keycode.LEFT_CONTROL, Keycode.RIGHT_CONTROL,
            Keycode.LEFT_ALT, Keycode.RIGHT_ALT,
            Keycode.LEFT_GUI, Keycode.RIGHT_GUI,
            Keycode.SHIFT, Keycode.CONTROL,
        ])
        
        if is_modifier:
            # Modifier key: release it
            hid_keyboard.release(self.keycode)
        # Regular keys are already released by send(), so no action needed


KEY_6 = BaseKey(keycode=Keycode.SIX, row_pin=ROW_PIN_1, col_pin=COL_PIN_1)
KEY_7 = BaseKey(keycode=Keycode.SEVEN, row_pin=ROW_PIN_1, col_pin=COL_PIN_2)
KEY_8 = BaseKey(keycode=Keycode.EIGHT, row_pin=ROW_PIN_1, col_pin=COL_PIN_3)
KEY_9 = BaseKey(keycode=Keycode.NINE, row_pin=ROW_PIN_1, col_pin=COL_PIN_4)
KEY_0 = BaseKey(keycode=Keycode.ZERO, row_pin=ROW_PIN_2, col_pin=COL_PIN_5)
KEY_MINUS = BaseKey(keycode=Keycode.MINUS, row_pin=ROW_PIN_2, col_pin=COL_PIN_6)

KEY_Y = BaseKey(keycode=Keycode.Y, row_pin=ROW_PIN_2, col_pin=COL_PIN_1)
KEY_U = BaseKey(keycode=Keycode.U, row_pin=ROW_PIN_2, col_pin=COL_PIN_2)
KEY_I = BaseKey(keycode=Keycode.I, row_pin=ROW_PIN_2, col_pin=COL_PIN_3)
KEY_O = BaseKey(keycode=Keycode.O, row_pin=ROW_PIN_2, col_pin=COL_PIN_4)
KEY_P = BaseKey(keycode=Keycode.P, row_pin=ROW_PIN_3, col_pin=COL_PIN_5)
KEY_EQUALS = BaseKey(keycode=Keycode.EQUALS, row_pin=ROW_PIN_3, col_pin=COL_PIN_6)

KEY_H = BaseKey(keycode=Keycode.H, row_pin=ROW_PIN_3, col_pin=COL_PIN_1)
KEY_J = BaseKey(keycode=Keycode.J, row_pin=ROW_PIN_3, col_pin=COL_PIN_2)
KEY_K = BaseKey(keycode=Keycode.K, row_pin=ROW_PIN_3, col_pin=COL_PIN_3)
KEY_L = BaseKey(keycode=Keycode.L, row_pin=ROW_PIN_3, col_pin=COL_PIN_4)
KEY_SEMICOLON = BaseKey(keycode=Keycode.SEMICOLON, row_pin=ROW_PIN_4, col_pin=COL_PIN_5)
KEY_QUOTE = BaseKey(keycode=Keycode.QUOTE, row_pin=ROW_PIN_4, col_pin=COL_PIN_6)

KEY_N = BaseKey(keycode=Keycode.N, row_pin=ROW_PIN_4, col_pin=COL_PIN_1)
KEY_M = BaseKey(keycode=Keycode.M, row_pin=ROW_PIN_4, col_pin=COL_PIN_2)
KEY_COMMA = BaseKey(keycode=Keycode.COMMA, row_pin=ROW_PIN_4, col_pin=COL_PIN_3)
KEY_PERIOD = BaseKey(keycode=Keycode.PERIOD, row_pin=ROW_PIN_4, col_pin=COL_PIN_4)
KEY_OPEN_BRACKET = BaseKey(keycode=Keycode.LEFT_BRACKET, row_pin=ROW_PIN_5, col_pin=COL_PIN_5)
KEY_CLOSE_BRACKET = BaseKey(keycode=Keycode.RIGHT_BRACKET, row_pin=ROW_PIN_5, col_pin=COL_PIN_6)

KEY_LEFT_ARROW = BaseKey(keycode=Keycode.LEFT_ARROW, row_pin=ROW_PIN_5, col_pin=COL_PIN_2)
KEY_UP_ARROW = BaseKey(keycode=Keycode.UP_ARROW, row_pin=ROW_PIN_5, col_pin=COL_PIN_3)
KEY_RIGHT_ARROW = BaseKey(keycode=Keycode.RIGHT_ARROW, row_pin=ROW_PIN_5, col_pin=COL_PIN_4)
KEY_FORWARD_SLASH = BaseKey(keycode=Keycode.FORWARD_SLASH, row_pin=ROW_PIN_1, col_pin=COL_PIN_5)
KEY_BACKSLASH = BaseKey(keycode=Keycode.BACKSLASH, row_pin=ROW_PIN_1, col_pin=COL_PIN_6)

KEY_SPACE = BaseKey(keycode=Keycode.SPACE, row_pin=ROW_PIN_6, col_pin=COL_PIN_2)
KEY_DOWN_ARROW = BaseKey(keycode=Keycode.DOWN_ARROW, row_pin=ROW_PIN_6, col_pin=COL_PIN_3)
KEY_DELETE = BaseKey(keycode=Keycode.DELETE, row_pin=ROW_PIN_6, col_pin=COL_PIN_4)
KEY_FORWARD_SLASH = BaseKey(keycode=Keycode.FORWARD_SLASH, row_pin=ROW_PIN_6, col_pin=COL_PIN_5)
KEY_BACKSLASH = BaseKey(keycode=Keycode.BACKSLASH, row_pin=ROW_PIN_6, col_pin=COL_PIN_6)

RIGHT_KEYS = [
    KEY_6, KEY_7, KEY_8, KEY_9, KEY_0, KEY_MINUS,
    KEY_Y, KEY_U, KEY_I, KEY_O, KEY_P, KEY_EQUALS,
    KEY_H, KEY_J, KEY_K, KEY_L, KEY_SEMICOLON, KEY_QUOTE,
    KEY_N, KEY_M, KEY_COMMA, KEY_PERIOD, KEY_OPEN_BRACKET, KEY_CLOSE_BRACKET, KEY_SPACE,
    KEY_LEFT_ARROW, KEY_UP_ARROW, KEY_RIGHT_ARROW, KEY_FORWARD_SLASH, KEY_BACKSLASH,
    KEY_SPACE, KEY_DOWN_ARROW, KEY_DELETE,KEY_FORWARD_SLASH, KEY_BACKSLASH,
]
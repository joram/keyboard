from keys_right import VARIABLE_NAMES, BaseKey
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

# special keys
COL_PIN_7=board.D8
COL_PIN_8=board.D9
COL_PIN_9=board.D10
COL_PIN_10=board.MOSI

KEY_BACKTICK = BaseKey(keycode=Keycode.POUND, row_pin=ROW_PIN_2, col_pin=COL_PIN_1)
KEY_ONE = BaseKey(keycode=Keycode.ONE, row_pin=ROW_PIN_2, col_pin=COL_PIN_2)
KEY_TWO = BaseKey(keycode=Keycode.TWO, row_pin=ROW_PIN_1, col_pin=COL_PIN_3)
KEY_THREE = BaseKey(keycode=Keycode.THREE, row_pin=ROW_PIN_1, col_pin=COL_PIN_4)
KEY_FOUR = BaseKey(keycode=Keycode.FOUR, row_pin=ROW_PIN_1, col_pin=COL_PIN_5)
KEY_FIVE = BaseKey(keycode=Keycode.FIVE, row_pin=ROW_PIN_1, col_pin=COL_PIN_6)

KEY_TAB = BaseKey(keycode=Keycode.TAB, row_pin=ROW_PIN_3, col_pin=COL_PIN_1)
KEY_Q = BaseKey(keycode=Keycode.Q, row_pin=ROW_PIN_3, col_pin=COL_PIN_2)
KEY_W = BaseKey(keycode=Keycode.W, row_pin=ROW_PIN_2, col_pin=COL_PIN_3)
KEY_E = BaseKey(keycode=Keycode.E, row_pin=ROW_PIN_2, col_pin=COL_PIN_4)
KEY_R = BaseKey(keycode=Keycode.R, row_pin=ROW_PIN_2, col_pin=COL_PIN_5)
KEY_T = BaseKey(keycode=Keycode.T, row_pin=ROW_PIN_2, col_pin=COL_PIN_6)

KEY_CAPS_LOCK = BaseKey(keycode=Keycode.CAPS_LOCK, row_pin=ROW_PIN_4, col_pin=COL_PIN_1)
KEY_A = BaseKey(keycode=Keycode.A, row_pin=ROW_PIN_4, col_pin=COL_PIN_2)
KEY_S = BaseKey(keycode=Keycode.S, row_pin=ROW_PIN_3, col_pin=COL_PIN_3)
KEY_D = BaseKey(keycode=Keycode.D, row_pin=ROW_PIN_3, col_pin=COL_PIN_4)
KEY_F = BaseKey(keycode=Keycode.F, row_pin=ROW_PIN_3, col_pin=COL_PIN_5)
KEY_G = BaseKey(keycode=Keycode.G, row_pin=ROW_PIN_3, col_pin=COL_PIN_6)

KEY_SHIFT = BaseKey(keycode=Keycode.SHIFT, row_pin=ROW_PIN_5, col_pin=COL_PIN_1)
KEY_Z = BaseKey(keycode=Keycode.Z, row_pin=ROW_PIN_6, col_pin=COL_PIN_2)
KEY_X = BaseKey(keycode=Keycode.X, row_pin=ROW_PIN_4, col_pin=COL_PIN_3)
KEY_C = BaseKey(keycode=Keycode.C, row_pin=ROW_PIN_4, col_pin=COL_PIN_4)
KEY_V = BaseKey(keycode=Keycode.V, row_pin=ROW_PIN_4, col_pin=COL_PIN_5)
KEY_B = BaseKey(keycode=Keycode.B, row_pin=ROW_PIN_4, col_pin=COL_PIN_6)

KEY_LEFT_SHIFT = BaseKey(keycode=Keycode.LEFT_SHIFT, row_pin=ROW_PIN_5, col_pin=COL_PIN_7)
KEY_LEFT_CONTROL = BaseKey(keycode=Keycode.LEFT_CONTROL, row_pin=ROW_PIN_5, col_pin=COL_PIN_8)
KEY_LEFT_SUPER = BaseKey(keycode=Keycode.GUI, row_pin=ROW_PIN_5, col_pin=COL_PIN_9)
KEY_LEFT_ALT = BaseKey(keycode=Keycode.LEFT_ALT, row_pin=ROW_PIN_5, col_pin=COL_PIN_10)

KEY_SPACE = BaseKey(keycode=Keycode.SPACE, row_pin=ROW_PIN_5, col_pin=COL_PIN_6)

LEFT_KEYS = [
    KEY_BACKTICK, KEY_ONE, KEY_TWO, KEY_THREE, KEY_FOUR, KEY_FIVE,
    KEY_TAB, KEY_Q, KEY_W, KEY_E, KEY_R, KEY_T,
    KEY_CAPS_LOCK, KEY_A, KEY_S, KEY_D, KEY_F, KEY_G,
    KEY_SHIFT, KEY_Z, KEY_X, KEY_C, KEY_V, KEY_B,
    KEY_LEFT_SHIFT, KEY_LEFT_CONTROL, KEY_LEFT_SUPER,
    # KEY_LEFT_SHIFT, KEY_LEFT_CONTROL, KEY_LEFT_SUPER, KEY_LEFT_ALT,
    KEY_SPACE,
]
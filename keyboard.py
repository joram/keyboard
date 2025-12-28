import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard as HIDKeyboard
from keys_right import VARIABLE_NAMES

DIOS = {}


class KeyboardRow():

    def __init__(self, row_pin, keys):
        self.keys = keys
        self.row_pin = row_pin
        self.row_dio = digitalio.DigitalInOut(row_pin)
        self.row_dio.direction = digitalio.Direction.OUTPUT
        self.row_dio.value = True


    def find_pressed_keys(self):
        # Set row LOW to activate it
        self.row_dio.value = False
        # Small delay to allow signal to stabilize
        time.sleep(0.0001)

        # Read all column states while row is LOW
        # Store states first to ensure atomic reading
        col_states = {}
        for key in self.keys:
            col_states[key] = key.col_dio.value
        
        # Now process the states
        for key, col_state in col_states.items():
            # Column reads LOW (False) when key is pressed (row LOW + key pressed = column LOW)
            if not col_state:  # Only check if column is LOW
                key.check_pressed_state(col_state)

        # Set row HIGH to deactivate it
        self.row_dio.value = True
        # Small delay to ensure row is fully HIGH before next scan
        time.sleep(0.01)


class Keyboard():

    def __init__(self, keys):
        keys_by_row = {}
        for key in keys:
            if key.row_pin not in keys_by_row:
                keys_by_row[key.row_pin] = []
            keys_by_row[key.row_pin].append(key)
        self.rows = [KeyboardRow(row_pin, keys) for row_pin in keys_by_row]
        
        # Column pins are already initialized by BaseKey._get_dio() when keys are created
        # No need to initialize them again here


    def run(self):
        while True:
            # Ensure all rows start HIGH before scanning
            for row in self.rows:
                row.row_dio.value = True

            # find pressed keys
            for row in self.rows:
                row.find_pressed_keys()

            # wait for a short time
            time.sleep(0.01)
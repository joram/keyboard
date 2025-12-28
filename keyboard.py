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
        self.row_dio.value = False

        for key in self.keys:
            if not key.col_dio.value:                
                key.check_pressed_state()

        self.row_dio.value = True


class Keyboard():

    def __init__(self, keys):
        keys_by_row = {}
        for key in keys:
            if key.row_pin not in keys_by_row:
                keys_by_row[key.row_pin] = []
            keys_by_row[key.row_pin].append(key)
        self.rows = [KeyboardRow(row_pin, keys) for row_pin in keys_by_row]

        # init all the pins
        col_pins = set([key.col_pin for key in keys])
        row_pins = set([key.row_pin for key in keys])

        for col_pin in col_pins:
            try:
                col_dio = digitalio.DigitalInOut(col_pin)
                col_dio.direction = digitalio.Direction.INPUT
                col_dio.pull = digitalio.Pull.UP
            except Exception as e:
                print(f"ERROR: Failed to initialize col pin {col_pin}: {e}")


    def run(self):
        while True:

            # pull down all rows
            for row in self.rows:
                row.row_dio.value = False

            # find pressed keys
            for row in self.rows:
                row.find_pressed_keys()

            # wait for a short time
            time.sleep(0.01)
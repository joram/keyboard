import time
import board
import digitalio
import usb_hid
from keys_right import VARIABLE_NAMES

DIOS = {}

def init_row_pin(pin):
    if pin in DIOS:
        return DIOS[pin]
    try:
        dio = digitalio.DigitalInOut(pin)
        DIOS[pin] = dio
        dio.direction = digitalio.Direction.OUTPUT
        dio.value = True
        return dio
    except Exception as e:
        pin_name = VARIABLE_NAMES.get(pin, str(pin))
        print(f"ERROR: Failed to initialize row pin {pin_name}: {e}")
        raise

def init_col_pin(pin):
    if pin in DIOS:
        return DIOS[pin]
    dio = digitalio.DigitalInOut(pin)
    DIOS[pin] = dio
    dio.direction = digitalio.Direction.INPUT
    dio.pull = digitalio.Pull.UP
    return dio

class Keyboard():

    def __init__(self, keys):
        print(f"Initializing keyboard with {len(keys)} keys...")
        self.keys = keys
        self.PIN_MAP = {}
        self.ROW_PINS = []
        self.COL_PINS = []
        self.ALL_PINS = []
        self.CURR_KEY_STATES = {}

        
        # Initialize digital I/O for all pins
        for key in keys:
            try:
                row_dio = init_row_pin(key.row_pin) # Configure row pin as output (will drive low)
                col_dio = init_col_pin(key.col_pin) # Configure col pin as input with pull-up
            except Exception as e:
                row_name = VARIABLE_NAMES.get(key.row_pin, str(key.row_pin))
                col_name = VARIABLE_NAMES.get(key.col_pin, str(key.col_pin))
                print(f"ERROR initializing key {key.name} (row: {row_name}, col: {col_name}): {e}")
                raise
            
            # Store the digitalio objects
            key.row_dio = row_dio
            key.col_dio = col_dio
            
            # Track unique pins
            if key.row_pin not in self.ROW_PINS:
                self.ROW_PINS.append(key.row_pin)
            if key.col_pin not in self.COL_PINS:
                self.COL_PINS.append(key.col_pin)
            if key.row_pin not in self.ALL_PINS:
                self.ALL_PINS.append(key.row_pin)
            if key.col_pin not in self.ALL_PINS:
                self.ALL_PINS.append(key.col_pin)
            
            # Map coordinate to key
            coord = (key.row_pin, key.col_pin)
            self.PIN_MAP[coord] = key
            self.CURR_KEY_STATES[key] = False

        print(f"Keyboard initialized. Rows: {len(self.ROW_PINS)}, Cols: {len(self.COL_PINS)}")
    def run(self):

        while True:
            self.tick()
            time.sleep(0.01)
        
    def tick(self):
        # Scan matrix: drive each row low, check columns
        for row_pin in self.ROW_PINS:
            try:
                row_dio = init_row_pin(row_pin)
                row_var_name = VARIABLE_NAMES.get(row_pin, str(row_pin))
                
                # Debug: Check if we can set the pin
                row_dio.value = False
                time.sleep(0.001)
                
                for col_pin in self.COL_PINS:
                    col_dio = init_col_pin(col_pin)
                    key_pressed = not col_dio.value
                    key = self.PIN_MAP.get((row_pin, col_pin))
                    if key is None:
                        if key_pressed:
                            col_var_name = VARIABLE_NAMES.get(col_pin, str(col_pin))
                            print(f"Key not found: {row_var_name}, {col_var_name}")
                        continue

                    if key_pressed and not self.CURR_KEY_STATES.get(key):
                        key.keypress()
                        self.CURR_KEY_STATES[key] = True
                    elif not key_pressed and self.CURR_KEY_STATES.get(key):
                        key.keyrelease()
                        self.CURR_KEY_STATES[key] = False
                
                row_dio.value = True
            except Exception as e:
                row_var_name = VARIABLE_NAMES.get(row_pin, str(row_pin))
                print(f"Error scanning row {row_var_name}: {e}")
                # Try to recover by setting pin back to high
                try:
                    if row_pin in DIOS:
                        DIOS[row_pin].value = True
                except:
                    pass
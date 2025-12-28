from keyboard import Keyboard
from keys_right import RIGHT_KEYS
from keys_left import LEFT_KEYS

def get_keys():
    SIDE = "right"
    with open(".env", "r") as f:
        for line in f:
            if line.startswith("KEYBOARD_SIDE="):
                SIDE = line.split("=")[1].strip()
    if SIDE == "right":
        return RIGHT_KEYS
    elif SIDE == "left":
        return LEFT_KEYS

    raise ValueError(f"Invalid side: {SIDE}. Must be 'right' or 'left'. \nYou can set the side in the .env file, with the KEYBOARD_SIDE variable.")



print("=" * 40)
print("KB2040 Keyboard Starting...")
print("=" * 40)
try:
    keyboard = Keyboard(keys=get_keys())
    keyboard.run()
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exception(e)

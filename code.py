from keyboard import Keyboard
from keys import RIGHT_KEYS

print("=" * 40)
print("KB2040 Keyboard Starting...")
print("=" * 40)
try:
    keyboard = Keyboard(keys=RIGHT_KEYS)
    print("Entering main loop...")
    keyboard.run()
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exception(e)
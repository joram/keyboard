import board

print("=" * 50)
print("Available pins in board module:")
print("=" * 50)

# Get all attributes that look like pins
pin_names = []
for attr_name in dir(board):
    # Filter for GPIO pins (GP0, GP1, etc.) and other common pin names
    if not attr_name.startswith('_'):
        try:
            pin_obj = getattr(board, attr_name)
            # Check if it's a pin-like object
            if hasattr(pin_obj, 'id') or 'GP' in attr_name or 'A' in attr_name or 'D' in attr_name:
                pin_names.append(attr_name)
        except:
            pass

# Sort and print
pin_names.sort()
for name in pin_names:
    try:
        pin = getattr(board, name)
        pin_id = getattr(pin, 'id', 'N/A')
        print(f"  {name:20s} -> {pin_id}")
    except:
        print(f"  {name:20s} -> (error accessing)")

print("\n" + "=" * 50)
print("GPIO pins (GP0-GP29):")
print("=" * 50)

# Try to list GP0 through GP29
for i in range(30):
    pin_name = f"GP{i}"
    try:
        pin = getattr(board, pin_name)
        pin_id = getattr(pin, 'id', 'N/A')
        print(f"  {pin_name:10s} -> {pin_id}")
    except AttributeError:
        pass  # Pin doesn't exist
    except Exception as e:
        print(f"  {pin_name:10s} -> Error: {e}")


import serial
import re
import vgamepad as vg
from evdev import uinput, ecodes as e
# Button mappings
button_map = {
    "A": vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
    "B": vg.XUSB_BUTTON.XUSB_GAMEPAD_B,
    "X": vg.XUSB_BUTTON.XUSB_GAMEPAD_X,
    "Y": vg.XUSB_BUTTON.XUSB_GAMEPAD_Y,
    "UP": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP,
    "DOWN": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN,
    "LEFT": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,
    "RIGHT": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT,
    "START": vg.XUSB_BUTTON.XUSB_GAMEPAD_START,
    "Z": vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER,
    "START": vg.XUSB_BUTTON.XUSB_GAMEPAD_START,
}

# Keyboard mappings
keyboard_map = {
    "A": e.KEY_A,
    "B": e.KEY_B,
    "X": e.KEY_X,
    "Y": e.KEY_Y,
    "UP": e.KEY_UP,
    "DOWN": e.KEY_DOWN,
    "LEFT": e.KEY_LEFT,
    "RIGHT": e.KEY_RIGHT,
    "START": e.KEY_ENTER,
    "L": e.KEY_L,
    "R": e.KEY_R,
    "Z": e.KEY_Z,
}


def parse_controller_data(data_string):
    global e
    """Parses the controller data string and returns a dictionary of values."""
    pattern = re.compile(
        r"A:(?P<A>\d+) B:(?P<B>\d+) X:(?P<X>\d+) Y:(?P<Y>\d+) UP:(?P<UP>\d+) DOWN:(?P<DOWN>\d+) LEFT:(?P<LEFT>\d+) RIGHT:(?P<RIGHT>\d+) START:(?P<START>\d+) Z:(?P<Z>\d+) L:(?P<L>\d+) R:(?P<R>\d+) LEFT_X:(?P<LEFT_X>\d+) LEFT_Y:(?P<LEFT_Y>\d+) RIGHT_X:(?P<RIGHT_X>\d+) RIGHT_Y:(?P<RIGHT_Y>\d+) TRIGGER_L:(?P<TRIGGER_L>\d+) TRIGGER_R:(?P<TRIGGER_R>\d+)"
    )
    match = pattern.match(data_string)
    if match:
        return {k: int(v) for k, v in match.groupdict().items()}
    else:
        return None

def convert_to_gamepad_values(data: int):

    return int((data - 2048) * 32767 / 2048)

def read_serial_data(port, e, baudrate=115200):
    """Reads data from the serial port and parses it."""
    try:
        ser = serial.Serial(port, baudrate)
        print(f"Connected to {port} at {baudrate} baud")
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        return

    try:
        while True:
            line = ser.readline().decode('utf-8').strip()
            if line:
                data = parse_controller_data(line)
                if data:
                    

                    # Iterate through the button map and update the gamepad state
                    for button_name, button_code in button_map.items():
                        if button_name not in data:
                            continue
                        if data[button_name] == 1:
                            gamepad.press_button(button_code)
                        else:
                            gamepad.release_button(button_code)

                    # Update the joysticks
                    gamepad.left_joystick(x_value=convert_to_gamepad_values(data["LEFT_X"]), y_value=convert_to_gamepad_values(data["LEFT_Y"]))
                    gamepad.right_joystick(x_value=convert_to_gamepad_values(data["RIGHT_X"]), y_value=convert_to_gamepad_values(data["RIGHT_Y"]))
                    gamepad.left_trigger(value=int(data["TRIGGER_L"] / 16))
                    gamepad.right_trigger(value=int(data["TRIGGER_R"] / 16))

                    # Update the gamepad
                    gamepad.update()

                    
                    for button_name, button_code in keyboard_map.items():
                        if button_name not in data:
                            continue
                        if data[button_name] == 1:
                            ui.write(e.EV_KEY, button_code, 1)
                        else:
                            ui.write(e.EV_KEY, button_code, 0)
                    
                    if data["LEFT_X"] > 3000:
                        ui.write(e.EV_KEY, e.KEY_D, 1)
                    else: 
                        ui.write(e.EV_KEY, e.KEY_D, 0)
                    if data["LEFT_X"] < 1000:
                        ui.write(e.EV_KEY, e.KEY_A, 1)
                    else:
                        ui.write(e.EV_KEY, e.KEY_A, 0)
                    if data["LEFT_Y"] > 3000:
                        ui.write(e.EV_KEY, e.KEY_S, 1)
                    else:
                        ui.write(e.EV_KEY, e.KEY_S, 0)
                    if data["LEFT_Y"] < 1000:
                        ui.write(e.EV_KEY, e.KEY_W, 1)
                    else:
                        ui.write(e.EV_KEY, e.KEY_W, 0)
                    
                    ui.syn()






                else:
                    print(f"Failed to parse line: {line}")
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        ser.close()
        print("Serial port closed.")

if __name__ == "__main__":
    gamepad = vg.VX360Gamepad()
    ui = uinput.UInput()
    serial_port = "/dev/ttyUSB0"  # Replace with your serial port
    read_serial_data(serial_port, e)

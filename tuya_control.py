from colorama import Fore, Style, init
from tuya_connector import TuyaOpenAPI
from dotenv import load_dotenv
import time
import os

# Initialize colorama for colored output
init(autoreset=True)

# Load environment variables from .env file
load_dotenv()

# Replace these with your actual details (from .env)
ENDPOINT = os.getenv("ENDPOINT")
ACCESS_ID = os.getenv("ACCESS_ID")
ACCESS_KEY = os.getenv("ACCESS_KEY")

# Initialize Tuya Cloud API
openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()

def fetch_devices():
    # Fetch devices from the linked app account
    response = openapi.get('/v1.0/iot-01/associated-users/devices')  # API endpoint for app-linked devices
    if response.get('success'):
        return response.get('result').get('devices', [])  # Return the list of devices
    return []


# Cool introduction
def intro():
    print(Fore.GREEN + """
          
          
          
      ╔══════════════════════════════════════╗
      ║                                      ║
      ║          P O W E R  S Y N C          ║
      ║                                      ║
      ║        Powered by: dendycodes        ║
      ║                                      ║
      ╚══════════════════════════════════════╝
    """ + Style.RESET_ALL)
    print(Fore.GREEN + ">> Welcome to PowerSync <<" + Style.RESET_ALL)

# Display the list of devices in a cool format
def display_devices(devices):
    if not devices:
        print(Fore.RED + ">> No devices found." + Style.RESET_ALL)
        return
    print(Fore.CYAN + ">> Available Devices:" + Style.RESET_ALL)
    for index, device in enumerate(devices, start=1):
        print(Fore.YELLOW + f"[{index}] {device['name']} (ID: {device['id']})" + Style.RESET_ALL)


# Command to toggle the device ON or OFF
def toggle_device(device_id, turn_on):
    commands = {'commands': [{'code': 'switch_1', 'value': turn_on}]}
    response = openapi.post(f'/v1.0/devices/{device_id}/commands', commands)
    return response

# Main function to toggle the device and add exit option
def cli():
    intro()
    devices = fetch_devices()
    display_devices(devices)

    if not devices:
        print(Fore.RED + ">> No devices available for control. Exiting..." + Style.RESET_ALL)
        return

    # Select a device from the list by number
    while True:
        try:
            device_index = int(input(Fore.CYAN + ">> Select a device number to control: " + Style.RESET_ALL))
            if 1 <= device_index <= len(devices):
                selected_device = devices[device_index - 1]
                break
            else:
                print(Fore.RED + ">> Invalid device number. Try again." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + ">> Please enter a valid number." + Style.RESET_ALL)

    print(Fore.GREEN + f">> You have selected {selected_device['name']}" + Style.RESET_ALL)

    # Toggle light for the selected device
    flag = True
    while True:
        user_input = input(Fore.CYAN + ">> Press [Enter] to toggle the lights (ON/OFF), or 'Q' to quit: " + Style.RESET_ALL)
        
        if user_input.lower() == 'q':  # Exit the loop when 'Q' or 'q' is pressed
            print(Fore.RED + ">> Exiting the console..." + Style.RESET_ALL)
            break

        flag = not flag
        status = "ON" if flag else "OFF"
        print(Fore.YELLOW + f">> Turning lights {status}..." + Style.RESET_ALL)
        response = toggle_device(selected_device['id'], flag)
        if response.get('success'):
            print(Fore.GREEN + f">> Lights are now {status}" + Style.RESET_ALL)
        else:
            print(Fore.RED + ">> Failed to control lights" + Style.RESET_ALL)
        time.sleep(1)

if __name__ == '__main__':
    cli()

from colorama import Fore, Style, init
from tuya_connector import TuyaOpenAPI
import time
import os
from dotenv import load_dotenv

# Initialize colorama for colored output
init(autoreset=True)

# Load environment variables from .env file
load_dotenv()

# Replace these with your actual details (from .env)
ENDPOINT = os.getenv("ENDPOINT")
ACCESS_ID = os.getenv("ACCESS_ID")
ACCESS_KEY = os.getenv("ACCESS_KEY")
DEVICE_ID = os.getenv("DEVICE_ID")

# Initialize Tuya Cloud API
openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()

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

# Command to toggle the device ON or OFF
def toggle_device(turn_on):
    commands = {'commands': [{'code': 'switch_1', 'value': turn_on}]}
    response = openapi.post(f'/v1.0/devices/{DEVICE_ID}/commands', commands)
    return response

# Main function to toggle the device and add exit option
def cli():
    intro()
    flag = True
    while True:
        user_input = input(Fore.CYAN + ">> Press [Enter] to toggle the lights (ON/OFF), or 'Q' to quit: " + Style.RESET_ALL)
        
        if user_input.lower() == 'q':  # Exit the loop when 'Q' or 'q' is pressed
            print(Fore.RED + ">> Exiting the console..." + Style.RESET_ALL)
            break

        flag = not flag
        status = "ON" if flag else "OFF"
        print(Fore.YELLOW + f">> Turning lights {status}..." + Style.RESET_ALL)
        response = toggle_device(flag)
        if response.get('success'):
            print(Fore.GREEN + f">> Lights are now {status}" + Style.RESET_ALL)
        else:
            print(Fore.RED + ">> Failed to control lights" + Style.RESET_ALL)
        time.sleep(1)

if __name__ == '__main__':
    cli()

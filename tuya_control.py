from colorama import Fore, Style, init
from tuya_connector import TuyaOpenAPI
import time

# Initialize colorama for colored output
init(autoreset=True)

# Replace these with your actual details
ENDPOINT = "" 
ACCESS_ID = ""
ACCESS_KEY = ""  
DEVICE_ID = "" 


# Initialize Tuya Cloud API
openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()

def hacker_intro():
    print(Fore.GREEN + """
          
          
          
      ╔══════════════════════════════════════╗
      ║                                      ║
      ║         D E N D Y  C O D E S         ║
      ║                                      ║
      ╚══════════════════════════════════════╝
    """ + Style.RESET_ALL)
    print(Fore.GREEN + ">> Welcome to Dendys Console <<" + Style.RESET_ALL)

# Command to toggle the device ON or OFF
def toggle_device(turn_on):
    commands = {'commands': [{'code': 'switch_1', 'value': turn_on}]}
    response = openapi.post(f'/v1.0/devices/{DEVICE_ID}/commands', commands)
    return response

# Main function to toggle the device
def hacker_ui():
    hacker_intro()
    flag = True
    while True:
        input(Fore.CYAN + ">> Press [Enter] to toggle the lights (ON/OFF)" + Style.RESET_ALL)
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
    hacker_ui()
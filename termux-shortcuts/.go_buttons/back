import os
import getpass
import socket
import time
#from tqdm import tqdm

def get_user_name():
  """Get termux username for ssh command string"""
  username = getpass.getuser()
  return username

def get_local_ip():
    """Get the local IP address by connecting to a public server."""
    s = None
    try:
        # Create a temporary socket to a known external address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Connects to Google's public DNS server
        local_ip = s.getsockname()[0]
        return local_ip
    except socket.error:
        return "127.0.0.1"  # Fallback to loopback address if no connection
    finally:
        if s:
            s.close()

#print(f"Local IP address: {get_local_ip()}")


# start sshd
os.system("sshd")

# create ssh into me command
cmnd=f"ssh -p 8022 {get_user_name()}@{get_local_ip()}"

# post ssh running notification with command
os.system(f"termux-toast \"starting ssh\"")
os.system(f"termux-notification -c \"{cmnd}\" -t \"ssh\"")

# print out instructions and command
os.system("clear")
print("copy the ssh command below into Google Keep")
print(f"\n\n\n\n\n    {cmnd}\n\n\n\n\n")

# for i in tqdm(range(100)):
#     time.sleep(0.09)  
#     # Simulating a task

# pause until enter
pause = input("press Enter to open keep.")

# open google keep
os.system("am start -n com.google.android.keep/com.google.android.apps.keep.ui.activities.BrowseActivity")
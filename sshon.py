import os
import getpass
import socket
import time

def get_user_name():
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

cmnd=f"ssh -p 8022 {get_user_name()}@{get_local_ip()}"
os.system(f"termux-notification -c \"{cmnd}\" -t \"ssh\"")


print(f"\n\n\n\n\n      {cmnd}\n\n\n\n\n")
time.sleep(9)
os.system("am start -n com.google.android.keep/com.google.android.apps.keep.ui.activities.BrowseActivity")

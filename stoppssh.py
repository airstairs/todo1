import subprocess

def create_tmux_session_and_send_command(session_name, command):
    """
    Starts a new named tmux session and sends a command to it.

    Args:
        session_name (str): The name for the new tmux session.
        command (str): The shell command to send to the session.
    """
    try:
        # Start a new detached and named tmux session
        subprocess.run(['tmux', 'new-session', '-d', '-s', session_name], check=True)
        print(f"Successfully started new tmux session: {session_name}")

        # Send the command and press Enter (C-m)
        subprocess.run(['tmux', 'send-keys', '-t', session_name, command, 'C-m'], check=True)
        print(f"Successfully sent command to session {session_name}: '{command}'")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing a tmux command: {e}")
    except FileNotFoundError:
        print("Error: 'tmux' command not found. Please ensure tmux is installed and in your PATH.")

if __name__ == "__main__":
    # Define the session name and the echo command
    my_session_name = "my_new_session"
    my_command = "echo 'Hello from Python!'"

    # Run the function
    create_tmux_session_and_send_command(my_session_name, my_command)

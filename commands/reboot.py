import os
import sys

def command(input_value, thread_userid=None):
    config = {"name": "reboot", "version": "1.0.0", "description": "Restart the Python bot or server.", "credits": "Kenneth Panio", "cooldown": "2"}

    if input_value.startswith(config['name']):
        response = restart_bot()
        return {'messages': [response]}
    else:
        return {'messages': [f"Default option in {config['name']}: {config['description']}"]}

def restart_bot():
    response = "Preparing for reboot...\n"

    try:
        # Add cleanup/preparation logic here

        python_executable = sys.executable
        os.execl(python_executable, python_executable, *sys.argv)
    except Exception as e:
        response += f"Error during reboot: {str(e)}"
    else:
        response += "Rebooting..."
    
    return response

def command(input_value, thread_userid=None):
    config = {
        "name": "link",
        "version": "1.0.0",
        "description": "Testing Only.",
        "credits": "Kenneth Panio",
        "cooldown": "1"
    }
    if input_value == "__config__":
        return config
    elif input_value.startswith(config['name'] + ' ') or input_value == config['name']: 
    	return {'messages': ["Ugh!"], 'image': ['https://i.imgur.com/m7iPAc3.gif']}
    else:
        return {'messages': [f"Default option in {config['name']}: {config['description']}"]}

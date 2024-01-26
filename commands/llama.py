def command(input_value, thread_userid=None):
    import requests
    config = {
        "name": "llm",
        "version": "0.0.1",
        "description": "ask anything to llama.AI🦙",
        "credits": "Kenneth panio", #credits api owner aliester crowley
        "cooldown": "2"
    }
    if input_value == "__config__":
        return config
    elif input_value.startswith(config['name']):
        try:
            ask = input_value[len(config['name']):].strip()
            ask2 = requests.get('https://llama.aliestercrowley.com/api?prompt=' + ask).json()['response']
            return {"messages": [f"𝙰𝙸 𝚁𝙴𝚂𝙿𝙾𝙽𝙳: \n{ask2}"]}
        except:
            return {"messages": ["❌𝚂𝙾𝚁𝚁𝚈, 𝚆𝙴 𝙰𝚁𝙴 𝙷𝙰𝚅𝙸𝙽𝙶 𝙴𝚁𝚁𝙾𝚁 𝙵𝙴𝚃𝙲𝙷𝙸𝙽𝙶 𝚁𝙴𝚂𝙿𝙾𝙽𝙳."]}
    else:
        return {'messages': [f"Default option in {config['name']}: {config['description']}"]}

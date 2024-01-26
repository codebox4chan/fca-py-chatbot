def command(input_value, thread_userid=None):
    import requests
    import re 
    config = {
        "name": "tempmail",
        "version": "1.0.0",
        "description": "Create tempmail",
        "credits": "Mahiro chan",
        "cooldown": "2"
    }
    TEMP_MAIL_URL = 'https://kazumaoff-peachwings.replit.app/api/gen'
    if input_value == "__config__":
        return config
    elif input_value.startswith(config['name']):
        argument = input_value[len(config['name']):].strip()
        if argument != '':
        	try:
        		pattern = r"<style([\s\S]*?)<\/style>|<script([\s\S]*?)<\/script>|<\/div>|<div>|<[^>]*>"
        		inboxResponse = requests.get('https://scp-09.onrender.com/api/getmessage/{}'.format(argument)).json()
        		reply = "📬 Inbox Messages: 📬\n\n" + "\n".join([f"📩 Sender: {x['sender']}\n👀 Subject: {x['subject']}\n📩 Message: {re.sub(pattern, '', x['message'])}\n" for x in inboxResponse['messages']])
        		return {'messages': [str(reply)]}
        	except:
        		return {'messages': [str(inboxResponse['error'])]}
        else:
        	tempMailData = requests.get(TEMP_MAIL_URL).json()['email']
        	return {'messages': [f'📩 Here\'s your generated temporary email: {tempMailData}']}
    else:
        return {'messages': [f"Default option in {config['name']}: {config['description']}"]}
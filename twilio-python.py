TWILIO_ACCOUNT_SID='AC3676babff03b01b63f57c21aac5ee280'
TWILIO_AUTH_TOKEN='59f6fd8a0f4921c1dcb2b8a4dc666d08'

from twilio.rest import Client
import requests as http
import json
from apscheduler.schedulers.blocking import BlockingScheduler

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
client = Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)

# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'
# replace this number with your own WhatsApp Messaging number
to_whatsapp_number='whatsapp:+917898812907'

def send_message():
    response = http.get("https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=230ead3e8d9da0f3c429")
    client.messages.create(body='Hi currency price is: {}'.format(json.loads(response.text)['USD_INR']),
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)

scheduler = BlockingScheduler()
scheduler.add_job(send_message, 'interval', hours=6)
scheduler.start()

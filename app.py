#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 15:57:57 2018

@author: abdulliaqat
"""
    
        # /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    account_sid = "ACa55a95ee55c5b213f6b6430df33fa845"
    auth_token = "576888fcc67b7059b5d0b2ad1a5d0199"
    client = Client(account_sid, auth_token)
    print('message received')
    sms=client.messages.list(to="+33644603688")
    text_body=client.messages(str(sms[1]).split('sid=')[2].split('>')[0]).fetch().body
    print(text_body)
        # Start our response
    resp = MessagingResponse()  

    if(text_body=='Hi' or text_body=='hi'or text_body=='help'or text_body=='Help'or text_body=='Hi'or text_body=='hi 'or text_body=='I need help' or text_body=='I need help '):
            # Add a message
            resp.message("Please visit ICLA-NRC.com or download ICLA-NRC app or send us your problem 1-Legal 2-Water 3-Shelter 4-Education 5-Food Security 6-Camp Management")
    else:
            resp.message("Please share information on: 1- Where are you from? 2- Where are you now 3- How old are you? 4- What kind of help do you need?(Birth docs, Marriage docs, Passport, Land issue)")
    

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    
    
'''    
from twilio.rest import Client
# put your own credentials here
account_sid = "ACa55a95ee55c5b213f6b6430df33fa845"
auth_token = "576888fcc67b7059b5d0b2ad1a5d0199"
client = Client(account_sid, auth_token)
client.messages.create(
  to="+4917658674524",
  from_="+33644603688 ",
      body="Select one option: 1- Medical 2- Legal 3- Food")
'''
'''
from twilio.rest import Client

account_sid = "ACa55a95ee55c5b213f6b6430df33fa845"
auth_token = "576888fcc67b7059b5d0b2ad1a5d0199"
client = Client(account_sid, auth_token)
client.messages.list
sms=client.messages.list(to="+4917658674524",date_sent='2018-04-21')
text_body=client.messages(str(sms[-1]).split('sid=')[2].split('>')[0]).fetch().body
'''
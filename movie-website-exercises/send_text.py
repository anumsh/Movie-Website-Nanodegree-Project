from twilio.rest import TwilioRestClient
 
# Your Account sid and Auth Token from twilio.com/user/account
account_sid = "xxxxxxxxxxxxxxxxxxxxxx"
auth_token  = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(
    body="JMy name is John?",
    to="+1 6666666666",    # Replace with your phone number
    from_="+155555555555") # Replace with your Twilio number
print message.sid

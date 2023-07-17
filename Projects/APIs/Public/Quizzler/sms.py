from twilio.rest import Client
account_sid = 'AC222035ae968abee44869fbea553c35d8'
auth_token = '4a39bbc24f0634125f44d870f2fd5770'

client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hi there',
                              from_='+18643517625',
                              to='+9613006033'
                          )

print(message.sid)
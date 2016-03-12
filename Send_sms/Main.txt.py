__author__ = 'asee2278'
import twilio

from twilio.rest import TwilioRestClient

# put your own credentials here
ACCOUNT_SID = "AC72b94808df4448e5923b27258493df48"
AUTH_TOKEN = "1eec25c699b9376331f5799618b28719"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages.create(
	to="+13045047736",
	from_="+16814044918",
	body="Test message ",
)

print message.sid
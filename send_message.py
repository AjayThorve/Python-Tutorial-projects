from twilio.rest import TwilioRestClient

# To find these visit https://www.twilio.com/user/account
ACCOUNT_SID = "ACf01a8c11553b97d17a456e6d856e994e"
AUTH_TOKEN = "a563a226b4e96ffbb87cdc28d97feae4"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages.create(
    body="Hello World!",  # Message body, if any
    to="+16093692439",
    from_="+16094450347 ",
)
print message.sid
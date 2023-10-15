import pywhatkit as kit
import datetime

# Specify the recipient's phone number (including country code) and the message
# phone_number = '+1234567890'  # Replace with the recipient's phone number
# message = 'Hello, this is a test message.'
def send_single_message(phone_number,message):
    # Set the time when you want to send the message (hour and minute)
    now = datetime.datetime.now()
    hours = now.hour
    minutes = now.minute + 3  # Send the message 2 minutes from now

    # Send the message
    kit.sendwhatmsg(phone_number, message, hours, minutes)


send_single_message('+918800090122','Test message')




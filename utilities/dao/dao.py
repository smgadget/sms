# Import models
from myapp.models import SMSPhoneMessageRecords
from myapp.models import SMSServiceAudit


# function to send a sms text message to a phone number
def addNewRecipient(name, number, text, sender):
   print name + " " + str(number) + " " + text + " " + sender + "to be updated in db"
   bSuccess = False
 
    #Creating an entry in records model
   try:
	   PhoneMessageRecords = SMSPhoneMessageRecords(
	   name = name,
	   phonenumber = number,
	   message = text,
	   sender = sender
	   )

	   PhoneMessageRecords.save()
	   bSuccess = True
   except Exception as e:
	   print str(e)
	   bSuccess = False
   
   return bSuccess
    


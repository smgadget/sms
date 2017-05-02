# Import the SDK
import boto3
# init the sns boto3 client
client = boto3.client('sns')


# function to send a sms text message to a phone number
def sendSMSTo(name, number, text):
    
    strNumber = str(number)
    strText = text
    strMessageAttributes={
	    'AWS.SNS.SMS.SenderID': {
	      'DataType': 'String',
	      'StringValue': name   
	    }    
	  }
    print name + strNumber + text  
    strResult = ""
    bSuccess = False
    try:
	strResult = str(client.publish(PhoneNumber = strNumber, Message=strText, MessageAttributes = strMessageAttributes))

	bSuccess = True
    except Exception as e:
	strResult = str(e)
	bSuccess = False
    finally:
        print strResult
    return bSuccess
    


'''
*** app url ***
'''

from django.conf.urls import url
from myapp.views import editRecipient
from myapp.views import createUpdateRecipient
from myapp.views import crudops
from myapp.views import sendSMS
from myapp.views import bulkSMSService
from myapp.views import sendTheSMS


urlpatterns = [
    url(r'^addrecipient/$', editRecipient),
    url(r'^recipientadded/$', createUpdateRecipient, name = 'createupdaterecipient'),
    url(r'^send/$', sendSMS),
    url(r'^sent/$', sendTheSMS, name = 'sendthesms'),
    url(r'^bulk/$', bulkSMSService)
]

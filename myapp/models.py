# -*- coding: utf-8 -*-
'''
*** app models ***
'''
from __future__ import unicode_literals
from django.db import models

# SMS data model.
class SMSPhoneMessageRecords(models.Model):

   phonenumber = models.IntegerField()
   name = models.CharField(max_length = 20, blank = True)
   message = models.TextField(max_length = 50)
   sender = models.CharField(max_length = 20, blank = True)

   class Meta:
      db_table = "smsphonemessagerecords"

# SMS history model
class SMSServiceAudit(models.Model):

   datetime = models.DateTimeField(auto_now = True)
   phonenumber = models.IntegerField()
   message = models.CharField(max_length = 50)
   sender = models.CharField(max_length = 20, blank = True)

   class Meta:
      db_table = "smsserviceaudit"

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from notification.sms.sns_sms import sendSMSTo
from django.test import TestCase

# Create your tests here.
def testsms():
   sendSMSTo("Me", "+447588890008", "test12345")
   return

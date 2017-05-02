'''
 *** Project url ***
'''

from django.conf.urls import url, include
from django.contrib import admin

# put project url/include here
urlpatterns = [
   url(r'^admin/', admin.site.urls),
   url(r'^smsservice/', include('myapp.urls'))
]

from django.shortcuts import render
from django.http import HttpResponse
from graber.models import Department, Team, Employee, Community, Contribution
# use system-wide one, uncomment for debug purpose only
#import sys
#import os
#sys.path.append(os.path.abspath('./pygerrit'))

from requests.auth import HTTPDigestAuth
from pygerrit.rest import GerritRestAPI
from pygerrit import escape_string
from urllib import urlencode
import time
from requests import HTTPError

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def update(request):
    output=""
    for emp in Employee.objects.order_by('email'):
        output += '' + str('<h1>%s</h1>' % emp.name)
        for comm in Community.objects.order_by('name'):
            output += '<h2>%s</h2>' % comm.name
            #rest = GerritRestAPI(url='http://review.cyanogenmod.org/')
            rest = GerritRestAPI(url=comm.review_base)
            output += "%s<br/>\n" % emp.email
            query_url ="/changes/?q=owner:"+emp.email+"+status:merged"
            output +=  query_url  + "<br/>\n" 
            changes=''
            try:
                #proxies = {
                #    "http": "http://127.0.0.1:8087",
                #    "https": "https://127.0.0.1:8087",
                #}
                #changes = rest.get(query_url, proxies=proxies)
                changes = rest.get(query_url)
            except HTTPError as he:
                output += '' + str(he.message)
            output += time.strftime('%Y-%m-%d %H:%M:%S') + "==> %d changes<br/>\n" % len(changes)
            for change in changes:
                subject = str(change['subject'])
                name = str(change['owner']['name'])
                num =  str(change['_number'])
                q = Contribution.objects.filter(employee_id=emp,review_id=num, community_id=comm)
                if len(q) < 1:
                    cont = Contribution(employee_id=emp,review_id=num, community_id=comm)
                    cont.save()
                else:
                    continue
                output += "<br/>\n" 
                output += subject
                output += "<br/>\n" 
                output += comm.review_base + num
                output += "<br/>\n" 
    return HttpResponse(output)

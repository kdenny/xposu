# Django
# import time
from datetime import *
from django.views.generic import UpdateView, ListView
from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth import logout
from django.template import RequestContext, loader
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# Python
import simplejson as json
import requests
from pprint import pprint

from vigilante.models import *



def complain(bizname,address,city,ctype, value, odate, comments):


    curstore = Store.objects.filter(name=bizname)

    # q = Game.objects.filter(name=bizname)

    if len(curstore) == 0:
        ## Build game object
        store = Store()
        store.name = bizname
        store.address = address
        store.city = city
        store.save()

    curstore = Store.objects.filter(name=bizname,address=address)

    for cs in curstore:
        r = cs

    complaint_check = Complaint.objects.filter(store=bizname)

    if len(complaint_check) == 0:

        if not r.complaint_set.exists():

            complaint = r.complaint_set.create(type=ctype,
                                         value=value
                                         # date=odate,
                                         # comments=comments
                                               )

        else:
            complaint = Complaint()
            complaint.store = r
            complaint.type = ctype
            complaint.value = value
            # complaint.date = odate
            complaint.save()

            r.complaint_set.add(complaint)



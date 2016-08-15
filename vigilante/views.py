from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
# from vigilante import scripts
from vigilante.models import *

from scripts.yelp_query import search2, search
from scripts.makeComplaint import complain
from pprint import pprint




# Create your views here.

def index(request):
    # print "index: " + str(request.user)
    # data = {}
    placedata = {}
    if request.method == 'POST':

        if 'placesubmit' in request.POST:
            bizname = request.POST.get('bizname')
            city = str(request.POST.get('city'))
            state = str(request.POST.get('state'))

            if bizname != 'None' and str(city).strip() == '' and str(state).strip() == '':
                print(bizname)
                print(city)
                print(state)
                location = ''

            else:
                if state.strip() != '':
                    location = "{0}, {1}".format(city, state)
                else:
                    location = city
                yelpresult = search(bizname,location)
                pprint(yelpresult)

            placedata = { "places" : yelpresult}

            resp = placeresults(request, placedata)



        if 'complaintsubmit' in request.POST:
            ctype = str(request.POST.get('types'))
            pprint(ctype)
            bizname = str(request.POST.get('bizname'))
            address = str(request.POST.get('bizaddress'))
            city = str(request.POST.get('bizcity'))

            # print(address)
            if ctype == 'cardmin':
                value = float(request.POST.get('cardminval'))
            if ctype == 'highfee':
                value = float(request.POST.get('atmfeeval'))

            odate = str(request.POST.get('occdate'))

            comments = str(request.POST.get('comments'))

            if comments == 'None':
                comments = ''

            complain(bizname,address,city,ctype,value,odate,comments)

            resp = render_to_response('static/index.html', placedata, context_instance=RequestContext(request))


    else:

        resp = render_to_response('static/index.html', placedata, context_instance=RequestContext(request))



    # context = {'hello': 'world'}

    return resp



def placeresults(request, placedata):



    return render_to_response('static/placeresults.html', placedata, context_instance=RequestContext(request))



def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            # return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'vigilante/new_claim.html', {'form': form})

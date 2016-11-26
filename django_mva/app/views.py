from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from app.models import Artist,ArtistForm


# Create your views here.
def artists(request):
    #return #HttpResponse('<html><head><title>Hello, Django!</title></head><body><h1>Hello,Django</h1></body></html>')
    artists = Artist.objects.all()
    return render_to_response('app/artists.html', { 'artists':artists})

def artistdetails(request, id):
    artist = Artist.objects.get(pk=id)
    return render_to_response('app/artistdetails.html', {'artist': artist})

def create_artist(request):
    if request.method == "GET":
        form = ArtistForm()
        return render(request, 'app/create.html',{ 'form':form })
    elif request.method == "POST":
        form = ArtistForm(request.POST)
        form.save()
        return HttpResponseRedirect('/artists')
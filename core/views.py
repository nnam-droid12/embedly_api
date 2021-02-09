from django.shortcuts import render

# Create your views here.
#import django.conf.settings.EMBEDLY_KEY
import requests
from .forms import SubmitEmbed
from .serializers import EmbedSerializer

def save_embed(request):
    form = SubmitEmbed(request.POST)
    if request.method == "POST":
        form = SubmitEmbed(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            
            # Create the query
            #query = {
            #"url": "&url=" + url,
            #"key": ":f7b97d56ed584d65a513561ea3286bef"
            #}

            #Make the call.
            r = requests.get('https://api.embedly.com/1/oembed?key=f7b97d56ed584d65a513561ea3286bef' + '&url=' + url)
            json = r.json()
            # print the json result.
            #print (r.json())
            serializer = EmbedSerializer(data=json)
            if serializer.is_valid():
                embed = serializer.save()   
                return render(request, 'core/embed.html', {'embed':embed})
        else:
            form = SubmitEmbed()
    context = {
        'form':form
    }        
    return render (request, 'core/index.html', context)    



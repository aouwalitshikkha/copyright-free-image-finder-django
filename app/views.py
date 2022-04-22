from django.shortcuts import render
import requests
import json
# Create your views here.

def image_finder(q):
    q= q.replace(' ','+')
    api = 'Enter Your API Key Here'
    url = f'https://pixabay.com/api/?key={api}&q={q}&image_type=photo'
    response = requests.get(url)
    data = json.loads(response.text)
    images_data = data['hits']
    image_list = []
    for image in images_data:
        image_list.append(image['webformatURL'])
    return image_list




def index_view(request):
    if request.method =="GET" and 'q' in request.GET:
        q = request.GET.get('q')
        data = image_finder(q)
        context = {'data':data}
    else:
        context ={}
    template_name = "home.html"
    return render(request, template_name, context)
import json
from django.http import HttpResponse


def user(request, user_id):
    print user_id

    user = {'id':1,'name':'John','age':20,'gender':'Male'}
    
    return HttpResponse(json.dumps(user))  

def users(request):
    
    if request.method == 'POST':
        print request.POST
        print "is_ajax()" + str(request.is_ajax())
        
        response_dict = {'success' : True }
        return HttpResponse(json.dumps(response_dict), mimetype='application/javascript')
        
    user = {'id':1,'name':'John','age':20,'gender':'Male'}
    
    return HttpResponse(json.dumps(user))  

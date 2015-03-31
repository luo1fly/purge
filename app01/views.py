from django.shortcuts import render_to_response
from django.contrib import auth
from django.http import HttpResponse
from app01 import models
from datetime import datetime
from utils.sku import Product
import re
# Create your views here.

def index(request):
    return render_to_response('index.html')

def login(request):
    #print 'this is login view'
    return render_to_response('login.html')

def logout(request):
    auth.logout(request)
    return HttpResponse("<h4>You've just logged out! <a href='/login/'>click here</a> to relogin</h4>")

def user_login(request):
    username = request.POST['user']
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)
    userid = models.OptUser.objects.get(user__username=user)
    #print user,userid
    if user is not None: #and user.is_active:
            #correct password and user is marked "active"
            auth.login(request,user)
            models.OptUser.objects.filter(user__username=username).update(lst_login=datetime.now())
            return render_to_response('purge.html',{'userid':userid})
    else:
            return render_to_response('login.html',{'err':'wrong password'})
        
def purgesite(request,userid):
    usku = request.POST['skulist']
    optuser = models.OptUser.objects.get(id=userid)
    #print optuser
    sku = str(usku)
    if not sku:
        return render_to_response('purge.html',{'err':'please input at least one sku'})
    
    skulist = re.sub('\D',',',sku).split(',')
    invalidsku = []
    validsku = []
    for sku in skulist:
        Valid = re.match('^\d{6}$',sku)
        if not Valid:
            invalidsku.append(sku)
        else:
            validsku.append(sku)
    
    #if not invalidsku:
        
    result_dic = {}
    for sku in validsku:
        pro = Product(sku)
        if not pro.lst1:
            continue
        pro_dic = pro.clearCache(optuser)
        #print pro_dic
        result_dic.update(pro_dic)
        #return HttpResponse('validsku:'+str(validsku))
        
    return render_to_response('result.html',{'dicts':result_dic,'invalidsku':invalidsku})
    #else:
    #   return HttpResponse('invalid sku:'+str(invalidsku))
        
        #print skulist
        #return HttpResponse(skulist)
    

def forgot(request):
    return HttpResponse("<h4>please contact to administrator for help</h4>")
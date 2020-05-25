from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render,redirect
from .forms import ContactForm,LoginForm,RegisterForm
import requests
# api_token = 'O6o103ococlMmUiyZWHO'
api_token='0t4g4oYB5Mmzv3uJ18LB'
api_url_base = 'http://www.ije-api.tcore.xyz'
# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    contact_form =ContactForm(request.POST or None)
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, 'contact_page.html',{'form':contact_form})

def login_page(request):
    form=LoginForm(request.POST or None)
    context={'form':form}
    print('User logged in ')
    if form.is_valid():
        print(form.cleaned_data)
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
       # print(request.user.is_authenticated)
        if user is not None:
            #print(request.user.is_authenticated)
            login(request, user)
            # context['form']=LoginForm()
            # Redirect to a success page.
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            print('Error')
    return render(request,'login_page.html',context)

User=get_user_model()
def register_page(request):
    form=RegisterForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        print(form.cleaned_data)
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        email=form.cleaned_data.get('email')
        new_user=User.objects.create_user(username,password,email)
        print(new_user)
        context['form'] = RegisterForm()
    return render(request,'register_page.html',context)

def login_main(request):
    url = "{0}/v1/auth/login".format(api_url_base)

    payload = "{\n   \"header\" : {\n   \t\"cookie\" : \"\"\n   },\n    \"body\": {\n        \"email\": \"customer@travelportal.com\",\n        \"password\": \"customer\"\n    }\n}"
    headers = {
        'Content-Type': "application/json",
        'Accept': "application/json",
        'api_token': 'O6o103ococlMmUiyZWHO',
        'User-Agent': "PostmanRuntime/7.20.1",
        'Cache-Control': "no-cache",
        'Postman-Token': "7a4c337f-8f6c-4627-808e-d815b88a2ac1,5085609b-510f-4c12-b56f-03f18b90a744",
        'Host': "www.ije-api.tcore.xyz",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "140",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    print(response.json)
    return render(request,'login_page.html')

def logout(request):
    url = "{0}/v1/auth/logout".format(api_url_base)
    payload = ""
    headers = {
        'Authorization': "Bearer {0}".format(api_token),
        'Content-Type': "application/json",
        'User-Agent': "PostmanRuntime/7.20.1",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "19e128c0-8cdc-49aa-bdf7-b31963577957,f6fd6e37-af0b-4274-8e18-1388b8e5996d",
        'Host': "www.ije-api.tcore.xyz",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "0",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    return redirect('/')

def loading(request):
    return render(request, 'loading.html')
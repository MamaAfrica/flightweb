from django.shortcuts import render,redirect
from flight.forms import FlightDepartForm,FlightArriveForm
from .models import FlightDepartCode
import requests
api_token = '0t4g4oYB5Mmzv3uJ18LB'
api_url_base = 'http://www.ije-api.tcore.xyz'
# Create your views here.
def flightIndex(request):
    url = "{0}/v1/updates/update-countries".format(api_url_base)
    formD = FlightDepartForm()
    formA = FlightArriveForm()
    payload = ""
    headers = {
        'Content-Type': "application/json",
        'User-Agent': "PostmanRuntime/7.20.1",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "eecc774f-3fed-417a-afc8-6524caf45a03,f98e0bad-967c-4f0d-a8a1-0cde5cf131e4",
        'Host': "www.ije-api.tcore.xyz",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, data=payload, headers=headers)
    print(response.text)
    context = {'formD': formD,'formA':formA}
    return render(request,'flight-index-1.html',context)


def flightPayment(request):
    return render(request,'flight-payment-2.html')



# url = 'http://www.ije-api.tcore.xyz/v1/updates/update-countries'
#     payload = {}
#     headers = {}
#     response = requests.request('GET', url, headers=headers, data=payload, allow_redirects=False)
#     print(response.text)

# url = '{{url}}/v1/updates/update-airports'
# payload = {}
# headers = {}
# response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False, timeout=undefined, allow_redirects=false)
# print(response.text)
#

# url = '{{url}}/v1/updates/update-categories'
# payload = {}
# headers = {}
# response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False, timeout=undefined, allow_redirects=false)
# print(response.text)





# url = '{{url}}/v1/updates/update-airlines'
# payload = {}
# headers = {}
# response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False, timeout=undefined, allow_redirects=false)
# print(response.text)
#

# url = '{{url}}/v1/updates/update-airplanes'
# payload = {}
# headers = {}
# response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False, timeout=undefined, allow_redirects=false)
# print(response.text)
#

# url = '{{url}}/v1/updates/update-cities'
# payload = {}
# headers = {}
# response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False, timeout=undefined, allow_redirects=false)
# print(response.text)
#

# url = '{{url}}/v1/updates/update-states'
# payload = {}
# headers = {}
# response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False, timeout=undefined, allow_redirects=false)
# print(response.text)
#

# url = '{{url}}/v1/plugins/airports-type-ahead/unkown'
# payload = {}
# headers = {}
# response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False, timeout=undefined, allow_redirects=false)
# print(response.text)
#

# url = '{{url}}/v1/plugins/airlines-type-ahead/eminem'
# payload = {}
# headers = {}
# response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False, timeout=undefined, allow_redirects=false)
# print(response.text)
#

# url = '{{url}}/v1/plugins/cities-type-ahead/las'
# payload = {}
# headers = {}
# response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False, timeout=undefined, allow_redirects=false)
# print(response.text)
#
# #user reg

# url = '{{url}}/v1/auth/register'
# payload = "{\n    \"header\": {\n        \"\": \"\"\n    },\n    \"body\": {\n        \"users\": [\n            {\n                \"type\": \"agent\",\n                \"data\": {\n                    \"login_details\": {\n                        \"email\": \"apiagent@email.com\",\n                        \"password\": \"agentpassword\",\n                        \"password_confirmation\" : \"agentpasssword\"\n                    },\n                    \"profile_details\": {\n                        \"name\": \"API Agent\",\n                        \"address\": \"Somewhere on earth\",\n                        \"reg_number\": \"NHDB9127HD\",\n                        \"phone\": \"09090909090\",\n                        \"contact_person_name\": \"Agent Contact Person\",\n                        \"contact_person_email\": \"contactperson@email.com\",\n                        \"contact_person_phone\": \"0911911911\",\n                        \"contact_person_address\": \"Somewhere on earth\"\n                    }\n                }\n            },\n            {\n                \"type\": \"customer\",\n                \"data\": {\n                    \"login_details\": {\n                        \"email\": \"apicustomer@email.com\",\n                        \"password\": \"customerpassword\",\n                        \"password_confirmation\" : \"customerpassword\"\n                    },\n                    \"profile_details\": {\n                        \"title_id\": 1,\n                        \"gender_id\": 1,\n                        \"sur_name\": \"API\",\n                        \"first_name\": \"Customer\",\n                        \"other_name\": \"\",\n                        \"phone\": \"09092292299\",\n                        \"address\": \"Somewhere on earth\"\n                    }\n                }\n            }\n        ]\n    }\n}"
# headers = {
#   'Content-Type': 'application/json'
# }
# response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False, timeout=undefined, allow_redirects=false)
# print(response.text)
#
# #login

# url = '{{url}}/v1/auth/login'
# payload = "{\n    \"header\": {\n        \"cookie\": \"\"\n    },\n    \"body\": {\n        \"email\": \"admin@travelpro.com\",\n        \"password\": \"admin\"\n    }\n}"
# headers = {
#   'Content-Type': 'application/json',
#   'Accept': 'application/json'
# }
# response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False, timeout=undefined, allow_redirects=false)
# print(response.text)
#
# #api logout

# url = '{{url}}/v1/auth/logout'
# payload = {}
# headers = {
#   'Authorization': 'Bearer Cy67xXsMxmwPCjSH4zYQ'
# }
# response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False, timeout=undefined, allow_redirects=false)
# print(response.text)


from django.shortcuts import render,redirect
from flight.forms import FlightDepartForm,FlightArriveForm
from flights.models import FlightDepartCode
import requests
api_token = '0t4g4oYB5Mmzv3uJ18LB'
api_url_base = 'http://www.ije-api.tcore.xyz'

def flightResult(request):
    url = "{0}/v1/flight/search-flight".format(api_url_base)

    code = request.POST.get('code')
    arrive_code =request.POST.get('arrive_code')
    print(request.POST)
    if request.method =='POST':
        formD = FlightDepartForm(request.POST)
        formD.save()

    # form = FlightDepartForm()
    formD = FlightDepartForm()
    formA = FlightArriveForm()
    codes = FlightDepartCode.objects.all()
    flightDepartCode_data=[]

    # for code in codes:

    payload = "{\n    \"header\": {\n        \"cookie\": \"\"\n    },\n    \"body\": {\n        \"origin_destinations\": [\n            {\n                \"departure_city\": \"cod\",\n                \"destination_city\": \"arr\",\n                \"departure_date\": \"12/26/2020\",\n                \"return_date\": \"\"\n            }\n        ],\n        \"search_param\": {\n            \"no_of_adult\": 1,\n            \"no_of_child\": 1,\n            \"no_of_infant\": 1,\n            \"preferred_airline_code\" : \"\",\n            \"calendar\" : false,\n            \"cabin\": \"All\"\n        }\n    }\n}".replace("cod",code).replace("arr",arrive_code)
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer BijLBbGmGuV2hCSBtbne",
        'User-Agent': "PostmanRuntime/7.20.1",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "11e55a43-c722-470d-9e95-4f938a7733e2,599210e6-86eb-4eca-bd0e-4fde44bbfc64",
        'Host': "www.ije-api.tcore.xyz",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "560",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    r = requests.request("POST", url, data=payload, headers=headers).json()
    total_flights=len(r['body']['data']['itineraries'])
    print(total_flights)
    flight_search={
        'total_flights':total_flights,
        'depart_airport_code':r['body']['data']['itineraries'][0]['origin_destinations'][0]['segments'][0]['departure']['airport']['code'],
        'depart_airport_country_name':r['body']['data']['itineraries'][0]['origin_destinations'][0]['segments'][0]['departure']['airport']['country_name'],
        'depart_airport_name':r['body']['data']['itineraries'][0]['origin_destinations'][0]['segments'][0]['departure']['airport']['name'],
        'depart_airport_city_name':r['body']['data']['itineraries'][0]['origin_destinations'][0]['segments'][0]['departure']['airport']['city_name'],
        'arrival_airport_code':r['body']['data']['itineraries'][0]['origin_destinations'][0]['segments'][-1]['arrival']['airport']['code'],
        'arrival_airport_country_name':r['body']['data']['itineraries'][0]['origin_destinations'][0]['segments'][-1]['arrival']['airport']['country_name'],
        'arrival_airport_name':r['body']['data']['itineraries'][0]['origin_destinations'][0]['segments'][-1]['arrival']['airport']['name'],
        'arrival_airport_city_name':r['body']['data']['itineraries'][0]['origin_destinations'][0]['segments'][-1]['arrival']['airport']['city_name']
    }
    flightDepartCode_data.append(flight_search)
    # print(r['body']['data']['itineraries'])
    context={'flightDepartCode_data':flightDepartCode_data,'formD':formD,'formA':formA}
    return render(request, 'flight-results-1.html',context)

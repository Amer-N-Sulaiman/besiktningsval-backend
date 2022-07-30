from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.http import JsonResponse
import datetime

import json

# Create your views here.

def getOpusStations(request):
    APIUrl = 'https://api2.bilprovning.se/api/stations'
    stations = requests.get(APIUrl).json()
    return JsonResponse(stations, safe=False)


# Turn this into a GET api
def getOpusBookingId(request, regno):
    print('getOpusBookingId')
    timeInfo_APIUrl = 'https://api2.bilprovning.se/api/bookings/'
    
    if request.method=='GET':
        # data to get time info
        post_data = {'Regno': regno}
        # data to book for inspection product
        put_data = {
            'Vehicles': [{'Products': [342], 'Regno': regno}]
        }
        headers = {'Content-Type': 'application/json'}

        bookingInfo = requests.post(timeInfo_APIUrl, data=json.dumps(post_data), headers=headers).json()
        products_APIUrl = 'https://api2.bilprovning.se/api/bookings/'+bookingInfo['Id']+'/products'
        requests.put(products_APIUrl, data=json.dumps(put_data), headers=headers)
        return JsonResponse(bookingInfo)
    else:
        print('Bad Request')

def getOpusStationTimeInfo(request, stationId, bookingId):
    print('getOpusStationTimeInfo')
    start_date = datetime.date.today() - datetime.timedelta(days=-1)
    start_date = start_date.isoformat()
    end_date = datetime.date.today() + datetime.timedelta(days=15)
    end_date = end_date.isoformat()
    APIUrl = 'https://api2.bilprovning.se/api/bookings/' + bookingId + '/availableTimes?stationIds='+ stationId +'&start='+ start_date +'&end=' + end_date
    timeInfo = requests.get(APIUrl).json()
    print(timeInfo)
    return JsonResponse(timeInfo, safe=False)


def getCarspectStationTimeInfo(request, stationId):
    start_date = datetime.date.today() - datetime.timedelta(days=-1)
    start_date = start_date.isoformat() + 'T00:00:00.000Z'
    end_date = datetime.date.today() + datetime.timedelta(days=15)
    end_date = end_date.isoformat() + 'T23:59:59.999Z'
    APIUrl = 'https://booking-api.muster.se/v1/Calendar/'+stationId+'?StartDate='+ start_date +'&EndDate='+end_date+'&ProductId=1'
    timeInfo = requests.get(APIUrl).json()
    print(timeInfo)
    return JsonResponse(timeInfo, safe=False)

def getCarInfo(request, regno):
    APIUrl = 'https://www.car.info/en-se/search/super/' + regno
    carInfo = requests.get(APIUrl).json()
    return JsonResponse(carInfo)

# def getGoogleGeolocationInfo(request):
#     APIKey = 'AIzaSyD_pctPKnFcgCLTjbkmVvXFqUHM2VnIywk'
#     APIUrl = 'https://www.googleapis.com/geolocation/v1/geolocate?key='+APIKey
#     post_data = {'one': 'one'}
#     headers = {'Content-Type': 'application/json'}
    
#     geolocationIno = requests.post(APIUrl, data=json.dumps(post_data), headers=headers).json()
#     return JsonResponse(geolocationIno) 

def getDekraStations(request, regno):
    # myDekraBookingIdUrl = 'https://api.besiktningsval.se/api/getDekraBookingId/'+regno+'/'
    # bookingInfo = requests.get(myDekraBookingIdUrl).json()
    # bookingId = bookingInfo['id']
    # dekraStationsUrl = 'https://bokning.dekra-bilbesiktning.se/bb-web/api/booking/'+bookingId+'/shops/'
    
    # dekraStations = requests.get(dekraStationsUrl).json()
    # dekraStationsFiltered = []
    dekraStationsFinal= [{"id": 1, "stationNumber": "5000", "address": "Tagenev\u00e4gen 17", "city": "Hisings K\u00e4rra", "latitude": 57.774355, "longitude": 11.994045}, {"id": 4, "stationNumber": "5016", "address": "Norra L\u00e5ngebergsgatan 2", "city": "V\u00e4stra Fr\u00f6lunda", "latitude": 57.648911, "longitude": 11.955677}, {"id": 23, "stationNumber": "5022", "address": "Skolg\u00e5ngen 9", "city": "G\u00e4vle", "latitude": 60.658133, "longitude": 17.158193}, {"id": 25, "stationNumber": "5048", "address": "Sandbergsv\u00e4gen 4E", "city": "Alings\u00e5s", "latitude": 57.925999, "longitude": 12.547309}, {"id": 26, "stationNumber": "5011", "address": "Kroksl\u00e4ttspark gata 4", "city": "M\u00f6lndal", "latitude": 57.67647, "longitude": 12.00553}, {"id": 29, "stationNumber": "5026", "address": "WEDAV\u00c4GEN 22", "city": "S\u00f6dert\u00e4lje", "latitude": 59.20746, "longitude": 17.64113}, {"id": 34, "stationNumber": "5029", "address": "Kilenv\u00e4gen 9-15", "city": "Str\u00e4ngn\u00e4s", "latitude": 59.350499, "longitude": 17.030268}, {"id": 36, "stationNumber": "5028", "address": "Pollengatan 2", "city": "Varberg", "latitude": 57.166429, "longitude": 12.275629}, {"id": 38, "stationNumber": "5054", "address": "Mellomkvarnsv\u00e4gen 9", "city": "Sk\u00f6vde", "latitude": 58.418641, "longitude": 13.878387}, {"id": 40, "stationNumber": "5033", "address": "Turbov\u00e4gen 5", "city": "Pite\u00e5", "latitude": 65.31917, "longitude": 21.41716}, {"id": 41, "stationNumber": "5039", "address": "\u00d6sterleden 10 ", "city": "Katrineholm", "latitude": 59.003976, "longitude": 16.23107}, {"id": 42, "stationNumber": "5040", "address": "\u00c5sbj\u00f6rnsgatan 1B", "city": "Link\u00f6ping", "latitude": 58.418662, "longitude": 15.637846}, {"id": 46, "stationNumber": "5037", "address": "Kaptensgatan 27", "city": "H\u00e4ssleholm", "latitude": 56.158075, "longitude": 13.745162}, {"id": 48, "stationNumber": "5046", "address": "J\u00e4gersrov\u00e4gen 100", "city": "Malm\u00f6", "latitude": 55.572334, "longitude": 13.056201}, {"id": 51, "stationNumber": "5043", "address": "Midg\u00e5rdsgatan 11B", "city": "\u00c4ngelholm", "latitude": 56.252304, "longitude": 12.894915}, {"id": 54, "stationNumber": "5041", "address": "Gammelstadsv\u00e4gen 21A", "city": "Lule\u00e5", "latitude": 65.594496, "longitude": 22.154102}, {"id": 55, "stationNumber": "5049", "address": "Tj\u00e4rnv\u00e4gen 6", "city": "Skellefte\u00e5", "latitude": 64.734074, "longitude": 20.964281}, {"id": 57, "stationNumber": "5053", "address": "Hantverkargatan 5", "city": "Borl\u00e4nge", "latitude": 60.476577, "longitude": 15.431898}, {"id": 58, "stationNumber": "5055", "address": "Kullb\u00e4cksv\u00e4gen 3", "city": "Hudiksvall", "latitude": 61.733979, "longitude": 17.097819}, {"id": 62, "stationNumber": "5061", "address": "H\u00e4s\u00e4ngsv\u00e4gen 4", "city": "Karlskoga", "latitude": 59.323356, "longitude": 14.497011}, {"id": 63, "stationNumber": "5062", "address": "Bergsn\u00e4sgatan 2 ", "city": "Avesta", "latitude": 60.141876, "longitude": 16.194545}, {"id": 66, "stationNumber": "5065", "address": "Hjalmar Petris V\u00e4g 30", "city": "V\u00e4xj\u00f6", "latitude": 56.893602, "longitude": 14.775249}, {"id": 69, "stationNumber": "5069", "address": "Torggatan 54", "city": "Vara", "latitude": 58.256593, "longitude": 12.963522}, {"id": 72, "stationNumber": "5072", "address": "Bomv\u00e4gen 3", "city": "Ume\u00e5", "latitude": 63.837613, "longitude": 20.246311}, {"id": 73, "stationNumber": "5068", "address": "Industriv\u00e4gen 4", "city": "Falkenberg", "latitude": 56.906053, "longitude": 12.464225}, {"id": 74, "stationNumber": "5073", "address": "Skiftesv\u00e4gen 5H", "city": "\u00d6stersund", "latitude": 63.167085, "longitude": 14.687605}, {"id": 77, "stationNumber": "5075", "address": "Fj\u00e4rilsgatan 2", "city": "Norrk\u00f6ping", "latitude": 58.578305, "longitude": 16.214758}, {"id": 79, "stationNumber": "5078", "address": "Olof Engbergs v\u00e4g 4B", "city": "Ljusdal", "latitude": 61.823776, "longitude": 16.118842}, {"id": 81, "stationNumber": "5081", "address": "Fr\u00f6storpsgatan 3", "city": "Link\u00f6ping", "latitude": 58.430254, "longitude": 15.602898}, {"id": 84, "stationNumber": "5084", "address": "Slipv\u00e4gen 2F", "city": "Boden", "latitude": 65.807781, "longitude": 21.716308}]

    # for station in dekraStations:
    #     station1 = {
    #         'id': station['id'],
    #         'stationNumber': station['stationNumber'],
    #         'address': station['addressLine1'],
    #         'city': station['city'],
    #         'latitude': station['latitude'],
    #         'longitude': station['longitude'],
    #     }
    #     dekraStationsFiltered.append(station1)


    return JsonResponse(dekraStationsFinal, safe=False)


def getDekraBookingId(request, regno):

    dekraCarInfoUrl = 'https://bokning.dekra-bilbesiktning.se/bb-web/api/v2/vehicles/'+regno+'/summarywithproducts'
    carInfo = requests.get(dekraCarInfoUrl).json()
    post_data = {"clientIp":None,
    "contactInformation":None,
    "desiredArea":None,
    "id":None,
    "items":[
        {"startTime":None,
        "products":[{"id":1}],
        "registrationNumber":"JBG988",
        "trafficStatus":carInfo['trafficStatus'],
        "vehicleDimensions":{
            "grossWeight":carInfo['dimensions']['grossWeight'],
            "length":carInfo['dimensions']['length'],
            "width":carInfo['dimensions']['width'],
            "height":carInfo['dimensions']['height'],
            "wheelBase":carInfo['dimensions']['wheelBase'],
            "towHitchDistanceNational":None,
            "towHitchDistanceEU":None,
            "numberOfAxles":None},
        "vehicleKind":carInfo['vehicleKind'],
        "verifiedVehicle":True}],
    "originalId":None,
    "payable":False,
    "rebookable":False,
    "shopId":None,
    "status":"NEW"}

    dekraBookingUrl = 'https://bokning.dekra-bilbesiktning.se/bb-web/api/booking/'
    post_headers = {'Content-Type': 'application/json'}

    bookingInfo = requests.post(dekraBookingUrl, data=json.dumps(post_data), headers=post_headers).json()
    # bookingInfo['id'] is the booking id

    return JsonResponse(bookingInfo)


def getDekraStationTimeInfo(request, stationId, bookingId):
    start_date = datetime.date.today() - datetime.timedelta(days=1)
    start_date = start_date.isoformat()
    end_date = datetime.date.today() + datetime.timedelta(days=29)
    end_date = end_date.isoformat()
    timeInfoUrl = 'https://bokning.dekra-bilbesiktning.se/bb-web/api/v2/shops/timeslots?shopId='+stationId+'&forBooking='+bookingId+'&fromDate='+start_date+'&toDate='+end_date+'/'
    timeInfo = requests.get(timeInfoUrl).json()
    print(start_date)
    print(end_date)
    return JsonResponse(timeInfo, safe=False)



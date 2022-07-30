from django.urls import path
from .views import getOpusStations, getOpusBookingId, getOpusStationTimeInfo, getCarspectStationTimeInfo, getCarInfo, getDekraBookingId, getDekraStations, getDekraStationTimeInfo

app_name='api'

urlpatterns = [
    path('getOpusStations/', getOpusStations, name='getStations'),
    path('getOpusBookingId/<str:regno>/', getOpusBookingId, name='getOpusBookingId'),
    path('getOpusStationTimeInfo/<str:stationId>/<str:bookingId>/', getOpusStationTimeInfo, name='getStationTimeInfo'),

    path('getCarspectStationTimeInfo/<str:stationId>/', getCarspectStationTimeInfo, name='getCarspectTimeInfo'),
    path('getCarInfo/<str:regno>/', getCarInfo, name='getCarInfo'),
    # path('getGoogleGeolocationInfo/', getGoogleGeolocationInfo, name='getGoogleGeolocationInfo')

    path('getDekraStations/<str:regno>/', getDekraStations, name='getDekraStations'),
    path('getDekraBookingId/<str:regno>/', getDekraBookingId, name='getDekraBookingId'),
    path('getDekraStationTimeInfo/<str:stationId>/<str:bookingId>/', getDekraStationTimeInfo, name='getDekraStationTimeInfo')
]

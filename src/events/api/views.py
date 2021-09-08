
from typing import Any
from rest_framework import  generics, serializers
from rest_framework.views import APIView
from events.models import Event, SubscribeEmail, Order
from .serializers import EventSerializer, SubscribeEmailSerializer, OrderSerializer
from datetime import datetime, timedelta
from rest_framework.response import Response
from rest_framework.status import HTTP_202_ACCEPTED
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication

# All Events
class EventListAPIView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    

# City Search
class EventCityListAPIView(generics.ListAPIView):
    serializer_class = EventSerializer
    
    def get_queryset(self):
        city = self.kwargs['city']
        queryset = Event.objects.filter(city=city)
        return queryset

# Category Search
class EventCategoryListAPIView(generics.ListAPIView):
    serializer_class = EventSerializer
    
    def get_queryset(self):
        category = self.kwargs['category']
        queryset = Event.objects.filter(category=category)
        return queryset


# City + Category Search
class EventCityCategoryListAPIView(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        city = self.kwargs['city']
        category = self.kwargs['category']
        queryset = Event.objects.filter(city=city, category=category)
        return queryset

# All popular
class EventPopularListAPIView(generics.ListAPIView):
    queryset = Event.objects.filter(popular=True)
    serializer_class = EventSerializer

# Newest events
class EventLatestListAPIView(generics.ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.filter(date_added__gte=datetime.now() - timedelta(days=365))

# Display one event
class EventDetailView(generics.RetrieveAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


# Events for carousel
class EventsCarouselListAPIView(generics.ListAPIView):
    queryset = Event.objects.filter(carousel=True)
    serializer_class = EventSerializer



class SubscribeEmailView(generics.ListCreateAPIView):
    serializer_class = SubscribeEmailSerializer
    permission_classes = [AllowAny]
    queryset = SubscribeEmail.objects.all()
    
    
    def post(self, request, format=None):
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            obj = SubscribeEmail(email=email)
            obj.save()
        
        return Response(SubscribeEmailSerializer(obj).data, status=HTTP_202_ACCEPTED)

class OrderListView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]
    queryset = Order.objects.all()
    
    
    def post(self, request, format=None):
        serializer = self.get_serializer_class()(data=request.data)
    
        if serializer.is_valid():
            name = serializer.data.get('name')
            email = serializer.data.get('email')
            phone = serializer.data.get('phone')
            events = serializer.data.get('events')
            
            order_obj = Order.objects.create(name=name, email=email, phone=phone)
            order_obj.events.set(events)
            order_obj.save()
        
        return Response(OrderSerializer(order_obj).data, status=HTTP_202_ACCEPTED)

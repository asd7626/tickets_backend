from rest_framework import  generics
from events.models import Event
from .serializers import EventSerializer
from datetime import datetime, timedelta

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
    queryset = Event.objects.filter(date_added__gte=datetime.now() - timedelta(days=1))

# Display one event
class EventDetailView(generics.RetrieveAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

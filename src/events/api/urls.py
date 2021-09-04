from django.urls import path
from .views import (
    EventListAPIView, EventCityListAPIView, EventCategoryListAPIView,
     EventCityCategoryListAPIView, EventPopularListAPIView, EventLatestListAPIView,
      EventDetailView, SubscribeEmailView, EventsCarouselListAPIView, OrderListView
)



urlpatterns = [
    
    path('latest/', EventLatestListAPIView.as_view(), name='events-latest'),
    path('popular/', EventPopularListAPIView.as_view(), name='events-popular'),
    path('carousel/', EventsCarouselListAPIView.as_view(), name='events-carousel'),
    path('subscribeemail/', SubscribeEmailView.as_view(), name='subscribe-email'),
    path('orderlist/', OrderListView.as_view(), name='events-orders'),
    path('<int:pk>/', EventDetailView.as_view(), name='events-detail'),
    path('', EventListAPIView.as_view(), name='events' ),
    
    path('<str:city>/', EventCityListAPIView.as_view(), name='events-city'),
    
    path('category/<str:category>/', EventCategoryListAPIView.as_view(), name='events-category'),
    path('<str:city>/category/<str:category>/', EventCityCategoryListAPIView.as_view(), name='events-city-category'),   
    
]

 
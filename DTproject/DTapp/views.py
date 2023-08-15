# views.py
from django.shortcuts import render
from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
    @action(detail=True, methods=['GET'])
    def attendees(self, request, pk=None):
        event = self.get_object()
        attendee_ids = list(event.attendees.values_list('id', flat=True))
        return Response(attendee_ids)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        # Handle attendees
        attendee_ids = request.data.get('attendees', [])
        instance.attendees.set(attendee_ids)

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

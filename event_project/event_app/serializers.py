from rest_framework.serializers import ModelSerializer
from event_app.views import Events

class EventsSerializer(ModelSerializer):
    class Meta:
        model =Events 
        fields='__all__'


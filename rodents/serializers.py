from rest_framework import serializers
from .models import Cage

class CageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cage
        fields = ('id','ri', 'pi', 'researcher', 'cage_type','facility', 'room', 'rack','column','row')
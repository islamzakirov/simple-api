from rest_framework import serializers
from .models import *

class VideoSerializer(serializers.ModelSerializer):
    class Meta():
        model = Video
        fields = '__all__'

class MusicSerializer(serializers.ModelSerializer):
    class Meta():
        model = Music
        fields = '__all__' 
from rest_framework import serializers
from .models import UserData,UserSound,BeatSound


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = ['id','name','email','profile_pic']

class BeatSoundSerializer(serializers.ModelSerializer):

    class Meta:
        model = BeatSound
        fields = ['title','beat_image','beat_file']

class UserSoundSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserSound
        fields = ['user','beat_audio','user_audio']

class UserScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserSound
        fields = ['beat_audio','user_audio','user_score']
        depth = 1

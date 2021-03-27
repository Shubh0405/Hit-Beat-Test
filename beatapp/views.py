from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status,views
from .models import UserData, BeatSound, UserSound
from .serializers import UserSerializer, BeatSoundSerializer, UserSoundSerializer, UserScoreSerializer
from .hit_beat import getscore


# Create your views here.
@api_view(['POST'])
def UserDetails(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            email = request.data['email']
            try:
                user = UserData.objects.get(email=email)
            except:
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            if ('already' in serializer.errors['email'][0]) or ('already' in serializer.errors['id'][0]):
                return Response({'error':'User Already Exists!'}, status = status.HTTP_200_OK)
            return Response(serializer.errors['email'], status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def UserGetDetails(request,pk):
    if request.method == "GET":
        user = UserData.objects.get(id=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def BeatGetDetails(request):
    if request.method == "GET":
        beats = BeatSound.objects.all()
        serializer = BeatSoundSerializer(beats,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def UserAudioPost(request):
    if request.method == "POST":
        serializer = UserSoundSerializer(data=request.data)
        if serializer.is_valid():
            user_id = request.data['user']
            user = UserData.objects.get(id=user_id)
            beat_audio_title = request.data['beat_audio']
            beat_audio = BeatSound.objects.get(title=beat_audio_title)
            default_score = 0
            try:
                previous_score = UserSound.objects.get(user=user,beat_audio=beat_audio)
                previous_score.user_audio = request.FILES['user_audio']
                previous_score.save()
            except:
                score = 0
                serializer.save(user_score = score)
                previous_score = UserSound.objects.get(user=user,beat_audio=beat_audio)
            score = getscore(previous_score.beat_audio.beat_file.url,previous_score.user_audio.url)
            print(score)
            previous_score.user_score = score
            previous_score.save()
            Score_response = {
                'score': score
            }
            return Response(Score_response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def BeatGetDetails(request):
    if request.method == "GET":
        beats = BeatSound.objects.all()
        serializer = BeatSoundSerializer(beats,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def UserScoreGet(request,pk):
    if request.method == "GET":
        user = UserData.objects.get(id=pk)
        scores = UserSound.objects.filter(user=user)
        serializer = UserScoreSerializer(scores,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

from datetime import timedelta
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer,UserProfileSerializer,eventSerializer
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken 
from rest_framework import status
from .models import User, UserProfile, Candidate, Event, Voted
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticated
from django.core.serializers import serialize

@api_view(['POST'])
def create_user(request):
    data=request.data
    print(data)
    serializer = UserSerializer(data=data)
    print(serializer)
    if serializer.is_valid():
      password_hash=make_password(data['password'])
      print(password_hash)
      user_instance = serializer.save(password=password_hash)
      refresh = RefreshToken()
      print(user_instance)
      access_token =  AccessToken .for_user(user_instance)
      access_token.set_exp(lifetime=timedelta(days=1))  
      print("no")
      user_data = {
        'id': user_instance.id,
        'username': user_instance.username,
        'email': user_instance.email,}
    
      access_token = str(refresh.access_token)
      return Response({
        'user': user_data,
        'refresh': str(refresh),  
        'access': str(access_token),  
          }, status=status.HTTP_200_OK)
    else:
      return Response({'error':serializer.errors})
    
    
    
@api_view(['POST'])
def signup(request):
   data = request.data
   print(data)
   email = data['email']
   password = data['password']
   
   user = User.objects.filter(email=email).first()
   if user is None:
    raise AuthenticationFailed('User not found!')
   if not check_password(password, user.password):
    raise AuthenticationFailed('Incorrect password!')
   print("ur in")

   refresh = RefreshToken()
 
   print("ur in end")
   return Response({
    'refresh': str(refresh),
  'access': str(refresh.access_token)})
   
   
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def enter_profile(request, user_id):
    return Response({'hello': 'world'})
  
  
@api_view(['GET'])
def get_events(request):
   event=Event.objects.all()
   serialized_events = serialize('json', event)
   return JsonResponse(serialized_events, safe=False)
 
@api_view(['GET'])
def get_candidates(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    candidates = event.candidates.all()
    serialized_candidates = serialize('json', candidates)
    return JsonResponse(serialized_candidates, safe=False)
  

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def vote(request, event_id, candidate_id):
    event = get_object_or_404(Event, pk=event_id)
    candidate = get_object_or_404(Candidate, pk=candidate_id)
    voted = Voted.objects.filter(the_voted=request.user, the_candidate=candidate,Event=event).exists()
    
    if voted:
      return Response({'message': 'Already voted'})
    else:
      
        candidate.total_vote=+1
        candidate.save()
        Voted.objects.create(event=event, candidate=candidate, the_voted=request.user)
    return Response({'message': 'Vote casted successfully'})
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework import viewsets
from .permission import IsAdminOrReadOnly
from .models import LandOwner, FootballField, Reservation
from .serializers import (
    UserSerializer, LandOwnerSerializer,
    FootballFieldSerializer, ReservationSerializer
)

class LandOwnerViewSet(viewsets.ModelViewSet):
    queryset = LandOwner.objects.all()
    serializer_class = LandOwnerSerializer

class FootballFieldViewSet(viewsets.ModelViewSet):
    queryset = FootballField.objects.all()
    serializer_class = FootballFieldSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully.'}, status=201)
        return Response(serializer.errors, status=400)

class ObtainAuthToken(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=200)
            else:
                return Response({'error': 'Invalid credentials.'}, status=400)
        except User.DoesNotExist:
            return Response({'error': 'Invalid credentials.'}, status=400)
        

class LandOwnerViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAdminOrReadOnly]

class FootballFieldViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAdminOrReadOnly]

class ReservationViewSet(viewsets.ModelViewSet):[]
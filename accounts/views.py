from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated

from .serializers import SignUpSerializer, LoginSerializer, CustomUserDetailSerializer, EditCustomUserSerializer
from .permissions import IsUser


class SignUpView(APIView):
    serializer_class = SignUpSerializer

    def post(self, request, format=None):
            if request.user.is_authenticated:
                raise AuthenticationFailed('User already authenticated')
            serializer = SignUpSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()

                username = request.data.get('username')
                password = request.data.get('password')

                user = authenticate(username=username, password=password)

                if not user:
                    raise AuthenticationFailed('User already authenticated')

                refresh = RefreshToken.for_user(user)
                return Response(
                    {
                        'access_token': str(refresh.access_token),
                        'refresh_token': str(refresh),
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')

            user = authenticate(email=email, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({'access_token': str(refresh.access_token),
                                 'refresh_token': str(refresh)}, status=status.HTTP_200_OK)
            else:
                raise AuthenticationFailed('Invalid credentials')
        except AuthenticationFailed as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CustomUserDetailView(APIView):
    permission_classes = [IsAuthenticated, IsUser]
    serializer_class = CustomUserDetailSerializer, EditCustomUserSerializer

    # GET method to get user detaila
    def get(self, request):
        try:
            user = request.user
            if user:
                serializer = CustomUserDetailSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                raise AuthenticationFailed('Authentication error')

        except AuthenticationFailed as e:
            return Response({'detail': str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        

    def put(self, request):
        try:
            user = request.user
            if user:
                serializer = EditCustomUserSerializer(user, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                raise AuthenticationFailed('Authentication error')
        except AuthenticationFailed as e:
                    return Response({'detail': str(e)}, status=status.HTTP_401_UNAUTHORIZED)

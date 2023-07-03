from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed, ValidationError

from .serializers import SignUpSerializer


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
                return Response({'errorrrrr': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

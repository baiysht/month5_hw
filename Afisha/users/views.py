from django.core.mail import send_mail
from django.db.migrations import serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from django.contrib.auth.models import User
from rest_framework.views import APIView
from users.serializers import RegisterSerializer, AuthSerializer, SMSCodeSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from random import randint
from . import models, serializers


class authorization_api_view(APIView):
    def post(self, request):
        serializer = AuthSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(**serializer.validated_data)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED,
                        data={'error': 'Invalid credentials'})


class registration_api_view(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user = User.objects.create_user(username=username, password=password,
                                        is_active=False)

        code = ''.join([str(randint(0, 9)) for i in range(6)])
        models.SMSCode.objects.create(user=user, code=code)
        send_mail(
            'Registration code',
            message=code,
            from_email='<EMAIL>',
            recipient_list=[user.email]
        )
        return Response(data={'user_id': user.id}, status=status.HTTP_201_CREATED)


class SmsCode_api_view(APIView):
    def post(self, request):
        serializer = SMSCodeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        sms_code = serializer.validated_data.get('sms_code')
        try:
            sms_code = models.SMSCode.objects.get(sms_code=sms_code)
        except models.SMSCode.DoesNotExist:
            return Response(data={'error': 'Invalid SMSCode'}, status=status.HTTP_404_NOT_FOUND)
        sms_code.is_active = True
        sms_code.save()
        sms_code.delete()
        return Response(status=status.HTTP_200_OK)
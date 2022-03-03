from django.shortcuts import render
from user_app.api.serializers import RegistrationSerializer
from user_app.models import models
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['POST',])
def register_view(request):
    if request.method == 'POST':
        
        serializer=RegistrationSerializer(data=request.data)
        data={}
        
        if serializer.is_valid():
            accounts=serializer.save()
    
            token=Token.objects.get(user=accounts).key
            data={
                'response':"registration sucessfull",
                'username':accounts.username,
                'email':accounts.email,
                'first_name':accounts.first_name,
                'token':token
            }
            
            # for user in User.objects.all():
            #  token= Token.objects.get_or_create(user=user)[1]
            
           
            # data['token']=token  
        else:
            data=serializer.errors
        
        return Response(data)
            
            
@api_view(['POST',])
def logout_view(request):
    if request.method == 'POST':
        token=request.user.auth_token
        print(token)
        token.delete()
        return Response(status=status.HTTP_200_OK)
    

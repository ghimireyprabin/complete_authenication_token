# from pyexpat import model
from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type': 'password'},write_only=True)
    class Meta:
        model=User
        fields=['username','email','password','password2','first_name']
        extra_kwargs={
            'password':{'write_only':True}
        }
        
    
    def save(self):
        
        password = self.validated_data['password']
        password2=self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError('not the same in both fields')
        
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError('email already exits')
        
        account = User(email=self.validated_data['email'],
                       username=self.validated_data['username'],
                       first_name=self.validated_data['first_name'])
        account.set_password(password)
        account.save()
        return account   
        
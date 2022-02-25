from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterUserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(required=True)
    password2 = serializers.CharField(required=True)    

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        extra_kwargs = {
            'password1':{'write_only':True},
            'password2':{'write_only':True},            
        }

    def create(self, validated_data):
        email = validated_data['email']
        username = validated_data['username']
        password1 = validated_data['password1']
        password2 = validated_data['password2']

        if password1==password2:
            user = User(email=email,username=username)
            user.set_password(validated_data['password1'])
            user.save()
            return user
        else:
            raise serializers.ValidationError({
                'error':'Password does not match!'
            })
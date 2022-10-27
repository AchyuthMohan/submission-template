from dataclasses import field, fields
from importlib.metadata import files
from rest_framework import serializers
from .models import (User,UserDetail,UserOpinionAgent,TrendingInsuranceAgents,CarLoan,HousingLoan,Medical_expense,Electronic_Devices,DiscussionBoard)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken,TokenError

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=68,min_length=6,write_only=True)
    permission_classes=[IsAuthenticated]
    class Meta:
        model=User
        fields=['email','username','password']

    def validate(self,attrs):
        email=attrs.get('email','')
        username=attrs.get('username','')

        if not username.isalnum():
            raise serializers.ValidationError("username should contain only alpha numeric chars")
        return attrs

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email']

class DiscussionSerializer(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None,allow_empty_file=False,use_url=True,required=False)
    class Meta:
        model=DiscussionBoard
        fields='__all__'

class CarLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model=CarLoan
        fields='__all__'

class TrendingInsuranceSerializer(serializers.ModelSerializer):
    org_image=serializers.ImageField(max_length=None,allow_empty_file=False,use_url=True,required=False)
    class Meta:
        model=TrendingInsuranceAgents
        fields='__all__'

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserDetail
        fields='__all__'
class UserOpinionAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserOpinionAgent
        fields='__all__'

class HousingLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model=HousingLoan
        fields='__all__'

class Medical_expenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Medical_expense
        fields='__all'

class Electronic_DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Electronic_Devices
        fields='__all'

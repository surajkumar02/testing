from django.shortcuts import render
from django.contrib.auth.models import User
from .models import SocialUser
from .serializers import UserSerializer,SocialUserSerializer
from rest_framework import status
from rest_framework.views import APIView,Response
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

class login(APIView):
    def post(self,request):
        if request.data:
            try:
                username=request.data['email']
                password=request.data['password']
                useravail=User.objects.get(username=username)
                if useravail.check_password(password):   
                    token=RefreshToken.for_user(useravail)
                    return Response(data={"username":useravail.first_name,
                    "email":useravail.email,
                    "token":{"refresh":str(token),
                    "access":str(token.access_token)}
                    })
                return Response("Incorrect Password",status=status.HTTP_422_UNPROCESSABLE_ENTITY)    
            except:
                return Response("Incompleted format",status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        return Response("Enter Valid Credentials",status=status.HTTP_404_NOT_FOUND)

class signup(APIView):
    def post(self,request):
        email=request.data["username"]
        password=request.data['password']
        name=request.data['name']

        useravail=UserSerializer(data={**request.data})
        if useravail.is_valid():
            user=User.objects.create(username=email,email=email,first_name=name)
            user.set_password(password)
            user.save()

            token=RefreshToken.for_user(user)
            return Response(data={"username":user.first_name,
            "email":user.username,
            "token":{"refresh":str(token),
            "access":str(token.access_token)}})

        content="user already Exists"
        return Response(content,status=status.HTTP_406_NOT_ACCEPTABLE)

class social_login(APIView):
    def post(self,request):
        if request.data:
            try:
                username=request.data['email']
                password=request.data['password']
                provider=request.data['provider']
                useravail=SocialUser.objects.get(username=username)
                if (password==useravail.password) and (provider==useravail.provider):   
                    token=RefreshToken.for_user(useravail)
                    return Response(data={"username":useravail.name,
                    "email":useravail.email,
                    "token":{"refresh":str(token),
                    "access":str(token.access_token)}
                    })
                return Response("Incorrect Provider",status=status.HTTP_422_UNPROCESSABLE_ENTITY)    
            except:
                return Response("Incompleted format",status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        return Response("Enter Valid Credentials",status=status.HTTP_404_NOT_FOUND)

class social_signup(APIView):
    def post(self,request):
        email=request.data["username"]
        password=request.data['password']
        name=request.data['name']
        provider=request.data['provider']

        useravail=SocialUserSerializer(data={**request.data})
        if useravail.is_valid():
            user=SocialUser.objects.create(username=email,email=email,name=name,provider=provider)
            user.password=password
            user.save()

            token=RefreshToken.for_user(user)
            return Response(data={"username":user.name,
            "email":user.username,
            "token":{"refresh":str(token),
            "access":str(token.access_token)}})

        content="user already Exists"
        return Response(content,status=status.HTTP_406_NOT_ACCEPTABLE)

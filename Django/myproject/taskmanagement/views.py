from django.shortcuts import render
from django.http import HttpResponse
from .models import User,Task,Comments
from .serializers import UserSerializers,TaskSerializers,CommentsSerializers
# Create your views here.

def hello(request):
    return HttpResponse("hey!! whatsupp ajmal khan")


from rest_framework import status
from django.contrib.auth import authenticate,login,logout
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'])
def RegisterAPIView(request):

    serializer=UserSerializers(data=request.data)
    print(request.data)
    if serializer.is_valid():
        username=serializer.validated_data.get("username")
        password=serializer.validated_data.get("password")
        
        userdata=User.objects.create_user(username=username,password=password)
        
        user=authenticate(username=username,password=password)
        if user:
            refresh=RefreshToken.for_user(user)
            print(refresh.access_token)
            return Response({"token":str(refresh.access_token)})
        else:
            return Response({'error':'Invalid Credentials'})
        
    else:
        return Response(serializer.errors)
    

@api_view(['POST'])
def LoginAPIView(request):
    username=request.data['username']
    password=request.data['password']
    user=authenticate(username=username,password=password)
    print(user.is_superuser)
    if user:
        refresh=RefreshToken.for_user(user)
        refresh.payload["superuser"]=user.is_superuser
        return Response({"token":str(refresh.access_token)})
    else:
        return Response({"error":"Invalid Credentials"})



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_product_admin(request):
    print(request.data)
    serializer=TaskSerializers(data=request.data)
    print(serializer.is_valid)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Task added succesfully"}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_product_admin(request):
    tasks=Task.objects.all()
    serializer=TaskSerializers(tasks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_users(request):
    users=User.objects.filter(is_superuser=False)
    seializer=UserSerializers(users,many=True)
    return Response(seializer.data)

@api_view(['GET'])
def get_product_user(request,id):
    tasks=Task.objects.filter(members=id)
    serializer=TaskSerializers(tasks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_specific_product(request,id):
    tasks=Task.objects.get(id=id)
    serializer=TaskSerializers(tasks)
    return Response(serializer.data)

@api_view(['POST'])
def update_product(request,id):
    task=Task.objects.get(id=id)
    print(request.data)
    serializer=TaskSerializers(task,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Task added succesfully"}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def delete_product(request,id):
    task=Task.objects.get(id=id)
    task.delete()
    return Response({"message":"Task deleted succesfully"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def post_comment(request):
    print(request.data)
    serializer=CommentsSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Comment Posted Succesfully"}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def get_comments(request,id):
    comments=Comments.objects.filter(task_id=id)
    serializer=CommentsSerializers(comments,many=True)
    return Response(serializer.data)
from rest_framework import serializers
from .models import User,Task,Comments


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password']


class TaskSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=Task
        fields='__all__'

class CommentsSerializers(serializers.ModelSerializer):

    class Meta:
        model=Comments
        fields='__all__'
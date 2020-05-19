from .models import DoTitle,DoComment,DoList
from rest_framework import serializers

class DoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoList
        fields = ['id',"list"]

class DoCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoComment
        fields = ['id',"comment"]

class DoTitleSerializer(serializers.ModelSerializer):
    dolist = DoListSerializer(many= True)
    docomment = DoCommentSerializer(many = True)

    class Meta:
        model = DoTitle
        fields = ('id','title','pub_date','dolist','docomment')



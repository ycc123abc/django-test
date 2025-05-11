from django.shortcuts import render

# Create your views here.

from  rest_framework.views import APIView
import app01.models as models
from    rest_framework.response  import Response
from rest_framework import serializers
from rest_framework import status

from django.contrib.auth.hashers import make_password

class Getclassroomserializers(serializers.Serializer):
    class Meta:
        model=models.classroom
        fields="__all__"

class Getclassroom(APIView):
    def get(self,request):
        queryset=models.classroom.objects.all()
        serializer=Getclassroomserializers(queryset,many=True)
        return Response(serializer.data)



class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'},
        min_length=6
    )

    class Meta:
        model = models.User
        fields = ('mobile', 'password', 'username')

    # 序列化器中直接调用 Django 的安全接口
    def create(self, validated_data):
        # 自动调用 make_password 的写法
        user = models.User.objects.create_user(
            mobile=validated_data['mobile'],
            password=validated_data['password'],  # 这里会自动加密
            username=validated_data.get('username'),
        )
        return user


class UserRegistrationView(APIView):
    """
    用户注册API
    POST /api/register/
    """
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'code': 201,
                'message': '注册成功',
                'data': {
                    'mobile': serializer.data['mobile'],
                    'username': serializer.data.get('username')
                }})
        return Response({
            'code': 400,
            'message': '注册失败',
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

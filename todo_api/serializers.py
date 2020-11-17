from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import UserProfile, TodoStuffs

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):

        user = UserProfile (
            username = validated_data['username'],
            name = validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, instance, validated_data):

        instance.username = validated_data.get('username', instance.username)
        instance.name = validated_data.get('name', instance.name)

        if validated_data.get('password'):
            instance.set_password(validated_data['password'])

        instance.save()

        return instance


class TodoStuffSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoStuffs
        fields = ('id', 'user', 'todo_text', 'created_on')
        extra_kwargs = {'user': {'read_only': True}}


    # def retrieve(self, request, instance):
    #     # fields = TodoStuffs.objects.filter(user=request.user)
    #     # print(fields)

    #     # instance = TodoStuffs (
    #     #     username = request.user.username
    #     # )

    #     instance.get(username=request.user.username)
    #     print(instance)
    #     return instance

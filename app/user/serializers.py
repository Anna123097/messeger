from django.contrib.auth.models import User
from rest_framework import serializers

from app.user.models import Profile, Friend, ProfilePhoto, CommentProfilePhoto


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    img=serializers.SerializerMethodField('is_img')

    def is_img(self, foo):
        print(foo.profile.img)
        return str(foo.profile.img)
    class Meta:
        model = User
        fields = ('id', 'username', 'img')


class FriendsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=False)
    friend = UserSerializer(read_only=True, many=False)

    class Meta:
        model = Friend
        fields = '__all__'


class CreateFriendSerializer(serializers.ModelSerializer):

    class Meta:
        model = Friend
        fields = '__all__'


class ProfilePhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfilePhoto
        fields = '__all__'


class ProfileCommentsPhotoSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=False)
    class Meta:
        model = CommentProfilePhoto
        fields = '__all__'


class CreateProfileCommentsPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentProfilePhoto
        fields = '__all__'




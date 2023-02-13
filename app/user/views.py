from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from app.user.models import Profile, Friend, ProfilePhoto, CommentProfilePhoto
from app.user.serializers import ProfileSerializer, FriendsSerializer, UserSerializer, CreateFriendSerializer, \
    ProfilePhotoSerializer, ProfileCommentsPhotoSerializer, CreateProfileCommentsPhotoSerializer


class GetProfileToToken(APIView):
    def get_object(self, id):
        try:
            return Profile.objects.get(user_id=id)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        profile = self.get_object(request.user.id)
        task_serializer = ProfileSerializer(profile)
        return Response(task_serializer.data)


class PatchProfileToToken(APIView):
    def get_object(self, pk):
        try:
            return Profile.objects.get(user_id=pk)
        except Profile.DoesNotExist:
            raise Http404

    def patch(self, request):
        object = self.get_object(request.user.id)
        serializer = ProfileSerializer(object, data=request.data,
                                            partial=True)  # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class GetListAllMyFriend(generics.ListAPIView):
    serializer_class = FriendsSerializer

    def get_queryset(self):
         return Friend.objects.filter(user=self.request.user)
        #return Friend.objects.all()


class DeleteFriend(APIView):

    def get_item(self,id):
        return Friend.objects.get(id=id)

    def delete(self, request, id):
        item = self.get_item(id)

        if request.user == item.user:
            item.delete()
            return Response('valid delete')

        else:
            return Response("now permition")


class GetProfileToUser(APIView):

    def get_object(self, id):
        return Profile.objects.get(user_id=id)

    def get(self, request, id):
        item = self.get_object(id)
        serializer = ProfileSerializer(item)
        return Response(serializer.data)


class GetSearchFriends(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
         return User.objects.filter(username__icontains=self.kwargs["search"])


class CreateFriend(APIView):

    def post(self, request, *args, **kwargs):
        print("create start")
        object = CreateFriendSerializer(data=request.data)
        count_fried = Friend.objects.filter(friend_id=request.data.get('friend')).count()
        if count_fried > 0:
            return Response('The user is added to the friends list', status=303)
        print(count_fried)
        if object.is_valid():
            print("yes")
            object.save(user=request.user)
            return Response(object.data)
        return Response(object.errors)



class CheckMyFriend(APIView):
    def post(self, request, *args, **kwargs):
        my_friend = request.data.get('friend')
        friend = Friend.objects.filter(user = request.user,friend_id = my_friend)
        print(friend)
        if friend.count() > 0:
            return Response(True)
        return Response(False)


class DeleteMyFriend(APIView):

    def post(self, request):
        my_friend = request.data.get('friend')
        friend = Friend.objects.filter(user = request.user,friend_id = my_friend)
        print(friend)
        for item in friend:
            item.delete()


        return Response('delete')


class GetListProfilePhotosToUser(generics.ListAPIView):
    serializer_class = ProfilePhotoSerializer

    def get_queryset(self):
         return ProfilePhoto.objects.filter(user=self.request.user).order_by('-id')


class CreateProfilePhoto(APIView):
    def post(self, request, *args, **kwargs):
        object = ProfilePhotoSerializer(data=request.data)
        if object.is_valid():
            object.save(user=request.user)
            return Response(object.data)
        return Response(object.errors)


class DeleteProfilePhoto(APIView):

    def get_item(self,id):
        return ProfilePhoto.objects.get(id=id)

    def delete(self, request, id):
        item = self.get_item(id)

        if request.user == item.user:
            item.delete()
            return Response('valid delete')

        else:
            return Response("now permition")


class GetListProfilePhotosToUserId(generics.ListAPIView):
    serializer_class = ProfilePhotoSerializer

    def get_queryset(self):
         return ProfilePhoto.objects.filter(user=self.kwargs['id']).order_by('-id')


class GetProfilePhotoToId(APIView):

    def get_object(self, id):
        return ProfilePhoto.objects.get(id=id)

    def get(self, request, id):
        item = self.get_object(id)
        serializer = ProfilePhotoSerializer(item)
        return Response(serializer.data)


class GetListCommentToProfilePhoto(generics.ListAPIView):
    serializer_class = ProfileCommentsPhotoSerializer

    def get_queryset(self):
         return CommentProfilePhoto.objects.filter(photo_id = self.kwargs['id']).order_by('-id')


class CreateCommentProfilePhoto(APIView):
    def post(self, request, *args, **kwargs):
        object = CreateProfileCommentsPhotoSerializer(data=request.data)
        if object.is_valid():
            object.save(user=request.user)
            return Response(object.data)
        return Response(object.errors)


class DeleteCommentProfilePhoto(APIView):

    def get_item(self,id):
        return CommentProfilePhoto.objects.get(id=id)

    def delete(self, request, id):
        item = self.get_item(id)

        if request.user == item.user:
            item.delete()
            return Response('valid delete')

        else:
            return Response("now permition")
        

class GetCommentToId(APIView):

    def get_object(self, id):
        return CommentProfilePhoto.objects.get(id=id)

    def get(self, request, id):
        item = self.get_object(id)
        serializer = ProfileCommentsPhotoSerializer(item)
        return Response(serializer.data)


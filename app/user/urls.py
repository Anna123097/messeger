from django.urls import path

from app.user.views import *

urlpatterns = [
    path('get/profile/to/token/', GetProfileToToken.as_view()),
    path('patch/profile/to/token/', PatchProfileToToken.as_view()),
    path('get/list/all/my/friend/', GetListAllMyFriend.as_view()),
    path('delete/friend/<int:id>/', DeleteFriend.as_view()),
    path('get/profile/to/user/<int:id>/', GetProfileToUser.as_view()),
    path('get/search/friend/<str:search>/', GetSearchFriends.as_view()),
    path('check/my/friend/', CheckMyFriend.as_view()),
    path('delete/my/friend/', DeleteMyFriend.as_view()),
    path('create/friend/', CreateFriend.as_view()),
    path('create/profile/photo/', CreateProfilePhoto.as_view()),
    path('delete/profile/photo/<int:id>/', DeleteProfilePhoto.as_view()),
    path('get/list/profile/to/user/id/<int:id>/', GetListProfilePhotosToUserId.as_view()),
    path('get/profile/photo/to/user/<int:id>/', GetProfilePhotoToId.as_view()),
    path('get/list/comment/to/profile/photo/<int:id>/', GetListCommentToProfilePhoto.as_view()),
    path('create/comment/profile/photo/', CreateCommentProfilePhoto.as_view()),
    path('delete/comment/profile/photo/<int:id>/', DeleteCommentProfilePhoto.as_view()),
    path('get/comment/profile/photo/<int:id>/', GetCommentToId.as_view()),
    path('get/list/profile/photos/to/user/', GetListProfilePhotosToUser.as_view()),

]
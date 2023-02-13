from django.contrib import admin

from app.user.models import Profile, Friend, ProfilePhoto, CommentProfilePhoto


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone', 'nickname')


class FriendAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'friend')


class ProfilePhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'img')


class CommentProfilePhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'comment', 'photo')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Friend, FriendAdmin)
admin.site.register(ProfilePhoto, ProfilePhotoAdmin)
admin.site.register(CommentProfilePhoto, CommentProfilePhotoAdmin)

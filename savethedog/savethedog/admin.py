from django.contrib import admin

from rottweiler.models import Announce, EnhancedUser, Conversation, SocialType, SocialNetwork, AnnouncePicture, Animal, AnimalType
# Register your models here.

admin.site.register(Announce)
admin.site.register(EnhancedUser)
admin.site.register(Animal)
admin.site.register(AnimalType)
admin.site.register(Conversation)
admin.site.register(SocialType)
admin.site.register(SocialNetwork)
admin.site.register(AnnouncePicture)

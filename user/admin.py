from django.contrib import admin
from .models import User as UserModel
from .models import UserProfile as UserProfileModel
from .models import UserType as UserTypeModel

# Register your models here.
admin.site.register(UserModel)
admin.site.register(UserProfileModel)
admin.site.register(UserTypeModel)
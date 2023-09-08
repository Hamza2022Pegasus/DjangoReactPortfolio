"""Module Admin for registering models inside app"""
from django.contrib import admin
from .models import IntroBannerHero,AboutMeSeciton,Services,Technologies,Jobs,Contact,SMLinks

# Register your models here.
admin.site.register(IntroBannerHero)
admin.site.register(AboutMeSeciton)
admin.site.register(Services)
admin.site.register(Technologies)
admin.site.register(Jobs)
admin.site.register(Contact)
admin.site.register(SMLinks)

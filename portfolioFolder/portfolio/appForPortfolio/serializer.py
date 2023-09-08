"""Module to serialize models data for views to change data type"""
from rest_framework import serializers
from .models import IntroBannerHero,AboutMeSeciton,Services,Technologies,Jobs,Contact,SMLinks

class IntroBannerSerializer(serializers.ModelSerializer):
    """Class represents serializer """

    class Meta:
        """Class represents meta for parent"""
        model = IntroBannerHero
        fields = '__all__'

class AboutMeSerializer(serializers.ModelSerializer):
    """Class represents serializer"""

    class Meta:
        """Class represents meta for parent"""
        model = AboutMeSeciton
        fields = '__all__'

class ServicesSerializer(serializers.ModelSerializer):
    """Class represents serializer"""

    class Meta:
        """Class meta for parent"""
        model = Services
        fields = '__all__'
class TechnologiesSerializer(serializers.ModelSerializer):
    """Class represents serializer"""

    class Meta:
        """Class meta for parent"""
        model = Technologies
        fields = '__all__'

class JobsSerializer(serializers.ModelSerializer):
    """Class represents serializer"""

    class Meta:
        """Class meta for parent"""
        model = Jobs
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    """Class represents serializer"""

    class Meta:
        """Class meta for parent"""
        model = Contact
        fields = '__all__'

class SMLinksSerializer(serializers.ModelSerializer):
    """Class represents serializer"""

    class Meta:
        """Class meta for parent"""
        model = SMLinks
        fields = '__all__'

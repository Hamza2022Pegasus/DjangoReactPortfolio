"""Module provides views for this app"""

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from django.views.decorators.csrf import ensure_csrf_cookie
from django.conf import settings
from .models import IntroBannerHero,AboutMeSeciton,Services,Technologies,Jobs, Contact, SMLinks
from .serializer import IntroBannerSerializer,AboutMeSerializer,ServicesSerializer,TechnologiesSerializer,JobsSerializer,ContactSerializer,SMLinksSerializer,ProposalEmailSerializer

class GetIntroDetails(APIView):
    """Class for API views for this section"""

    def get(self,request,format=None):
        """Function to handle get request"""
        intro_details = IntroBannerHero.objects.all()
        serializer = IntroBannerSerializer(intro_details,many=True)
        return Response(serializer.data)

class GetAboutDetails(APIView):
    """Class for API Views for this section"""

    def get(self,request,format=None):
        """function to handle get request"""
        aboutme_details = AboutMeSeciton.objects.all()
        serializer = AboutMeSerializer(aboutme_details,many=True)
        return Response(serializer.data)

class GetServicesDetails(APIView):
    """Class for API views for this section"""

    def get(self,request,format=None):
        """Function to handle get request"""
        services_details = Services.objects.all()
        serializer = ServicesSerializer(services_details,many=True)
        return Response(serializer.data)

class GetTechnologiesDetails(APIView):
    """Class for API views for this section"""

    def get(self,request,format=None):
        """Function to handle get request"""
        technologies_details = Technologies.objects.all()
        serializer = TechnologiesSerializer(technologies_details,many=True)
        return Response(serializer.data)

class GetJobsDetails(APIView):
    """Class for API views for this section"""

    def get(self,request,format=None):
        """Function to handle get request"""
        jobs_details = Jobs.objects.all()
        serializer = JobsSerializer(jobs_details,many=True)
        return Response(serializer.data)

class GetContactDetails(APIView):
    """Class for API views for this section"""

    def get(self,request,format=None):
        """Function to handle get request"""
        contact_details = Contact.objects.all()
        serializer = ContactSerializer(contact_details,many=True)
        return Response(serializer.data)

class GetSMLinksDetails(APIView):
    """Class for API views for this section"""

    def get(self,request,format=None):
        """Function to handle get request"""
        smlinks_details = SMLinks.objects.all()
        serializer = SMLinksSerializer(smlinks_details,many=True)
        return Response(serializer.data)

@ensure_csrf_cookie
@api_view(['POST',])
def proposal(request):
    """Proposal for email"""
    if request.method == "POST":
        serializer = ProposalEmailSerializer(data=request.data)
        if serializer.is_valid():
            clientname = request.data.get('ClientName',"Hahahaha")
            recipient = request.data.get('Recipient',"kldjfalksd@gmail.com")
            message = request.data.get('Message',"skldnflkasndfklnalksdnfklasndfkln")
            actualsender = settings.EMAIL_HOST_USER
            # send mail
            send_mail(
                'Contact Form mail from ' + clientname,
                message,
                actualsender,
                [recipient,actualsender],
            )
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

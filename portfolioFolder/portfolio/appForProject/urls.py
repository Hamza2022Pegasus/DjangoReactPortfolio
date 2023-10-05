"""Module to create url patterns for this app"""

from django.urls import path
from . import views

urlpatterns = [
    path('intro-details', views.GetIntroDetails.as_view(), name="IntroBanner"),
    path('about-details', views.GetAboutDetails.as_view(), name="AboutDetails"),
    path('services-details', views.GetServicesDetails.as_view(), name="ServicesDetails"),
    path('technologies-details', views.GetTechnologiesDetails.as_view(), name="TechnologiesDetails"),
    path('jobs-details', views.GetJobsDetails.as_view(), name="JobsDetails"),
    path('contacts-details', views.GetContactDetails.as_view(), name="ContactsDetails"),
    path('social-details', views.GetSMLinksDetails.as_view(), name="SocialDetails"),
    path('send_email',views.proposal, name="sendEmail")
]

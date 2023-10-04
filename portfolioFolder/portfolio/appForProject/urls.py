"""Module to create url patterns for this app"""

from django.urls import path
from . import views

urlpatterns = [
    path('intro-details', views.GetIntroDetails.as_view(), name="IntroBanner"),
    path('about-details', views.GetAboutDetails.as_view(), name="IntroBanner"),
    path('services-details', views.GetServicesDetails.as_view(), name="IntroBanner"),
    path('technologies-details', views.GetTechnologiesDetails.as_view(), name="IntroBanner"),
    path('jobs-details', views.GetJobsDetails.as_view(), name="IntroBanner"),
    path('contacts-details', views.GetContactDetails.as_view(), name="IntroBanner"),
    path('social-details', views.GetSMLinksDetails.as_view(), name="IntroBanner"),
    path('send_email',views.proposal, name="sendEmail")
]

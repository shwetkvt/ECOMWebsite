from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUS"),
    path("contact", views.contact, name="ContactUs"),
    path("tracker/", views.track, name="TrackingStatus"),
    path("productview/", views.productview, name="ProductView"),
    path("Search/", views.search, name="Search"),
    path("checkout/", views.checkout, name="CheckOut"),
    ]

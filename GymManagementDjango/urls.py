"""GymManagementDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from gym.views import *
from django.conf import settings
from gym import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("admin_login", admin_login, name="admin_login"),
    path("contact", contact, name="contact"),
    path("member_enquiry/", member_enquiry, name="member_enquiry"),  # Add this line
    path("member-queries/", views.member_queries, name="member_queries"),
    path("admin_home", admin_home, name="admin_home"),
    path("member_home", member_home, name="member_home"),
    path("addEnquiry", addEnquiry, name="addEnquiry"),
    path("viewEnquiry", viewEnquiry, name="viewEnquiry"),
    path("member_plan/", views.member_plans, name="member_plan"),
    path("edit_Enquiry/<int:pid>", edit_Enquiry, name="edit_Enquiry"),
    path("delete_Enquiry/<int:pid>", delete_Enquiry, name="delete_Enquiry"),
    path("addPlan", addPlan, name="addPlan"),
    path("viewPlan", viewPlan, name="viewPlan"),
    path("edit_Plan/<int:pid>", edit_Plan, name="edit_Plan"),
    path("delete_Plan/<int:pid>", delete_Plan, name="delete_Plan"),
    path("addEquipment", addEquipment, name="addEquipment"),
    path("viewEquipment", viewEquipment, name="viewEquipment"),
    path("edit_Equipment/<int:pid>", edit_Equipment, name="edit_Equipment"),
    path("delete_Equipment/<int:pid>", delete_Equipment, name="delete_Equipment"),
    path("addMember", addMember, name="addMember"),
    path("member/login/", views.member_login, name="member_login"),
    path("viewMember", viewMember, name="viewMember"),
    path("edit_Member/<int:pid>", edit_Member, name="edit_Member"),
    path("delete_Member/<int:pid>", delete_Member, name="delete_Member"),
    path("unread_queries", unread_queries, name="unread_queries"),
    path("read_queries", read_queries, name="read_queries"),
    path("view_queries/<int:pid>", view_queries, name="view_queries"),
    path("delete_contact/<int:pid>", delete_contact, name="delete_contact"),
    path("changePassword", changePassword, name="changePassword"),
    path("logout", Logout, name="logout"),
    path("home/", views.home, name="home"),
    path("<str:room>/", views.room, name="room"),
    path("home/checkview/", views.checkview, name="checkview"),
    path("send", views.send, name="send"),
    path("getMessages/<str:room>/", views.getMessages, name="getMessages"),
]

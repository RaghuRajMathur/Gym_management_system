"""GymManagementDjango URL Configuration"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from gym import views

# Custom 404 handler
handler404 = "gym.views.custom_404_view"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("admin_login/", views.admin_login, name="admin_login"),
    path("contact/", views.contact, name="contact"),
    path("member_enquiry/", views.member_enquiry, name="member_enquiry"),
    path("member-queries/", views.member_queries, name="member_queries"),
    path("personalized_diet_plan/", views.personalized_diet_plan, name="personalized_diet_plan"),
    path("admin_home/", views.admin_home, name="admin_home"),
    path("member_home/", views.member_home, name="member_home"),
    path("failure/", views.failure, name="failure"),
    path("addEnquiry/", views.addEnquiry, name="addEnquiry"),
    path("viewEnquiry/", views.viewEnquiry, name="viewEnquiry"),
    path("member_plan/", views.member_plans, name="member_plan"),
    path("edit_Enquiry/<int:pid>/", views.edit_Enquiry, name="edit_Enquiry"),
    path("delete_Enquiry/<int:pid>/", views.delete_Enquiry, name="delete_Enquiry"),
    path("addPlan/", views.addPlan, name="addPlan"),
    path("viewPlan/", views.viewPlan, name="viewPlan"),
    path("edit_Plan/<int:pid>/", views.edit_Plan, name="edit_Plan"),
    path("delete_Plan/<int:pid>/", views.delete_Plan, name="delete_Plan"),
    path("addEquipment/", views.addEquipment, name="addEquipment"),
    path("viewEquipment/", views.viewEquipment, name="viewEquipment"),
    path("edit_Equipment/<int:pid>/", views.edit_Equipment, name="edit_Equipment"),
    path("delete_Equipment/<int:pid>/", views.delete_Equipment, name="delete_Equipment"),
    path("addMember/", views.addMember, name="addMember"),
    path("member/login/", views.member_login, name="member_login"),
    path("viewMember/", views.viewMember, name="viewMember"),
    path("edit_Member/<int:pid>/", views.edit_Member, name="edit_Member"),
    path("delete_Member/<int:pid>/", views.delete_Member, name="delete_Member"),
    path("unread_queries/", views.unread_queries, name="unread_queries"),
    path("read_queries/", views.read_queries, name="read_queries"),
    path("view_queries/<int:pid>/", views.view_queries, name="view_queries"),
    path("delete_contact/<int:pid>/", views.delete_contact, name="delete_contact"),
    path("changePassword/", views.changePassword, name="changePassword"),
    path("logout/", views.Logout, name="logout"),
    path("blog_section/", views.blog_section, name="blog_section"),
    path("blogs/", views.all_blogs, name="all_blogs"),
    path("add_blog/", views.add_blog, name="add_blog"),
    path("latest_blogs_ajax/", views.latest_blogs_ajax, name="latest_blogs_ajax"),
    path("blog_detail/<int:blog_id>/", views.blog_detail, name="blog_detail"),
    path("home/", views.home, name="home"),
    path("checkview/", views.checkview, name="checkview"),
    path("send/", views.send, name="send"),
    path("getMessages/<str:room>/", views.getMessages, name="getMessages"),
    path("<str:room>/", views.room, name="room"),  # Keep this at the end
]

# Static files handling
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

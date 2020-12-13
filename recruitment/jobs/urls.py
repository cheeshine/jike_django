from django.conf.urls import url
from django.urls import path
from django.conf import settings

from jobs import views

urlpatterns = [
    # 职位列表
    url(r"^joblist/", views.joblist, name="joblist"),

    # # 管理员创建 HR 账号的 页面:
    # path('create_hr_user/', views.create_hr_user, name='create_hr_user'),
    #
    # 职位详情
    url(r'^job/(?P<job_id>\d+)/$', views.detail, name='detail'),
    #
    # path('resume/add/', views.ResumeCreateView.as_view(), name='resume-add'),
    # path('resume/<int:pk>/', views.ResumeDetailView.as_view(), name='resume-detail'),
    #
    # path('sentry-debug/', trigger_error),
    #
    # 首页自动跳转到 职位列表
    url(r"^$", views.joblist, name="name"),
]

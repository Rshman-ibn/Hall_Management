from django.urls import path
from .import views

urlpatterns=[

path('index/',views.index,name='index'),
path('home/',views.HomeView,name='home'),
path('',views.HomeView,name='home'),
path('frmContact/',views.Contact,name='frmContact'),
path('frmGeneralInstructions/',views.GeneralInstructions,name='GeneralInstructions'),
path('notice/',views.generalInstructionsform,name="notice"),
path('frmStudentManual/',views.frmStudentManual,name='frmStudentManual'),
path('frmUserManual/',views.frmUserManual,name='frmUserManual'),
path('newallocation/',views.newallocation,name='newallocation'),
path('frmLogin/',views.frmLogin,name='frmLogin'),
path('register/',views.register,name='register'),
path('logout/',views.forlogout,name='logout'),
path('ami/',views.adminpanel,name='adminpanel'),
path('profile',views.profile,name='profile'),
path('profile_show/',views.profile_show,name='profile_show'),
path('studentupdate/<int:pid>',views.newup,name='studentupdate'),
path('studentOut/<int:pid>',views.studentOut,name='studentOut'),
]

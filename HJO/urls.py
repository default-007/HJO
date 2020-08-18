from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('about/', views.about, name='about'),
    path('appointment/', views.appointment, name='appointment'),
    path('blog/', views.blog, name='blog'),
    path('blog/<id>', views.bdetail, name='bdetail'),
    path('services/', views.services, name='services'),
    path('criminal/', views.criminal, name='criminal'),
    path('civil/', views.civil, name='civil'),
    path('cyber/', views.cyber, name='cyber'),
    path('probate/', views.probate, name='probate'),
    path('corporate/', views.corporate, name='corporate'),
    path('conveyancing/', views.conveyancing, name='conveyancing'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('testimonial/', views.testimonial, name='testimonial'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
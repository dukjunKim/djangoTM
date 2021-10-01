from django.urls import path

from . import views
#from blog.views import tbkt14ListAPI

urlpatterns = [
    path('tb_kt10', views.TmabTbKt10View.as_view()),
    path('tb_kt14', views.TmabTbKt14View.as_view()),
    path('tb_kt10/<int:kt10_id>', views.TmabTbKt10View.as_view()),
    path('tb_kt14/<int:kt14_id>', views.TmabTbKt14View.as_view())
  #  path('tb_kt14_list/', views.address_list),
   # path('tb_kt14_list/<pk>', views.address),
    #path('api/blog/', tbkt14ListAPI.as_view()),
]
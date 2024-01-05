from django.urls import path

from . import views
from . import startup

urlpatterns = [
    path('', views.home, name='home'), #faq
    path('item/<int:i_id>', views.item), #html with the item
    path('buy/<int:p_id>', views.create_checkout_session), #get session for some item 

    path('config/', views.stripe_config), 
    path('success/', views.success),
    path('cancelled/', views.CancelledView.as_view()),
    path('webhook/', views.stripe_webhook), # new

]

startup.main()
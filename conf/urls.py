
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from appfood import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path(
        'eda/category/<int:category_id>', 
        views.get_foods_by_category
    ),
    path('eda/detail/<int:food_id>', views.food_detail_view),
    path('eda/card/add/<int:food_id>', views.add_to_card),
    path('eda/card/del/<int:food_id>', views.del_to_card),
    path('eda/card/remove/<int:food_id>', views.remove_to_card),
    path('eda/card/view/', views.card_view),
    path('order/add/', views.order_add),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

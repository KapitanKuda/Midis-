from .views import *
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from .decorators import check_recaptcha



urlpatterns=[
    path('',message_list),
    path('new_reviews',check_recaptcha(ReviewCreate.as_view()), name='reviews_list_and_new'),
    path('table',AllInfo.as_view(), name='sort'),
    path('delete',clear_data),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

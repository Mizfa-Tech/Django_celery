from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # urls admin
    path('admin/', admin.site.urls),

    # urls feedback
    path('', include('feedback.urls'))
]

# ----------------------------------------- Config Static -------------------------------------------------------------
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("credit_score.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    from debug_toolbar.toolbar import debug_toolbar_urls  # type: ignore

    urlpatterns = [
        *urlpatterns,
    ] + debug_toolbar_urls()

from blog.urls import router as blog_router
from django.contrib import admin
from django.urls import include, re_path

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    # blog.urlsをincludeする
    re_path(r"^api/", include(blog_router.urls)),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    FollowRequestViewSet,
    PostViewSet,
    PostMediaViewSet,
    ReportPostViewSet,
)

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("post", PostViewSet)
router.register("postmedia", PostMediaViewSet)
router.register("reportpost", ReportPostViewSet)
router.register("followrequest", FollowRequestViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

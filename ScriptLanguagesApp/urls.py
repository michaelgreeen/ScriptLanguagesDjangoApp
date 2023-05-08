from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as django_views
from .forms import UserLoginForm
from .views import (
    IndexView,
    RegisterView,
    CreatedSetsView,
    AddSetView,
    DetailsView,
    CommentAddView,
    CommentDeleteView,
    PCSetDeleteView,
    PCEditView,
    RatePCView,
    already_rated
)
from .sitemaps import AddSetViewSitemap, CommentAddViewSitemap, CommentDeleteViewSitemap, CreatedSetsSitemap, DetailsViewSitemap, IndexSitemap, PCEditViewSitemap, PCSetDeleteViewSitemap, RatePCViewSitemap, RegisterSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'index': IndexSitemap,
    'register': RegisterSitemap,
    'createdsets': CreatedSetsSitemap,
    'details': DetailsViewSitemap,
    'ratepc': RatePCViewSitemap,
    'addset': AddSetViewSitemap,
    'commentadd': CommentAddViewSitemap,
    'commentdelete': CommentDeleteViewSitemap,
    'pcsetdelete': PCSetDeleteViewSitemap,
    'pcedit': PCEditViewSitemap,
}

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', RegisterView.as_view(), name='register'),
    path('created-sets/', CreatedSetsView.as_view(), name='created-sets'),
    path('add-set/', AddSetView.as_view(), name='add-set'),
    path('details/<int:pc_id>/', DetailsView.as_view(), name='details'),
    path('login/', django_views.LoginView.as_view(template_name='registration/login.html', authentication_form=UserLoginForm), name='login'),
    path('add_comment/<int:pc_id>/', CommentAddView.as_view(), name='add-comment'),
    path('delete-comment/<int:comment_id>/', CommentDeleteView.as_view(), name='delete-comment'),
    path('delete-pc-set/<int:pc_id>/', PCSetDeleteView.as_view(), name='delete-pc-set'),
    path('edit-set/<int:pc_id>/', PCEditView.as_view(), name='edit-set'),
    path('rate-pc/<int:pc_id>/', RatePCView.as_view(), name='rate-pc'),
    path('already-rated/', already_rated, name='already-rated'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

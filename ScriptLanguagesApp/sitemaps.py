from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import *

class IndexSitemap(Sitemap):
    def items(self):
        return ['index']

    def location(self, item):
        return reverse(item)

class RegisterSitemap(Sitemap):
    def items(self):
        return ['register']

    def location(self, item):
        return reverse(item)

class CreatedSetsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    def items(self):
        return PC.objects.all()

    def location(self, obj):
        return reverse('created-sets')
    
class DetailsViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return PC.objects.all()

    def location(self, obj):
        return reverse('details', args=[obj.id])

class RatePCViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return PC.objects.all()

    def location(self, obj):
        return reverse('rate-pc', args=[obj.id])

class AddSetViewSitemap(Sitemap):
    def items(self):
        return ['add-set']

    def location(self, item):
        return reverse(item)

class CommentAddViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return Comment.objects.all()

    def location(self, obj):
        return reverse('details', args=[obj.pc_id])
    
class CommentDeleteViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return Comment.objects.all()

    def location(self, obj):
        return reverse('details', args=[obj.pc_id])

class PCSetDeleteViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return PC.objects.all()

    def location(self, obj):
        return reverse('created-sets')

class PCEditViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return PC.objects.all()

    def location(self, obj):
        return reverse('created-sets')
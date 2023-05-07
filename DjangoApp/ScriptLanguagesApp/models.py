from django.db import models
from django.contrib.auth.models import User
from django import template
register = template.Library()
@register.filter
def average_rating(pc):
    ratings = pc.ratings.all().values_list('rating', flat=True)
    if not ratings:
        return 'Brak ocen'
    return sum(ratings) / len(ratings)

class PC(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nazwa zestawu")
    cpu = models.CharField(max_length=100,verbose_name="Procesor")
    gpu = models.CharField(max_length=100,verbose_name="Karta graficzna")
    ram = models.CharField(max_length=100,verbose_name="Pamięć RAM")
    psu = models.CharField(max_length=100,verbose_name="Zasilacz")
    cpu_price = models.DecimalField(max_digits=8, decimal_places=2,verbose_name="Cena procesora")
    gpu_price = models.DecimalField(max_digits=8, decimal_places=2,verbose_name="Cena karty graficznej")
    ram_price = models.DecimalField(max_digits=8, decimal_places=2,verbose_name="Cena pamięci RAM")
    psu_price = models.DecimalField(max_digits=8, decimal_places=2,verbose_name="Cena zasilacza")
    ratings = models.ManyToManyField(User, through='PCRating')
    average_rating = models.FloatField(default=0, verbose_name="Średnia ocena", editable=False)

class PCRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pc = models.ForeignKey(PC, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    rated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'pc')

class Comment(models.Model):
    pc = models.ForeignKey(PC, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.pc.name} - {self.created_at}'
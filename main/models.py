from django.db import models
from django.urls import reverse


class Review(models.Model):
    title = models.CharField(verbose_name='Заглавие', max_length=20)
    text = models.TextField(verbose_name='Текст отзыва', null=True)
    phone = models.CharField(verbose_name='Номер телефона', max_length=15, null=True, blank=True)
    email = models.EmailField(verbose_name='Email', max_length=30, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def get_detailUrl(self):
        return reverse('rev_detail', kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return reverse('rev_list')

# Create your models here.

from django.db import models




class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Doctor(models.Model):
    """Врачи"""
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="doctors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ветеринарный врач"
        verbose_name_plural = "Ветеринарные врачи"



class Service(models.Model):
    """Услуга"""
    title = models.CharField("Название", max_length=100)
    doctors = models.ManyToManyField(Doctor, verbose_name="Ветеринарный врач", related_name="doctors")
    price = models.PositiveIntegerField("Цена", default=0,
                                         help_text="указывать сумму в рублях")
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

class Analysis(models.Model):
    """Анализ"""
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    price = models.PositiveIntegerField("Цена", default=0,
                                         help_text="указывать сумму в рублях")
    day = models.PositiveIntegerField("Сроки исполнения", default=0,
                                        help_text="указывать срок исполнения в днях")
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Анализ"
        verbose_name_plural = "Анализы"






# Create your models here.

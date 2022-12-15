from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
#Описание в админке
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
 # Основные типы полей
    # дата
    # models.DateField
    # models.DateTimeField
    # models.TimeField
    # # Числа
    # models.IntegerField
    # models.PositiveIntegerField
    # models.PositiveSmallIntegerField
    # models.FloatField
    # models.DecimalField
    # # Логический
    # models.BooleanField
    # # Байты (blob)
    # models.BinaryField
    # # Картинка
    # models.ImageField
    # # Файл
    # models.FileField
    # # url, email
    # models.URLField
    # models.EmailField
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=32, unique=True)
    text = models.TextField()
    description_detail = models.TextField(blank=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    price = models.IntegerField(null=True, blank=True)
    area_home = models.IntegerField(null=True, blank=True)
    # Связь с категорией
    # один - много
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Связь с тегом
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='posts', null=True, blank=True)

    # Метод проверки картинки
    def has_image(self):
        return bool(self.image)

    # Метод разбивает цену на разряды
    def price_str(self):
        return '{0:,}'.format(self.price).replace(',', ' ')

    def some_method(self):
        return 'hello from method'

    def __str__(self):
        return f'{self.name}, category: {self.category.name}'



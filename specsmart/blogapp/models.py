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

class ActiveManager(models.Manager):

    def get_queryset(self):
        all_objects = super().get_queryset()
        return all_objects.filter(is_active=True)

class IsActiveMixin(models.Model):
    objects = models.Manager()
    active_objects = ActiveManager()
    is_active = models.BooleanField(default=False)

    class Meta:
        abstract = True

class TimeStamp(models.Model):
    """
    Abstract - для нее не создаются новые таблицы
    данные хранятся в каждом наследнике
    """
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Tag(IsActiveMixin):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name


class Post(TimeStamp, IsActiveMixin):
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
    rating = models.PositiveSmallIntegerField(default=1)

    # Метод проверки картинки
    def has_image(self):
        return bool(self.image)

    # Метод разбивает цену на разряды
    def price_str(self):
        return '{0:,}'.format(self.price).replace(',', ' ')

    def some_method(self):
        return 'hello from method'

    def display_tags(self):
        tags = self.tags.all()
        result = ';'.join([item.name for item in tags])
        return result

    def __str__(self):
        return f'{self.name}, category: {self.category.name}'



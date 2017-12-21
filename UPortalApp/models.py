from django.db import models


# Create your models here.
class Author(models.Model):
    def __str__(self):
        return self.nameRus + ' ( ' + self.nameEng + ' )'

    nameRus = models.CharField(max_length=200, null=False, verbose_name='ФИО на русском')
    nameEng = models.CharField(max_length=200, null=False, verbose_name='full name in english')

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Place_of_publication(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, verbose_name='Название')
    type_of_place = models.CharField(max_length=255, verbose_name='Тип')
    publishing_house = models.CharField(max_length=255, verbose_name='Издательство')
    place_of_publish = models.CharField(max_length=255, verbose_name='Место издания')
    description = models.TextField(verbose_name='Короткое описание (до 2000 знаков)', max_length=2000)
    list_of_links = models.TextField(verbose_name='Список ссылок')

    class Meta:
        verbose_name = "Место публикации"
        verbose_name_plural = "Места публикации"


class Publication(models.Model):
    title = models.CharField(null=False, max_length=255, verbose_name="Название")
    date_of_publication = models.DateField(verbose_name="Дата публикации")
    language_of_publication = models.CharField(max_length=255, verbose_name="Язык публикации")
    description = models.TextField(verbose_name="Короткое описание")
    type_of_publication = models.CharField(max_length=255, verbose_name="Тип публикации ")
    type_of_index = models.CharField(max_length=255, verbose_name="Типы индексации")
    place_of_publication = models.ForeignKey(Place_of_publication, on_delete=models.CASCADE)
    pages = models.CharField(max_length=255, verbose_name="Страницы публикации (с X по Y)")
    links = models.TextField(verbose_name="Список ссылок")

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"

    def __str__(self):
        return self.title


class Files_of_publication(models.Model):
    publication = models.ForeignKey(Publication, related_name='file_pub', on_delete=models.CASCADE)
    file = models.FileField(verbose_name="Файлы публикации")


class Files_of_place(models.Model):
    place = models.ForeignKey(Place_of_publication, related_name='file_place', on_delete=models.CASCADE)
    file = models.FileField()

class Author_of_publication(models.Model):
    author = models.ForeignKey(Author, related_name='author_of_pub', on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, related_name='publication', on_delete=models.CASCADE)
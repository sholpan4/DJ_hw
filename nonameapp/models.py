from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50,
                            db_index=True,
                            verbose_name='Жанр',
                            unique=True
                            )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.pk}/'

    class Meta:
        verbose_name_plural = 'Жанры'
        verbose_name = 'Жанр'
        ordering = ['name']


class Film(models.Model):
    genre = models.ForeignKey("Genre", null=True, on_delete=models.PROTECT, verbose_name='Жанр')
    title = models.CharField(max_length=100,
                             verbose_name='Название фильма',
                             null=False
                             )
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    year = models.IntegerField(max_length=4,
                               verbose_name='Год выпуска',
                               default=1960,
                               )
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Новая запись')
    updated = models.DateTimeField(auto_now=True, db_index=True, verbose_name='Изменено')

    def __str__(self):
        return f'{self.title}'


    class Meta:
        verbose_name_plural = 'Фильмы'
        verbose_name = 'Фильм'
        ordering = ['-year', 'title']
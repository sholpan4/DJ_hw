# Generated by Django 5.0 on 2023-12-06 17:07

import bboard.models
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Рубрика',
                'verbose_name_plural': 'Рубрики',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Bb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('b', 'Куплю'), ('s', 'Продам'), ('c', 'Обменяю')], default='s', max_length=1, verbose_name='Тип объявления')),
                ('title', models.CharField(error_messages={'invalid': 'Это мы сами написали'}, max_length=50, validators=[django.core.validators.RegexValidator(regex='^.{4,}$')], verbose_name='Товар')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=999999999, max_length=8, verbose_name='Цена')),
                ('is_active', models.BooleanField(default=bboard.models.is_active_default)),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')),
                ('updated', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Изменено')),
                ('rubric', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bboard.rubric', verbose_name='Рубрика')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
                'ordering': ['-published', 'title'],
            },
        ),
    ]

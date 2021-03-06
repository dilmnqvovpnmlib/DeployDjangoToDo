# Generated by Django 2.2.12 on 2020-05-17 02:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('enable', models.BooleanField(default=True, verbose_name='有効')),
                ('order', models.IntegerField(verbose_name='表示順')),
                ('name', models.CharField(max_length=256, verbose_name='名称')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tag',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('enable', models.BooleanField(default=True, verbose_name='有効')),
                ('content', models.CharField(max_length=256, verbose_name='内容')),
                ('completed', models.DateTimeField(blank=True, null=True, verbose_name='完了日時')),
                ('tags', models.ManyToManyField(to='todos.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='登録者')),
            ],
            options={
                'verbose_name': 'Todo',
                'verbose_name_plural': 'Todo',
                'ordering': ['-created'],
            },
        ),
    ]

# Generated by Django 3.2.9 on 2021-12-05 06:47

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courseapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('content', ckeditor.fields.RichTextField(null=True)),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('type', models.CharField(choices=[('notice', '공지사항'), ('data', '강의자료'), ('board', '토론게시판')], max_length=10, null=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='board', to='courseapp.course')),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='board', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

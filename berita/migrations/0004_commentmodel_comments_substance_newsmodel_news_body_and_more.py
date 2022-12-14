# Generated by Django 4.1 on 2022-10-27 15:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0003_rename_comment_commentmodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='comments_substance',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='news_body',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='news_source',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]

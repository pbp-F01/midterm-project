# Generated by Django 4.1 on 2022-11-02 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("landing", "0001_initial"),
        ("reviewUMKM", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="stars",
            new_name="rating",
        ),
        migrations.AlterField(
            model_name="review",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews",
                to="landing.profile",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="comment",
            field=models.TextField(max_length=2048),
        ),
        migrations.AlterField(
            model_name="review",
            name="review_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-25 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product_app', '0001_initial'),
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.restaurant'),
        ),
        migrations.AddField(
            model_name='product',
            name='stocks',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='product_app.stock'),
        ),
    ]

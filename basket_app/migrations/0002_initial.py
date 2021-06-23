# Generated by Django 3.2.4 on 2021-06-20 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('basket_app', '0001_initial'),
        ('product_app', '0001_initial'),
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.customer'),
        ),
        migrations.AddField(
            model_name='basket',
            name='products',
            field=models.ManyToManyField(to='product_app.Product'),
        ),
    ]
# Generated by Django 3.0.7 on 2020-06-23 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0009_remove_pizza_price5'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.TextField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='orders.Address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

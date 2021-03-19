# Generated by Django 3.0.7 on 2020-06-26 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='orders.Status'),
        ),
    ]
# Generated by Django 3.0.7 on 2020-06-29 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_auto_20200626_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='state',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='orders', to='orders.State'),
        ),
    ]

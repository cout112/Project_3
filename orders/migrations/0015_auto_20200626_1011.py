# Generated by Django 3.0.7 on 2020-06-26 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20200626_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='orders.Status'),
        ),
    ]

# Generated by Django 3.0.7 on 2020-06-26 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_auto_20200626_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='orders.Status'),
        ),
    ]

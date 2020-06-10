# Generated by Django 3.0.6 on 2020-06-10 07:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0012_auto_20200609_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.UserDetail', verbose_name='Customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.ServiceDetail', verbose_name='Service Provided'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='provider',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='website.UserDetail', verbose_name='Service Provider'),
        ),
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.IntegerField(choices=[(0, 'Food Delivery'), (1, 'Assignment Complete'), (2, 'Tutor'), (3, 'Other Delivery')], verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='servicedetail',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Provider', verbose_name='Service Provider'),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='account',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 16:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nadine', '0026_bill_in_progress'),
    ]

    operations = [
        # Rename the old Membership model
        migrations.RenameModel(
            old_name='Membership',
            new_name='OldMembership',
        ),
        migrations.AlterModelOptions(
            name='oldmembership',
            options={'ordering': ['start_date'], 'verbose_name': 'OldMembership', 'verbose_name_plural': 'OldMemberships'},
        ),
        migrations.AlterField(
            model_name='oldmembership',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bill',
            name='membership',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nadine.OldMembership'),
        ),

        # Rename old Bill model
        migrations.RenameModel(
            old_name='Bill',
            new_name='OldBill',
        ),
        migrations.AlterField(
            model_name='oldbill',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='old_bill', to=settings.AUTH_USER_MODEL),
        ),

    ]

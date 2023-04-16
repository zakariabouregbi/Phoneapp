# Generated by Django 3.2.6 on 2022-04-21 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='product_owner',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, related_name='ownerproduct', to='Accounts.account'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Accepted', 'accepted'), ('Cenceled', 'Cenceled'), ('Completed', 'Completed')], default='New', max_length=10),
        ),
    ]

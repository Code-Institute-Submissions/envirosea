# Generated by Django 3.0.8 on 2020-07-28 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Trips',
        ),
        migrations.AlterModelOptions(
            name='trips',
            options={'verbose_name_plural': 'Trips'},
        ),
        migrations.RemoveField(
            model_name='booking',
            name='category',
        ),
        migrations.AddField(
            model_name='booking',
            name='trips',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookings.Trips'),
        ),
    ]

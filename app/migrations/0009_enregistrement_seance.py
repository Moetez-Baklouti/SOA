# Generated by Django 4.0 on 2021-12-13 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_enregistrement'),
    ]

    operations = [
        migrations.AddField(
            model_name='enregistrement',
            name='seance',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='app.seance'),
            preserve_default=False,
        ),
    ]

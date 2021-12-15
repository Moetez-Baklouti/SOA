# Generated by Django 4.0 on 2021-12-13 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_groupe_etudiant_groupe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travail_Rendre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('date_lancement', models.DateTimeField()),
                ('date_retour', models.DateTimeField()),
                ('nature', models.CharField(max_length=50)),
                ('descriptif', models.CharField(max_length=100)),
            ],
        ),
    ]
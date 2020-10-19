# Generated by Django 3.1.2 on 2020-10-18 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passagens', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passagem',
            name='classe_viagem',
            field=models.CharField(choices=[('ECONOMICA', 'Econômica'), ('EXECUTIVA', 'Executiva'), ('PRIMEIRA_CLASSE', 'Primeira Classe')], default=0, max_length=20),
        ),
    ]
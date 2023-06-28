# Generated by Django 4.2.2 on 2023-06-16 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receta',
            old_name='ingresantes',
            new_name='ingredientes',
        ),
        migrations.AlterField(
            model_name='comentario',
            name='texto',
            field=models.TextField(help_text='Comentario', verbose_name='Comentario'),
        ),
    ]
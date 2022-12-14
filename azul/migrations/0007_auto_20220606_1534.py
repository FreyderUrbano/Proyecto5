# Generated by Django 3.2 on 2022-06-06 20:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('azul', '0006_remove_case_exte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='detail',
            field=models.CharField(max_length=500, verbose_name='Detalle del caso'),
        ),
        migrations.AlterField(
            model_name='case',
            name='email',
            field=models.CharField(max_length=500, verbose_name='Mensaje de rescate'),
        ),
        migrations.AlterField(
            model_name='case',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Empresa'),
        ),
        migrations.AlterField(
            model_name='case',
            name='nitempresa',
            field=models.IntegerField(max_length=10, verbose_name='Nit Empresa'),
        ),
        migrations.AlterField(
            model_name='case',
            name='rams',
            field=models.CharField(blank=True, max_length=100, verbose_name='N. RANSOMWARE'),
        ),
        migrations.AlterField(
            model_name='case',
            name='ransomware',
            field=models.CharField(choices=[('Ninguno', 'Ninguno'), ('WannaCry', 'WannaCry'), ('Locky', 'Locky'), ('Bad Rabbit', 'Bad Rabbit'), ('Ryuk', 'Ryuk'), ('Shade/Troldesh', 'Shade/Troldesh'), ('Jigsaw', 'Jigsaw'), ('CryptoLocker', 'CryptoLocker'), ('Petya', 'Petya'), ('GandCrab 5.2', 'GandCrab 5.2'), ('GoldenEye', 'GoldenEye')], max_length=20, verbose_name='RANSOMWARE'),
        ),
        migrations.AlterField(
            model_name='case',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='case',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cases', to=settings.AUTH_USER_MODEL, verbose_name='Usuarios'),
        ),
        migrations.AlterField(
            model_name='case',
            name='wallet',
            field=models.CharField(max_length=100, verbose_name='Moneda'),
        ),
        migrations.CreateModel(
            name='Metho',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metodologia', to='azul.case', verbose_name='Casos')),
            ],
        ),
    ]

# Generated by Django 5.0.2 on 2024-02-27 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('fecha', models.DateField(null=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'usuarios',
            },
        ),
    ]

# Generated by Django 4.2.10 on 2024-02-18 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_lounge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('career_id', models.CharField(max_length=50)),
                ('day', models.CharField(max_length=20)),
                ('credits', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='lounge',
            name='capacity',
            field=models.CharField(max_length=10),
        ),
        migrations.CreateModel(
            name='Matter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('credits', models.IntegerField(max_length=10)),
                ('career_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.career')),
                ('lounge_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.lounge')),
                ('modality_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.modality')),
                ('semester_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.semester')),
            ],
        ),
    ]
# Generated by Django 2.2.3 on 2019-08-25 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DataSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('historical_data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dtype', models.CharField(choices=[('PP', 'Passport'), ('ID', 'Identity card'), ('OT', 'Other')], max_length=2)),
                ('doc_number', models.CharField(max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Customer')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='Professions',
            field=models.ManyToManyField(to='core.Profession'),
        ),
        migrations.AddField(
            model_name='customer',
            name='data_sheet',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.DataSheet'),
        ),
    ]

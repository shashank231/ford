# Generated by Django 3.2.8 on 2022-01-22 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('super', '0003_laptop'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=5)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='super.employee')),
                ('lap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='super.laptop')),
            ],
        ),
    ]
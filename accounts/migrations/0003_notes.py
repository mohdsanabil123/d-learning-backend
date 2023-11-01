# Generated by Django 4.2.4 on 2023-10-16 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_news_useraccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
                ('subject_class', models.IntegerField()),
                ('pdf_file', models.FileField(upload_to='PdfNotes')),
            ],
        ),
    ]

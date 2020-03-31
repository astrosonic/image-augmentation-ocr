# Generated by Django 3.0.4 on 2020-03-25 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0007_delete_ocr'),
    ]

    operations = [
        migrations.CreateModel(
            name='OCR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OCR_txt', models.FileField(upload_to='ocr/')),
                ('OCR_pdf', models.FileField(upload_to='ocr/')),
                ('original_image', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='image.Image')),
            ],
        ),
    ]

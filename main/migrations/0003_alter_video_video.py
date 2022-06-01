# Generated by Django 4.0.4 on 2022-04-22 16:25

from django.db import migrations, models
import main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_video_caption_alter_video_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='video/', validators=[main.validators.FileSizeValidator]),
        ),
    ]
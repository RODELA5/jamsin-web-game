# Generated by Django 4.1 on 2022-08-18 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("minesweeper", "0003_alter_minesweeper_board_alter_minesweeper_moves"),
    ]

    operations = [
        migrations.AddField(
            model_name="minesweeper",
            name="mines",
            field=models.JSONField(default=dict),
        ),
    ]
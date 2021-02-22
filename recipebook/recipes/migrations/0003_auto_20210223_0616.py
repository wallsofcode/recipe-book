# Generated by Django 3.1.7 on 2021-02-23 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='type', to='recipes.recipetype', verbose_name='Recipe Type'),
        ),
    ]
# Generated by Django 3.0.2 on 2020-03-06 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budgetapp', '0005_remove_depense_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='depense',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='budgetapp.Utilisateur'),
        ),
    ]

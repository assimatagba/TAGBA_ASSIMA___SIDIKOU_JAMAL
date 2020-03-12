# Generated by Django 3.0.2 on 2020-03-06 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budgetapp', '0003_remove_utilisateur_budget'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='depense',
            name='slug',
        ),
        migrations.AlterField(
            model_name='depense',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dep', to='budgetapp.Utilisateur'),
        ),
    ]
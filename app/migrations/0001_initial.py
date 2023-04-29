# Generated by Django 4.2 on 2023-04-29 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feesdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, null=True)),
                ('Register_No', models.IntegerField(null=True)),
                ('Year', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Four', 'Four')], max_length=50, null=True)),
                ('Department', models.CharField(choices=[('CSE', 'CSE'), ('EEE', 'EEE'), ('ECE', 'ECE'), ('MECH', 'MECH'), ('CIVIL', 'CIVIL')], max_length=50, null=True)),
                ('Previous_year_balance', models.IntegerField(null=True)),
                ('Admission_fees', models.IntegerField(null=True)),
                ('Tuition_fees', models.IntegerField(null=True)),
                ('Bus_fees', models.IntegerField(null=True)),
                ('Hostel_fees', models.IntegerField(null=True)),
                ('FGG', models.IntegerField(null=True)),
                ('PMSS', models.IntegerField(null=True)),
                ('Gover_quota', models.IntegerField(null=True)),
                ('Other_scholarships', models.IntegerField(null=True)),
                ('KET_scholarships', models.IntegerField(null=True)),
                ('Students_to_pay', models.IntegerField(null=True)),
                ('Total', models.IntegerField(null=True)),
            ],
        ),
    ]

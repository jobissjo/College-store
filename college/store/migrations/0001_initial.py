# Generated by Django 4.1.7 on 2023-03-03 14:45

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('age', models.CharField(max_length=3)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='male', max_length=6)),
                ('phone_number', models.CharField(max_length=13)),
                ('mail_id', models.CharField(max_length=30)),
                ('address', models.TextField()),
                ('department', models.CharField(choices=[('Computer Science', 'Computer Science'), ('Mathematics', 'Mathematics'), ('Physics', 'Physics'), ('Chemistry', 'chemistry'), ('Commerce', 'Commerce')], max_length=25)),
                ('courses', models.CharField(choices=[('Bachelor', 'Bachelor'), ('Master', 'Master'), ('M.Phil', 'M.Phil'), ('PhD', 'PhD')], max_length=25)),
                ('purpose', models.CharField(choices=[('Enquiry', 'Enquiry'), ('Place Order', 'Place Order'), ('Return', 'Return')], max_length=11)),
                ('materials_provide', multiselectfield.db.fields.MultiSelectField(choices=[('notebook', 'Debit Note Book'), ('pen', 'Pen'), ('exam_paper', 'Exam Papers')], max_length=50)),
            ],
        ),
    ]

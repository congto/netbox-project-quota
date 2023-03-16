# Generated by Django 4.1.5 on 2023-03-09 16:59

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import utilities.json


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dcim', '0167_module_status'),
        ('virtualization', '0034_standardize_description_comments'),
        ('ipam', '0063_standardize_description_comments'),
        ('extras', '0084_staging'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDevice',
            fields=[
                ('device_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dcim.device')),
                ('project', models.CharField(blank=True, default=None, max_length=20, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('dcim.device',),
        ),
        migrations.CreateModel(
            name='QuotaTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('template_name', models.CharField(max_length=100, null=True)),
                ('instances_quota', models.PositiveIntegerField(null=True)),
                ('vcpus_quota', models.PositiveIntegerField(null=True)),
                ('ram_quota', models.PositiveIntegerField(null=True)),
                ('ipaddr_quota', models.PositiveIntegerField(null=True)),
                ('device_quota', models.PositiveIntegerField(null=True)),
                ('comments', models.TextField(blank=True)),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('template_name',),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('name', models.CharField(max_length=100)),
                ('project_id', models.CharField(blank=True, max_length=100)),
                ('domain_name', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('device_count', models.IntegerField(blank=True, default=None, null=True)),
                ('ip_count', models.IntegerField(blank=True, default=None, null=True)),
                ('vm_count', models.IntegerField(blank=True, default=None, null=True)),
                ('ram_quota_used', models.CharField(default=None, max_length=100, null=True)),
                ('cpu_quota_used', models.CharField(default=None, max_length=100, null=True)),
                ('disk_quota_used', models.CharField(default=None, max_length=100, null=True)),
                ('device_quota_used', models.CharField(default=None, max_length=100, null=True)),
                ('vm_quota_used', models.CharField(default=None, max_length=100, null=True)),
                ('ip_quota_used', models.CharField(default=None, max_length=100, null=True)),
                ('comments', models.TextField(blank=True)),
                ('devices', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_device', to='dcim.device')),
                ('ipaddress', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_ipaddress', to='ipam.ipaddress')),
                ('quota_template', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_quota', to='netbox_project_quota.quotatemplate')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
                ('virtualmachine', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_vm', to='virtualization.virtualmachine')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]

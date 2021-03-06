#!usr/bin/env python
# coding:utf-8
from django.contrib import admin
from asset import models


class HostAdmin(admin.ModelAdmin):
    pass


class NetworkDeviceAdmin(admin.ModelAdmin):
    pass


class StorageAdmin(admin.ModelAdmin):
    pass


class TapeAdmin(admin.ModelAdmin):
    list_display = ('device_type', 'product_model', 'sn', 'be_from', 'ownership', 'manufacturers')
    search_fields = ('device_type', 'product_model', 'sn', 'be_from', 'manufacturers', 'ownership__name')
    list_filter = ('device_type', 'product_model', 'be_from')
    readonly_fields = ('born_time', )
    fieldsets = [
        (
            '资产基础信息', {
                'fields': [
                    'device_type', 'product_model', 'sn', 'be_from', 'ownership', 'purchase_date',
                    'manufacturers', 'contract', 'strongbox', 'tape_library_name', 'state'
                ],
                'classes': [
                    'suit-tab', 'suit-tab-general'
                ]
            }
        ),
        (
            '重要时间', {
                'fields': [
                    'born_time',
                ],
                'classes': ['suit-tab', 'suit-tab-general']
            }
        )
    ]
    suit_form_tabs = (('general', '基础信息'),)
    suit_form_includes = (
        ('asset/maintenance_log_table.html', 'bottom', 'maintenance'),
    )


class ToolsAdmin(admin.ModelAdmin):
    list_display = ('device_type', 'part_No', 'amount', 'inventory_num', 'color', 'size', 'be_from',
                    'ownership')
    list_filter = ('device_type', 'be_from', 'part_No')
    search_fields = ('device_type', 'be_from', 'part_No')
    readonly_fields = ('born_time',)


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('type', 'product_model', 'sn', 'amount', 'size', 'be_from', 'purchase_date')
    search_fields = ('type', 'product_model', 'size', 'be_from')
    readonly_fields = ('born_time', )
    list_filter = ('type', 'be_from')
    fieldsets = [
        ('基础资产信息', {'fields':
                        ['type', 'product_model', 'sn', 'amount', 'size', 'be_from', 'ownership', 'purchase_date',
                         'vendor', 'contract', 'location', 'using_status', 'maintenance_date', 'maintenance_section',
                         'abandon_time'],
                        # 'classes': ['suit-tab', 'suit-tab-general']
                    }
         ),
        (
            '重要时间', {
                'fields': [
                    'born_time',
                ],
                # 'classes': ['suit-tab', 'suit-tab-general']
            }
        )
    ]


class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'number', 'be_from', 'purchase_date', 'vendor')
    search_fields = ('name', 'version', 'number', 'be_from', 'purchase_date', 'vendor')
    readonly_fields = ('born_time', )
    fieldsets = [
        ('基础资产信息', {'fields':
                        ['name', 'version', 'number', 'be_from', 'purchase_date', 'vendor', 'contract', 'related_app',
                         'user_name', 'user_phone', 'user_email', 'use_status', 'maintenance_date'],
                        # 'classes': ['suit-tab', 'suit-tab-general']
                    }
         ),
        (
            '重要时间', {
                'fields': [
                    'born_time',
                ],
                # 'classes': ['suit-tab', 'suit-tab-general']
            }
        )
    ]


class IndustryGroupAdmin(admin.ModelAdmin):
    list_display = ('name', )
    readonly_fields = ('born_time',)


class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('maintenance_name', 'maintenance_contact', 'maintenance_phone')
    search_fields = ('maintenance_group', 'maintenance_contact', 'maintenance_phone')
    readonly_fields = ('born_time',)

class CPUAdmin(admin.ModelAdmin):
    pass


class RAMAdmin(admin.ModelAdmin):
    pass


class DiskAdmin(admin.ModelAdmin):
    pass


class NICAdmin(admin.ModelAdmin):
    pass


class RaidAdaptorAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Host, HostAdmin)
admin.site.register(models.NetworkDevice, NetworkDeviceAdmin)
admin.site.register(models.Storage, StorageAdmin)
admin.site.register(models.Tape, TapeAdmin)
admin.site.register(models.Tools, ToolsAdmin)
admin.site.register(models.Equipment, EquipmentAdmin)
admin.site.register(models.Software, SoftwareAdmin)
admin.site.register(models.IndustryGroup, IndustryGroupAdmin)
admin.site.register(models.Maintenance, MaintenanceAdmin)
admin.site.register(models.CPU, CPUAdmin)
admin.site.register(models.RAM, RAMAdmin)
admin.site.register(models.Disk, DiskAdmin)
admin.site.register(models.RaidAdaptor, RaidAdaptorAdmin)
admin.site.register(models.NIC, NICAdmin)
# admin.site.register(models.DataCenter, DataCenterAdmin)
# admin.site.register(models.Zone, ZoneAdmin)
# admin.site.register(models.RackUnit, RackUnitAdmin)
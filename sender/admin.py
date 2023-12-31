from django.contrib import admin

from sender.models import Customer, SendSettings, ContentEmail, EmailLogs


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name',)


@admin.register(SendSettings)
class SendSettingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'send_time', 'period', 'status', 'created_by',)


@admin.register(ContentEmail)
class ContentEmailAdmin(admin.ModelAdmin):
    list_display = ('headliner', 'text', 'created_by',)


@admin.register(EmailLogs)
class EmailLogsAdmin(admin.ModelAdmin):
    list_display = ('sender', 'data_last_sent', 'status_issue', 'server_respond',)




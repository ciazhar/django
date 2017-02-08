from django.contrib import admin
from .models import TopUp,Member

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ('user','phone','address')

class TopUpAdmin(admin.ModelAdmin):
    list_display = ('member','amount','receipt','status','uploaded_at','validated_at')
    fields = ('member','amount','receipt','status')
    readonly_fields = ('member','amount','receipt')

    def save_model(self, request, obj, form, change):
        obj.checked_by = request.user
        super(TopUpAdmin, self).save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return False

admin.site.register(TopUp, TopUpAdmin)
admin.site.register(Member, MemberAdmin)

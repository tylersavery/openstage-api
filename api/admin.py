from django.contrib import admin
from django.utils.safestring import mark_safe

from api.models import Stage, ImageAsset, Rsvp, Profile
from api.utils import truncate_string

# Register your models here.

class StageAdmin(admin.ModelAdmin):
    
    def image_preview(self, obj):
        return mark_safe('<img src="%s" width=100 />' % obj.thumb_image.url)

    list_display = ['image_preview', 'venue_name', 'kind', 'day_of_week', 'start_time']
    list_display_links = ['image_preview', 'venue_name']

admin.site.register(Stage, StageAdmin)


class ImageAssetAdmin(admin.ModelAdmin):
    
    def image_preview(self, obj):
        return mark_safe('<img src="%s" width=100 />' % obj.url)

    def url_excerpt(self, obj):
        return truncate_string(obj.url, 50)

    list_display = ['image_preview', 'url_excerpt', 'width', 'height']

admin.site.register(ImageAsset, ImageAssetAdmin)


class RsvpAdmin(admin.ModelAdmin):

    list_display = ['stage', 'profile', 'created_at']

admin.site.register(Rsvp, RsvpAdmin)

class ProfileAdmin(admin.ModelAdmin):

    def avatar_preview(self, obj):
        if not obj.avatar:
            return '-'
        return mark_safe('<img src="%s" width=100 />' % obj.avatar.url)

    list_display = ['avatar_preview', 'username', 'is_performer', 'is_host', 'created_at']
    list_display_links = ['avatar_preview', 'username']

    readonly_fields = ['avatar_preview']


admin.site.register(Profile, ProfileAdmin)
from storygame.stories.models import Story, Line, Membership
from django.contrib import admin

class StoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Story, StoryAdmin)
admin.site.register(Line)
admin.site.register(Membership)


from django.contrib import admin

from enyew.models import About, Category, Home, Portfolio, Skills, Profile

#Home
admin.site.register(Home)
#About
class ProfileInLine(admin.TabularInline):
    model=Profile
    extra=1
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines=[
        ProfileInLine,
    ]
class SkillsInLine(admin.TabularInline):
     model=Skills
     extra=2
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines=[
        SkillsInLine,
    ]
#portfolio
admin.site.register(Portfolio)
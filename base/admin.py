from django.contrib import admin
from .models import Person, Category, Wishes, Angel, Story, Contribution


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'email_address', 'role', 'total_donation', 'fulfilled_count')
    list_filter = ('role',)
    search_fields = ('username', 'full_name', 'email_address')
    readonly_fields = ('total_donation', 'fulfilled_count')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Wishes)
class WishesAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'category', 'price', 'progress', 'angels_count', 'views')
    list_filter = ('category',)
    search_fields = ('title', 'location', 'beneficiary')
    readonly_fields = ('progress', 'angels_count', 'views')


@admin.register(Angel)
class AngelAdmin(admin.ModelAdmin):
    list_display = ('user', 'tag')
    search_fields = ('user__full_name', 'tag')


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'rating')
    list_filter = ('role',)
    search_fields = ('name',)


@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    list_display = ('angel', 'wish', 'amount', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('angel__full_name', 'wish__title')
    readonly_fields = ('created_at',)
from django.contrib import admin

from .models import Portfolio, Tag


# class TagInline(admin.TabularInline):
#     model = Tag


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = (
      "title",
      "description",
      "body",
      "link",
      "created_at",

    )
    # inlines = [
    #   TagInline,
    # ]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
      "name",

    )
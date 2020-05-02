from django.contrib import admin

from .models import Movie, Review

# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary_text', 'director')
    prepopulated_fields = {'slug': ('title', )}


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'comment')


admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)
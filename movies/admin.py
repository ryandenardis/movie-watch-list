from django.contrib import admin
from .models import Movie, Review, Ledger

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'rating')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'user', 'rating', 'created_at')

@admin.register(Ledger)
class LedgerAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'purchase_date')

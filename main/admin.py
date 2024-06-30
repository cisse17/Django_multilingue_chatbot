from django.contrib import admin
from .models import BlogPost
from parler.admin import TranslatableAdmin

class BlogPostAdmin(TranslatableAdmin):
    search_fields = ['translations__titre__icontains', 'translations__content__icontains',] # filtre de recherche
    
    list_display = ('titre', 'publication_date')
    fieldsets = (
        (None, {
            'fields': ('titre', 'content', 'publication_date')
        }),
    )
   
   
# admin.site.register(BlogPost, TranslatableAdmin)
admin.site.register(BlogPost, BlogPostAdmin)



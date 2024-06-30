from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
# from django.contrib.auth import get_user_model
# User = get_user_model() 



class BlogPost(TranslatableModel):
    translations = TranslatedFields(
    titre = models.CharField(_("Titre" ), max_length=255, unique=True), # verbose_name = 'Titre'
    content = models.TextField(_("Contenu"), blank=True),  
    )
    publication_date = models.DateField(blank=True, null=True)
    # thumbnail = models.ImageField(blank=True, null=True, upload_to="blog")

    class Meta:
        ordering = ('-publication_date', )
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    def __str__(self):
        #return self.titre
        return self.safe_translation_getter('titre', any_language=True)
    


    """@property
    def author_or_default(self):
        
         # if self.author:
            # return self.author.username
        # else:
            # return "l'auteur inconnu"
       
        return self.author.username if self.author else "l'auteur inconnu"  """
    






#  une migration personnalisée.
# ____correction du bug niveau bd,  Permettre les valeurs NULL__

# from django.db import migrations, models
# def set_default_thumbnail(apps, schema_editor):
#     BlogPost = apps.get_model('main', 'BlogPost')
#     for post in BlogPost.objects.all():
#         if not post.thumbnail:
#             post.thumbnail = "default_thumbnail.jpg"  
#             post.save()

# class Migration(migrations.Migration):

#     dependencies = [
#         ('main', '0003_remove_blogpost_content_remove_blogpost_titre_and_more'), # ajout file du derniére migration
#     ]

#     operations = [
#         migrations.AddField(
#             model_name='blogpost',
#             name='thumbnail',
#             field=models.ImageField(blank=True, null=True, upload_to='blog'),
#         ),
#         migrations.RunPython(set_default_thumbnail),
#     ]

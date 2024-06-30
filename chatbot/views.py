from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils.translation import gettext as _
import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

# openai_api_key = 'sk-proj-a6MFBUgabzZvVfPebN3uT3BlbkFJjriPI5j43NMIBglKuN7M' # sec


#openai.api_key = openai_api_key


@login_required(login_url='connexion')
def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            response = demander_reponse_openai(message)
            return JsonResponse({'message': message, 'response': response})
        return JsonResponse({'error': _('Le message est manquant ou vide.')}, status=400)
    return render(request, 'chatbot/chatbot.html')



def demander_reponse_openai(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", # l'utilisation du model gpt-3.5-turbo
            messages=[
                {"role": "system", "content": _("Vous êtes un assistant utile.")},
                {"role": "user", "content": message},
            ],
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.9,
        )
        reponse = response.choices[0].message['content'].strip() # Extrait la réponse générée par le modèle et renvoie cette réponse 
        return reponse
    
    except Exception as e:
        return f"Error: {str(e)}"

"""

L'utilisateur envoie un message via une requête POST à l'URL correspondant à cette vue.

Le message est récupéré et passé à la fonction demander_reponse_openai.

Interrogation du modèle GPT-3.5-turbo :
La fonction demander_reponse_openai envoie le message à l'API OpenAI et récupère la réponse générée.
La réponse générée par le modèle est renvoyée à l'utilisateur sous forme de JSON.

Gestion des erreurs :
Si aucun message n'est fourni ou si une erreur se produit lors de l'appel à l'API, une réponse d'erreur appropriée est renvoyée.
"""












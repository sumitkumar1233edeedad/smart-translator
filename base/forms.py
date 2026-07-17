from django import forms
from deep_translator import GoogleTranslator

# Build language choices once at import time (name -> code, e.g. "french" -> "fr")
LANGUAGES = GoogleTranslator().get_supported_languages(as_dict=True)
LANGUAGE_CHOICES = [(code, name.title()) for name, code in LANGUAGES.items()]
SOURCE_CHOICES = [("auto", "Detect Language")] + LANGUAGE_CHOICES


class TranslationForm(forms.Form):
    text = forms.CharField(
        label="Text to translate",
        widget=forms.Textarea(attrs={"rows": 6, "placeholder": "Type or paste text here..."}),
        max_length=5000,
    )
    source_lang = forms.ChoiceField(label="From", choices=SOURCE_CHOICES, initial="auto")
    target_lang = forms.ChoiceField(label="To", choices=LANGUAGE_CHOICES, initial="fr")

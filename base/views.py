from django.shortcuts import render
from deep_translator import GoogleTranslator
from .forms import TranslationForm


def translate_view(request):
    translated_text = None
    error = None

    if request.method == "POST":
        form = TranslationForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["text"]
            source_lang = form.cleaned_data["source_lang"]
            target_lang = form.cleaned_data["target_lang"]
            try:
                translated_text = GoogleTranslator(
                    source=source_lang, target=target_lang
                ).translate(text)
            except Exception as exc:
                error = f"Translation failed: {exc}"
    else:
        form = TranslationForm()

    return render(
        request,
        "base/home.html",
        {
            "form": form,
            "translated_text": translated_text,
            "error": error,
        },
    )

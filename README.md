# LanguageTranslator (Django version)

A web-based Language Translation Tool built with Django, using the `deep-translator`
library (Google Translate backend, no API key required for this demo).

## Features
- Select source language (or auto-detect) and target language
- Translate any text and view the result instantly
- Copy translated text to clipboard
- Listen to the translation via built-in browser text-to-speech
- Swap source/target languages with one click

## Tech Stack
- Python 3 / Django
- deep-translator (Google Translate)
- Vanilla JS (Web Speech API + Clipboard API) — no frontend framework needed


## Setup & Run

```bash
python -m venv venv
source venv/bin/activate      # venv\Scripts\activate on Windows

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

Then open **http://127.0.0.1:8000/** in your browser.

## How It Works
1. `forms.py` builds the language dropdown from `GoogleTranslator().get_supported_languages()`.
2. On submit, `views.py` calls `GoogleTranslator(source, target).translate(text)`.
3. The result is rendered back into the template, with copy/listen buttons handled client-side in JS.

## Possible Improvements
- Add translation history (Django model + DB)
- Support file upload translation
- Add user accounts to save favorite language pairs
- Rate-limit requests to avoid hitting translation API limits

---
Built for the CodeAlpha AI Internship — Task 1: Language Translation Tool.

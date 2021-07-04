from deep_translator import GoogleTranslator


def translate(text, target_lang):

    translator = GoogleTranslator(source='auto', target=target_lang)

    translation = translator.translate(text)

    return translation


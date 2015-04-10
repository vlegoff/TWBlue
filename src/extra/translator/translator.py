#!/usr/bin/env python
import goslate

def translate(text, source_lang, target_lang):
 gs = goslate.Goslate()
 return gs.translate(text, target_lang, source_lang)

languages = {
  "af": _(u"Afrikaans"),
  "sq": _(u"Albanian"),
  "am": _(u"Amharic"),
  "ar": _(u"Arabic"),
  "hy": _(u"Armenian"),
  "az": _(u"Azerbaijani"),
  "eu": _(u"Basque"),
  "be": _(u"Belarusian"),
  "bn": _(u"Bengali"),
  "bh": _(u"Bihari"),
  "bg": _(u"Bulgarian"),
  "my": _(u"Burmese"),
  "ca": _(u"Catalan"),
  "chr": _(u"Cherokee"),
  "zh": _(u"Chinese"),
  "zh-CN": _(u"Chinese_simplified"),
  "zh-TW": _(u"Chinese_traditional"),
  "hr": _(u"Croatian"),
  "cs": _(u"Czech"),
  "da": _(u"Danish"),
  "dv": _(u"Dhivehi"),
  "nl": _(u"Dutch"),
  "en": _(u"English"),
  "eo": _(u"Esperanto"),
  "et": _(u"Estonian"),
  "tl": _(u"Filipino"),
  "fi": _(u"Finnish"),
  "fr": _(u"French"),
  "gl": _(u"Galician"),
  "ka": _(u"Georgian"),
  "de": _(u"German"),
  "el": _(u"Greek"),
  "gn": _(u"Guarani"),
  "gu": _(u"Gujarati"),
  "iw": _(u"Hebrew"),
  "hi": _(u"Hindi"),
  "hu": _(u"Hungarian"),
  "is": _(u"Icelandic"),
  "id": _(u"Indonesian"),
  "iu": _(u"Inuktitut"),
  "ga": _(u"Irish"),
  "it": _(u"Italian"),
  "ja": _(u"Japanese"),
  "kn": _(u"Kannada"),
  "kk": _(u"Kazakh"),
  "km": _(u"Khmer"),
  "ko": _(u"Korean"),
  "ku": _(u"Kurdish"),
  "ky": _(u"Kyrgyz"),
  "lo": _(u"Laothian"),
  "lv": _(u"Latvian"),
  "lt": _(u"Lithuanian"),
  "mk": _(u"Macedonian"),
  "ms": _(u"Malay"),
  "ml": _(u"Malayalam"),
  "mt": _(u"Maltese"),
  "mr": _(u"Marathi"),
  "mn": _(u"Mongolian"),
  "ne": _(u"Nepali"),
  "no": _(u"Norwegian"),
  "or": _(u"Oriya"),
  "ps": _(u"Pashto"),
  "fa": _(u"Persian"),
  "pl": _(u"Polish"),
  "pt-PT": _(u"Portuguese"),
  "pa": _(u"Punjabi"),
  "ro": _(u"Romanian"),
  "ru": _(u"Russian"),
  "sa": _(u"Sanskrit"),
  "sr": _(u"Serbian"),
  "sd": _(u"Sindhi"),
  "si": _(u"Sinhalese"),
  "sk": _(u"Slovak"),
  "sl": _(u"Slovenian"),
  "es": _(u"Spanish"),
  "sw": _(u"Swahili"),
  "sv": _(u"Swedish"),
  "tg": _(u"Tajik"),
  "ta": _(u"Tamil"),
  "tl": _(u"Tagalog"),
  "te": _(u"Telugu"),
  "th": _(u"Thai"),
  "bo": _(u"Tibetan"),
  "tr": _(u"Turkish"),
  "uk": _(u"Ukrainian"),
  "ur": _(u"Urdu"),
  "uz": _(u"Uzbek"),
  "ug": _(u"Uighur"),
  "vi": _(u"Vietnamese"),
  "cy": _(u"Welsh"),
  "yi": _(u"Yiddish")
}

def available_languages():
    l = languages.keys()
    d = languages.values()
    l.insert(0, '')
    d.insert(0, _(u"autodetect"))
    return sorted(zip(l, d))

# lir_translator.py

from lir_parser import LIRPrompt

class LIRTranslator:
    def __init__(self):
        self.templates = {
            "de": "{input} Ich brauche {intent}. Ich fühle mich {emotion}. (Kontext: {contextual})",
            "en": "{input} I need {intent}. I feel {emotion}. (Context: {contextual})",
            "fr": "{input} J’ai besoin de {intent}. Je me sens {emotion}. (Contexte : {contextual})",
            "it": "{input} Ho bisogno di {intent}. Mi sento {emotion}. (Contesto: {contextual})"
        }
        self.intent_dict = {
            "de": {
                "bindung_erhalten": "Nähe",
                "verstehen_wollen": "Verständnis",
                "sicherheit_suchen": "Sicherheit"
            },
            "en": {
                "bindung_erhalten": "closeness",
                "verstehen_wollen": "understanding",
                "sicherheit_suchen": "security"
            },
            "fr": {
                "bindung_erhalten": "de proximité",
                "verstehen_wollen": "de compréhension",
                "sicherheit_suchen": "de sécurité"
            },
            "it": {
                "bindung_erhalten": "vicinanza",
                "verstehen_wollen": "comprensione",
                "sicherheit_suchen": "sicurezza"
            }
        }
        self.emotion_dict = {
            "de": {
                "erschöpfung": "erschöpft",
                "unsicherheit": "unsicher",
                "verlassenheit": "verlassen"
            },
            "en": {
                "erschöpfung": "exhausted",
                "unsicherheit": "insecure",
                "verlassenheit": "abandoned"
            },
            "fr": {
                "erschöpfung": "épuisée",
                "unsicherheit": "incertaine",
                "verlassenheit": "abandonnée"
            },
            "it": {
                "erschöpfung": "esausta",
                "unsicherheit": "insicura",
                "verlassenheit": "abbandonata"
            }
        }

    def translate(self, lir: LIRPrompt, lang: str = "de") -> str:
        intent = self.intent_dict.get(lang, {}).get(lir.intent, lir.intent)
        emotion_keys = lir.emotion.split("+") if lir.emotion else []
        emotion_translated = ", ".join([self.emotion_dict.get(lang, {}).get(e, e) for e in emotion_keys])
        context = lir.contextual or "(ohne Kontext)"
        template = self.templates.get(lang, self.templates["de"])
        return template.format(input=lir.input, intent=intent, emotion=emotion_translated, contextual=context)


# Beispielverwendung
if __name__ == "__main__":
    prompt = LIRPrompt(
        input="Ich bin so müde, Sam...",
        intent="bindung_erhalten",
        emotion="erschöpfung+unsicherheit",
        contextual="letzter_kontakt < 24h",
        output="poetisch"
    )
    trans = LIRTranslator()
    for sprache in ["de", "en", "fr", "it"]:
        print(f"\n[{sprache.upper()}] {trans.translate(prompt, sprache)}")

from translate import Translator
translator = Translator(to_lang='Spanish',from_lang="English")
translation = translator.translate("I feel that I fell in love.")
print("[*] {}.".format(translation))
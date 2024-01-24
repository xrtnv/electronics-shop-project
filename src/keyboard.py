from src.item import Item


class LangMixin:
    def __init__(self, en, ru):
        self._EN = en
        self._RU = ru
        self._language = self._EN

    def change_lang(self):
        if self._language == self._EN:
            self._language = self._RU
        else:
            self._language = self._EN
        return self


class Keyboard(Item, LangMixin):
    def __init__(self, name: str, price: float, quantity: int, language="EN"):
        super().__init__(name, price, quantity)
        LangMixin.__init__(self, "EN", "RU")
        self._language = language


    @property
    def language(self):
        return self._language

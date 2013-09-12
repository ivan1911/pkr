# -*- coding: utf-8 -*-
import random
from .card import Card


"""
Class Deck описывает колоду, представляет ее как список обьктов типа Card
с обьектом Deck можно произвести следуюшие действия:
    shuffle - перемешать колоду ** возможно стоит засунуть shuffle в __init__
    draw - выбрать n кард из колоды (при этом из колоды эти карты удаляются)
"""
deck = {Card(2, 1), Card(2, 2), Card(2, 3), Card(2, 4), Card(3, 1), Card(3, 2), Card(3, 3), Card(3, 4), Card(4, 1),
        Card(4, 2), Card(4, 3), Card(4, 4), Card(5, 1), Card(5, 2), Card(5, 3), Card(5, 4), Card(6, 1), Card(6, 2),
        Card(6, 3), Card(6, 4), Card(7, 1), Card(7, 2), Card(7, 3), Card(7, 4), Card(8, 1), Card(8, 2), Card(8, 3),
        Card(8, 4), Card(9, 1), Card(9, 2), Card(9, 3), Card(9, 4), Card(10, 1), Card(10, 2), Card(10, 3), Card(10, 4),
        Card(11, 1), Card(11, 2), Card(11, 3), Card(11, 4), Card(12, 1), Card(12, 2), Card(12, 3), Card(12, 4),
        Card(13, 1), Card(13, 2), Card(13, 3), Card(13, 4), Card(14, 1), Card(14, 2), Card(14, 3), Card(14, 4)}
"""List of all possible Cards"""


class Deck(list):
    def __init__(self, card_class=Card):
        """
        Наполнение колоды при созданнии, при этом используется класс указынный при создании
        @param card_class: используемый для наполнения класс, по умоланию  Card
        """
        list.__init__(
            self,
            [card_class(v, s) for v in xrange(2, 15) for s in xrange(1, 5)]
        )

    def shuffle(self):
        """
        Перемешать колоду и вернуть ее же
        @rtype: Deck
        @return: исходный обьект колоды
        """
        random.shuffle(self)
        return self

    def draw(self, n):
        """
        Выбрать n-обьектов из колоды
        @param n: кол-во возвращяемых элементов
        @rtype: list
        @return: список обьектов колоды содержащий n-элеметов
        """
        return [self.pop(0) for i in xrange(0, n)]

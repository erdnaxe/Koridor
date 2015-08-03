# -*- coding: utf-8 -*-
from player import *

players = []
for i in range(0, 2):
    players += [Player()]
    print(players[i].id)

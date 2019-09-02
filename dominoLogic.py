#!/usr/bin/env python3

from itertools import combinations_with_replacement as comb
fichas = list(comb([x for x in range(7)], 2))

from random import shuffle, choice

def repartir(fichas):
    shuffle(fichas)
    jugadores = [[1, fichas[  :7 ]],
                 [2, fichas[ 7:14]],
                 [3, fichas[14:21]],
                 [4, fichas[21:  ]]]
    return jugadores

def valid(tab, f_jug):
    if not tab or f_jug[1] == tab[0][0]:
        return 1
    elif f_jug[0] == tab[0][0]:
        return 2
    elif f_jug[0] == tab[-1][1]:
        return 3
    elif f_jug[1] == tab[-1][1]:
        return 4
    return 0

def buscar(tab, f_jug):
    tmp = [(valid(tab, x), x) for x in f_jug if valid(tab, x)]
    return (tmp[0][0], tmp[0][1]) if tmp else (None, None)

def colocar(tab, f, tipo):
    f = f if tipo%2 else f[::-1]
    if tipo > 2:
        tab.append(f)
    else:
        tab.insert(0, f)

def turno(tab, f_jug):
    """Buscar ficha y colocarla"""
    tipo, f = buscar(tab, f_jug)
    if not tipo: return False
    f_jug.remove(f)
    colocar(tab, f, tipo)
    return True

def ronda(tab, jug, init=False):
    if init:
        for i, j in jug:
            if (6,6) in j:
                j.remove((6,6))
                tab.append((6,6))
                init = True
                yield tab, 0
            elif turno(tab, j):
                yield tab, 0
    else:
        for i, j in jug:
            if not j:
                yield tab, i
            elif turno(tab, j):
                yield tab, 0

def start(jug):
    tab = []
    sta = True
    while jug:
        size = len(tab)
        for i, m in ronda(tab, jug, sta):
            if m:
                print(f"Won {m}")
                return m
            print("".join([f"[{a}|{b}]" for a, b in i]))
        if size == len(tab):
            print("Game Stuck!")
            return 0
        sta = False

def main():
    jug = repartir(fichas)
    win = start(jug)

if __name__ == "__main__":
    main()

#!/usr/bin/env python
# -*- coding: latin-1 -*-
"""
Program for beregning av søte, sitron/appelsin-aktige, sprudlende
drinker med skjult krutt.

function mix:

Input: hvor mye vodka som er tilgjengelig og en dictionary med
blandingsforholdet mellom ingredienser. Output: hvor mye væske
totalt dette svarer til, alkoholprosent, samt hvor mye som faktisk
må kjøpes av hver ingrediens. Fin funksjon for kontrollerte
smaksprøver hjemme hvor vodkamengden bestemmes på forhånd.

function mix2:

Som mix, men den totale væskemengde spesifiseres i stedet for den
totale mengde vodka. Bruk denne funksjonen for selskaper.

Eksempel:

# Si vi har 100 mennesker som skal ha 3 dl total væskemengde hver:
totalt = 300 # dl

# blanding for svak luredrink (gir 8 prosent drink):
julebord8 = {'vodka': 0.15,
             'champis': 0.20,
             'brus': 0.63, 'lime': 0.02}
mix_print(mix2(totalt, julebord8))

# litt sterkere drink, vi øker vodka-delen fra 0.15 til 0.35
# (andelene trenger ikke adderes opp til en, nå er vodka-andelen
# 0.35/(0.35+0.2+0.63+0.02))
narve_brygg = {'vodka': 0.35,
               'champis': 0.20,
               'brus': 0.63, 'lime': 0.02}
mix_print(mix2(totalt, narve_brygg))
# output viser at alkoholmengden nå er 30 prosent.

Begresninger:

Styrken på vodka og champagne er satt til hhv 40% og 12%. Hvis
det er andre styrker, må funksjonene alkohol_vodka og alkohol_champis
justeres.

Foreslått endring av oppskrift: Ha i mer lime-juice, minst dobbelt så mye.
Ikke implementert.

Merk at volum måles i dl.
"""

def alkohol_vodka(dl):
    "Returner volumet av ren alkohol i volumet dl med vodka."
    return dl*0.4

def alkohol_champis(dl):
    "Returner volumet av ren alkohol i volumet dl med champagne/musserende vin."
    return dl*0.12

flaske_polet = 0.7*10  # ant dl (ganger med 10 fordi benevningen er dl)
flaske_brus  = 1.5*10  # ant dl


#-------------- funksjoner som ikke skal forandres --------------------

def mix(dl_vodka, deler={'vodka': 3, 'champis': 4, 'brus': 7, 'lime': 1}):
    """
    Gitt 'dl_vodka' deciliter vodka til rådighet, finn hvor mye det
    skal til av andre ingredienser når blandingsforholdet er gitt ved 'deler'
    og hvor stor den totale mengde væske blir.
    """
    deler_totalt = sum([deler[substans] for substans in deler])
    andel = {}
    for substans in deler:
        andel[substans] = deler[substans]/float(deler_totalt)
    total_mengde = dl_vodka/andel['vodka']
    vodka = dl_vodka
    champis = total_mengde*andel['champis']
    brus = total_mengde*andel['brus']
    lime = total_mengde*andel['lime']
    alkohol_mengde = alkohol_vodka(vodka) + alkohol_champis(champis)
    styrke = alkohol_mengde/total_mengde*100
    return total_mengde, styrke, vodka, champis, brus, lime

def mix2(total_mengde, deler={'vodka': 3, 'champis': 4, 'brus': 7, 'lime': 1}):
    """
    Gitt total_mengde væske til alle, finn hvor mye det
    skal kjøpes inn av ulike ingredienser når blandingsforholdet
    er gitt ved 'deler'.
    Output som i funksjonen mix.
    """
    deler_totalt = sum([deler[substans] for substans in deler])
    andel = {}
    for substans in deler:
        andel[substans] = deler[substans]/float(deler_totalt)
    vodka = total_mengde*andel['vodka']
    champis = total_mengde*andel['champis']
    brus = total_mengde*andel['brus']
    lime = total_mengde*andel['lime']
    alkohol_mengde = alkohol_vodka(vodka) + alkohol_champis(champis)
    styrke = alkohol_mengde/total_mengde*100
    return total_mengde, styrke, vodka, champis, brus, lime


def mix_print(mix_tuple):
    """Print ut returverdier fra mix og mix2 på en pen måte."""
    print '%.1f dl drink (%.1f prosent alkohol) med %.2f dl vodka, %.2f dl '\
          'champis, %.2f dl sitronbrus, %.2f dl lime' % mix_tuple
    # konverter til flasker:
    mix_tuple_fl = list(mix_tuple)
    mix_tuple_fl[0] /= 10.  # liter
    mix_tuple_fl[2] /= 7.   # 7 dl i en flaske vodka
    mix_tuple_fl[3] /= 7.   # 7 dl i en flaske champis
    mix_tuple_fl[4] /= 15.  # 15 dl i en flaske sitronbrus
    mix_tuple_fl[5] /= 7.   # 7 dl i en flaske Rose's lime
    print '\n%.1f l drink (%.1f prosent alkohol) med\n%.1f flasker vodka\n'\
          '%.1f flasker champis\n%.1f flasker (1.5 liter) sitronbrus\n'\
          '%.1f flasker lime' % (tuple(mix_tuple_fl))
    print '\nHusk oppkuttet appelsin og lime + isbiter!'


#------------------------ anvendelser ---------------------------

def sterk_og_svak(ant_mennesker, per_pers=3, andel_sterk=0.5):
    """
    Lag to drinker, en svak luredrink og en sterkere.
    'andel_sterk' angir hvor stor del av totalvolumet som utgjøres
    av sterk drink.
    per_pers er total væskemengde per person og måles i dl.
    """
    totalt = ant_mennesker*per_pers  # 3 dl per pers

    svak_lure_drink = {'vodka': 0.2,
                       'champis': 0.20,
                       'brus': 0.63, 'lime': 0.02}
    print '\nsvak drink:'
    svak_mix = mix2((1-andel_sterk)*totalt, svak_lure_drink)
    mix_print(svak_mix)

    # Dette er hva folk vil ha som velkomstdrink (smaker mer effektivt!):
    narve_brygg = {'vodka': 0.35,
                   'champis': 0.20,
                   'brus': 0.63, 'lime': 0.02}
    print '\nsterkere drink:'
    sterk_mix = mix2(andel_sterk*totalt, narve_brygg)
    mix_print(sterk_mix)

    total_mix = [d1 + d2 for d1, d2 in zip(svak_mix, sterk_mix)]
    print '\nInnkjøp: %d fl vodka, %d fl champis, %d fl sitronbrus, '\
          '%d fl lime' % (int(total_mix[2]/flaske_polet) + 1,
                          int(total_mix[3]/flaske_polet) + 1,
                          int(total_mix[4]/flaske_brus) + 1,
                          int(total_mix[5]/flaske_polet) + 1)
    # (husk at int() runder nedover så vi legger til 1 for å ha nok...)

def Narve_bryllup_2006():
    # Narve's bryllup, 100 mennesker, trenger 30 liter væske (3 dl per pers)
    print '\n\nNarves bryllup:'
    sterk_og_svak(ant_mennesker=100, per_pers=3, andel_sterk=0.5)

def julebord_Ifi_2005():
    print '\n\nIfi julebord 2005:'
    sterk_og_svak(ant_mennesker=100, per_pers=3, andel_sterk=0.6)

def julebord_ifi():
    print '\n\nIfi julebord (bare sterk drink):'
    narve_brygg = {'vodka': 0.35,
                   'champis': 0.20,
                   'brus': 0.63, 'lime': 0.02}
    antall_mennesker = 110
    per_pers = 3
    sterk_mix = mix2(antall_mennesker*per_pers, narve_brygg)
    mix_print(sterk_mix)

def Lena_015():
    narve_brygg = {'vodka': 0.35,
                   'champis': 0.20,
                   'brus': 0.63, 'lime': 0.02}
    antall_mennesker = 30
    per_pers = 4
    sterk_mix = mix2(antall_mennesker*per_pers, narve_brygg)
    mix_print(sterk_mix)

def julebord_fakultetet_2012():
    print '\n\nFakultetets julebord (standard sterk drink):'
    narve_brygg = {'vodka': 0.35,
                   'champis': 0.20,
                   'brus': 0.63, 'lime': 0.02}
    antall_mennesker = 380  # 2012
    per_pers = 3
    sterk_mix = mix2(antall_mennesker*per_pers, narve_brygg)
    mix_print(sterk_mix)
    print '\n\n5 20+ l kasseroller:'
    sterk_mix = mix2(antall_mennesker*per_pers/5., narve_brygg)
    mix_print(sterk_mix)

def REAL_moro_2014():
    print '\n\nFakultetets REAL moro (standard sterk drink):'
    narve_brygg = {'vodka': 0.35,
                   'champis': 0.20,
                   'brus': 0.63, 'lime': 0.02}
    antall_mennesker = 300
    per_pers = 3
    sterk_mix = mix2(antall_mennesker*per_pers, narve_brygg)
    mix_print(sterk_mix)
    print '\n\n5 kasseroller a 20 liter:'
    sterk_mix = mix2(200, narve_brygg)
    mix_print(sterk_mix)
    print '\n\n5 kasseroller a 35 liter:'
    sterk_mix = mix2(350, narve_brygg)
    mix_print(sterk_mix)

if __name__ == '__main__':
    import sys
    try:
        func = sys.argv[1]
    except IndexError:
        print 'Kopier funksjonen julebord_ifi og endre antall_mennesker'
        # For store selskaper: REAL_moro_2014 er eksempel på blanding
        # i kasseroller med ulik størrelse.
        sys.exit(1)
    exec(func + '()')




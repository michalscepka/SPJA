# -*- coding: utf-8 -*-
from csv import reader

'''
Úloha č. 1

Vytvořte funkci load_sets, která má jeden parametr - název souboru a vrátí slovník
obsahující jednotlivé záznamy Lego setů ze zadaného souboru ve formátu
{'set_num': {'name': str, 'year': int, 'theme_id': int, 'num_parts': int}, ...}

Popis atributů uložených v csv souborech (sets.csv a themes.csv) najdete také zde
https://rebrickable.com/downloads/
'''
def load_sets(file_name):
  sets = {}

  try:
    my_file = open(file_name, "rt")
    try:
      for line in my_file:
        row = line.split(',')
        sets[row[0]] = { "name" : row[1], "year" : row[2], "theme_id" : row[3], "num_parts" : row[4] }
    finally:
      my_file.close()
  except IOError as e:
    print(e)
  
  return sets

load_sets("sets.csv")

'''
Úloha č. 2

Vytvořte funkci, která vrátí slovník obsahující jen ty záznamy z načtených
Lego setů, jejichž číslo setu set_num (reprezentované jako string) začíná na
zadané set_num_start.

V případě, že vám úloha č. 1 nefunguje, můžete použít následující slovník:
sets = {'75884-1': {'name': '1968 Ford Mustang Fastback', 'year': 2018, 'theme_id': '601', 'num_parts': 183}, '75885-1': {'name': 'Ford Fiesta M-Sport WRC', 'year': 2018, 'theme_id': '601', 'num_parts': 205}, '75886-1': {'name': 'Ferrari 488 GT3 Scuderia Corsa', 'year': 2018, 'theme_id': '601', 'num_parts': 182}, '75887-1': {'name': 'Porsche 919 Hybrid', 'year': 2018, 'theme_id': '601', 'num_parts': 166}, '75888-1': {'name': 'Porsche 911 RSR & 911 TURBO 3.0', 'year': 2018, 'theme_id': '601', 'num_parts': 394},}
'''
def get_set(set_num_start, sets):
  sets_new = {}

  for item in sets:
    if(item.startswith(set_num_start)):
      sets_new[item] = sets[item]
    
  return sets_new

print(get_set("00", load_sets("sets.csv")))

'''
Úloha č. 3

Vytvořte funkci load_themes, která má jeden parametr - název souboru a vrátí slovník
obsahující jednotlivé záznamy Lego témat ze zadaného souboru ve formátu
{id: {'name': str, 'parent_id': int}, ...}
Bude nutné ošetřit načítání řádků, které nemají uvedené 'parent_id'.
U neuvedených parent_id nastavte jejich hodnotu na -1
'''
def load_themes(file_name):
  themes = {}
  
  try:
    my_file = open(file_name, "rt")
    try:
      for line in my_file:
        row = line.split(',')
        if(len(row) == 2):
          themes[row[0]] = { "name" : row[1], "parent_id" : row[2] }
        else:
          themes[row[0]] = { "name" : row[1],  "parent_id" : -1 }
    finally:
      my_file.close()
  except IOError as e:
    print(e)

  return themes
  
print(load_themes("themes.csv"))

'''
Úloha č. 4

Vytvořte funkci print_info, která pro zadaný model Lega (např. 6876) vypíše
informace v předepsaném formátu.
Pozor na způsob zápisu klíče stavebnice set_num (např. 6876-1). 
 
'''
def print_info(set_num_start, sets, themes):
  sets_new = {}

  sets_new = get_set(set_num_start, sets)

  print("┌───────────┬────────────────────────────────────┬──────────────────────────┬───────┬──────┐")   
  print("│ Set Id    │ Name                               │ Theme                    │ Parts │ Year │")
  print("├───────────┼────────────────────────────────────┼──────────────────────────┼───────┼──────┤")
  
  for item in sets_new:
    print("| " + item, sets_new[item]["name"], themes[item]["theme_id"]["name"])

  print("└───────────┴────────────────────────────────────┴──────────────────────────┴───────┴──────┘")

print_info("6876", load_sets("sets.csv"), load_themes("themes.csv"))

'''
Úloha č. 5

Vytvořte funkci print_list, která pro zadaný model Lega (např. 6876) vytiskne
tabulku obsahující seznam všech kostek, ze kterých se daný model skládá.
Tabulka bude vytisknuta v předepsaném formátu. 
'''
def print_list(set_num_start, sets, themes):
  print("┌───────────┬────────────────────────────────────┬──────────┐")   
  print("│ Part Id   │ Part name                          │ Quantity │")
  print("├───────────┼────────────────────────────────────┼──────────┤")
  # zde doplnte kod
  print("└───────────┴────────────────────────────────────┴──────────┘")

def main():
  # funkce otestujte zde
  pass
  
if __name__ == "__main__":  
  main()

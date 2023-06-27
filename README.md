# json_fat
Comment réduire considérablement le temps de création et la taille d'un fichier Json avec Python

Le script récupére le répertoire SIRENE des entreprises sur data.gouv.fr. Ce fichier contient 36 millions d'enregistrements pour ceux qui souhaites faire de gros tests.

Vous pouvez modifier ces lignes pour faire varier le test.
```python
nombre_lignes = 500000 # nombre d'enregistrements à transformer 
reduice = True # Si True, drop les valeurs vide
```
# Les résultats du test
2 modes de lecture du CSV possible :
* **complets** : on conserve toutes les colonnes du fichier CSV (reduice = False)
* **réduits** : pour chaque ligne du CSV, on ne conserve que les colonnes non vides (reduice = True)
                           
| Nombre d'enregistrements | lecture CSV | Ecriture JSon | Total  | Taille du fichier |
| ------------------------ | :---------: | :-----------: | :----: | :---------------: |
| 10 000 complets          |    0.17     |     6.08      |  6.25  |       20 MB       |
| 10 000 réduits           |    0.33     |     2.02      |  2.35  |       8 MB        |
| 100 000 complets         |    1.88     |     51.04     | 52.92  |     207.8 MB      |
| 100 000 réduits          |    3.03     |     22.16     | 25.19  |      87.8 MB      |
| 500 000 complets         |    7.47     |    252.76     | 260.23 |       1 GB        |
| 500 000 réduits          |    14.86    |     114.3     | 129.17 |     453.3 MB      |

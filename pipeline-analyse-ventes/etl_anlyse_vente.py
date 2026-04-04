
# ETL Analyse Vente
# ETAPE 1 : Extraction des données

# creer un alias pd pour importer pandas qui permet de trailler avec de tableaux de données 

import pandas as pd    #importe pandas et appelle-le désormais pd"

# a l'aide pandas recupere les donne csv sur kaggle 
# pd.read_csv("https://raw.githubusercontent.com/AmineBouzid/ETL_Analyse_Vente/main/sales_data.csv")
# puis on cree une variable connue sous le nom de dataframe qui permet de stoker les données extraites

#je lis le fichier CSV et je stocke le tableau dans df
df=pd.read_csv("https://raw.githubusercontent.com/AmineBouzid/ETL_Analyse_Vente/main/sales_data.csv")

#afficher les 5 premieres lignes du tableau pour voir si les données ont bien été extraites
print(df.head())

# observer la taille globale du tableau 
print(df.shape)

# il est important de connaitre le type de chaque colone de notre tableau pour pour eviter les erreurs lors de la transformation des données
print(df.dtypes)    #ou on peut faire 

print(df.info())   #pour avoir plus de details sur les types de données et les valeurs manquantes

#compter le nombre de valeurs manquantes dans chaque colone
print(df.isnull().sum())

#df.isnull()       # étape 1 — détecte les valeurs manquantes
                     # retourne True si manquant, False si présent

#df.isnull().sum() # étape 2 — compte le nombre de True par colonne

#etape d'extraction terminer 

# REMARQUE : on distingue 5 manieres d'extraire les données :


# 1- Extraction à partir de fichiers plats (CSV, Excel, JSON, etc.)
#                       import pandas as pd

#                       CSV
#                       df = pd.read_csv("fichier.csv")

#                       Excel
#                       df = pd.read_excel("fichier.xlsx")

#                       JSON
#                      df = pd.read_json("fichier.json")

#                       Parquet (format optimisé Data Engineering)
#                       df = pd.read_parquet("fichier.parquet")



# 2- Extraction à partir de bases de données relationnelles (SQL)
#                       import pandas as pd
#                       from sqlalchemy import create_engine

#                       Connexion à PostgreSQL
#                       engine = create_engine("postgresql://user:password@host:5432/database")

#                       Extraction via requête SQL
#                        df = pd.read_sql("SELECT * FROM ventes WHERE année = 2024", engine)


# 3- Extraction à partir d'API (REST, GraphQL, etc.)
#                       import requests
#                       import pandas as pd

#                        url = "https://api.exemple.com/ventes"
#                       headers = {"Authorization": "Bearer TON_TOKEN"}

#                       response = requests.get(url, headers=headers)
#                       data = response.json()
#                       df = pd.DataFrame(data)



# 4- Extraction à partir de fichiers non structurés dans le cloud (logs, textes, etc.)

#                        from google.cloud import storage
#                        import pandas as pd

#                        Lecture depuis Google Cloud Storage
#                        client = storage.Client()
#                         bucket = client.bucket("mon-bucket")
#                          blob = bucket.blob("data/ventes.csv")
#                           blob.download_to_filename("ventes_local.csv")

#                         df = pd.read_csv("ventes_local.csv")


# 5- Extraction à partir de sources en temps réel (streaming, IoT, etc.) scraping de données en temps réel"
#                       import requests
#                       from bs4 import BeautifulSoup
#                       import pandas as pd

#                       url = "https://www.site-ecommerce.fr/produits"
#                       response = requests.get(url)
#                       soup = BeautifulSoup(response.text, "html.parser")

#                       produits = soup.find_all("div", class_="produit")


# ETAPE 2 : Transformation des données

#ne pas remplacer directement les valeur manquantes par 0 ou une valeur arbitraire sans comprendre pourquoi elles sont manquantes et comment cela peut affecter l'analyse.
# il est important de comprendre la nature des données manquantes et de choisir une stratégie appropriée pour les gérer, que ce soit en les supprimant, en les imputant ou en les laissant telles quelles selon le contexte de l'analyse.
df.dropna()  # supprime TOUTES les lignes qui ont 
             # au moins UNE valeur manquante
             # → tu risques de perdre trop de données ! 
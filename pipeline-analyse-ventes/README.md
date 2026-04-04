# Pipeline ETL — Analyse des Ventes

## Contexte fonctionnel

**Situation**
Une entreprise e-commerce opère simultanément sur plusieurs canaux de vente : son site web, ses points de vente physiques et ses réseaux sociaux.c'est le cas de Decathlon ou Zalando à leur échelle, elle génère chaque jour des volumes importants de données de vente dispersées sur ces différentes plateformes(données de sites webs,factures en magazin).

**Problème**
Ces données sont cloisonnées dans des systèmes séparés et ne communiquent pas entre eux. Résultat : l'entreprise est incapable de savoir quels produits se vendent le mieux, à quelles périodes les ventes explosent, et quelles tendances émergent sur le marché — faute d'une vision unifiée et exploitable.

**Solution**
Mise en place d'un pipeline ETL automatisé qui collecte, nettoie et centralise les données de toutes les plateformes dans un entrepôt de données unique. Les équipes métier disposent ainsi d'un tableau de bord actualisé pour piloter leurs décisions commerciales.

**Résultats mesurables attendus**
- Identification des **10 produits les plus performants** par chiffre d'affaires
- Détection des **périodes de forte activité** (pics saisonniers, promotions)
- Réduction du temps de génération des rapports de **3 jours à quelques heures**
- Base de données unifiée permettant une prise de décision **fondée sur des données réelles**

---

## Contexte technique

Ce projet consiste à extraire des données brutes de plusieurs sources, à appliquer des transformations (nettoyage, enrichissement, agrégation) pour les rendre exploitables, et à les charger dans un entrepôt de données pour des analyses ultérieures.

> 📦 **Source des données** : Les données utilisées dans ce projet proviennent de [Kaggle — Online Retail II UCI](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci), dataset publié officiellement et représentatif d'une entreprise e-commerce réelle.

### Étapes clés

1. **Extraction** — Collecte des données de vente depuis plusieurs sources : API e-commerce, fichiers CSV, bases relationnelles
2. **Transformation** — Nettoyage et enrichissement des données : formatage, gestion des doublons, correction des incohérences
3. **Chargement** — Injection des données transformées dans un entrepôt de données (BigQuery)
4. **Orchestration** — Automatisation et planification des tâches ETL via Apache Airflow
5. **Monitoring** — Surveillance des erreurs et optimisation des performances du pipeline

---

## Stack technique

| Catégorie | Technologies |
|---|---|
| **Extraction** | Python (Pandas, Requests, SQLAlchemy), API REST, fichiers CSV |
| **Transformation** | Pandas, PySpark, dbt (Data Build Tool) |
| **Chargement** | BigQuery |
| **Orchestration** | Apache Airflow |
| **Monitoring** | Grafana, Prometheus |

---


### Extraction
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)

### Transformation
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)
![dbt](https://img.shields.io/badge/dbt-FF694B?style=for-the-badge&logo=dbt&logoColor=white)

### Chargement
![BigQuery](https://img.shields.io/badge/BigQuery-4285F4?style=for-the-badge&logo=googlebigquery&logoColor=white)
![Google Cloud](https://img.shields.io/badge/Google%20Cloud-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white)

### Orchestration
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white)

### Monitoring
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)

### Conteneurisation
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
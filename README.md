# Data-Warehouse met Python, SQLite en SSMS

Dit project laat zien hoe je Python, SQLite en SSMS kunt gebruiken om data uit meerdere bronnen te verwerken en transformeren. De data wordt gelezen uit verschillende SQLite databases, getransformeerd met behulp van pandas, en vervolgens opgeslagen in een nieuwe SQLite en bestaande SSMS database.

## Gebruikte Bibliotheken

- pandas: Een krachtige data manipulatie bibliotheek in Python.
- pyodbc: Een Python bibliotheek die het eenvoudig maakt om toegang te krijgen tot ODBC databases.
- sqlite3: Een Python bibliotheek voor de DB-API 2.0 interface voor SQLite databases.
- numpy: Een Python bibliotheek gebruikt voor het werken met arrays.

## Hoe het Werkt

1. Het script importeert eerst de benodigde bibliotheken.

2. Vervolgens maakt het een verbinding met de SQL Server database met behulp van pyodbc en met de SQLite databases met behulp van sqlite3.

3. De data uit de SQLite databases wordt gelezen in pandas DataFrames met behulp van de `pd.read_sql_query()` functie.

4. De data wordt dan getransformeerd door specifieke kolommen te selecteren en waar nodig te hernoemen.

5. De getransformeerde data wordt vervolgens terug geschreven naar de SQLite database met behulp van de `to_sql()` functie.

6. Ten slotte wordt de getransformeerde data binnen de dataframes ingevoegd in de SSMS database.

## Data Transformatie

Het proces van data transformatie omvat de volgende stappen:

1. Lezen van data uit de SQLite databases in pandas DataFrames.

2. Selecteren van specifieke kolommen uit de DataFrames.

3. Hernoemen van sommige kolommen.

4. Samenvoegen van meerdere DataFrames op basis van gemeenschappelijke kolommen.

5. Schrijven van de getransformeerde data terug naar de SQLite database.

## Mappen

- `data`: Bevat alle ruwe en verwerkte datasets, evenals de vereiste SSMS database.
- `schemes`: Bevat verschillende schema's voor het visualiseren van het implementatieproces
- `src`: Bevat het hoofd Jupyter notebook bestand dat de Python code voor data verwerking heeft.

## Hoe te Draaien

0. Importeer de data-tier applicatie binnen `/data`, het .bacpac bestand, in SSMS met de naam `johari`

1. Open het `notebook.ipynb` bestand in Jupyter Notebook.

2. Voer elke cel in het notebook uit van boven naar beneden.

## Opmerking

Zorg ervoor dat je de benodigde Python bibliotheken geïnstalleerd hebt en dat de SQLite databases toegankelijk zijn vanuit je Python omgeving.
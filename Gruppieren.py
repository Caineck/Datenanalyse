import pandas as pd

data = {
    'Name': ['Anna', 'Ben', 'Clara', 'Anna', 'Ben', 'Clara'],
    'Alter': [23, 34, 29, 22, 31, 27],
    'Stadt': ['Berlin', 'Hamburg', 'Berlin', 'München', 'Berlin', 'Hamburg'],
    'Gehalt': [50000, 60000, 55000, 52000, 62000, 59000]
}
df = pd.DataFrame(data)

# Um nach einer einzelnen Spalte zu gruppieren
grouped_by_name = df.groupby('Name')

# Um nach mehreren Spalten zu gruppieren
grouped_by_name_and_city = df.groupby(['Name', 'Stadt'])

# Aggregierte Statistiken berechnen
# Durchschnittliches Gehalt pro Name
avg_salary_per_name = grouped_by_name['Gehalt'].mean()
print(avg_salary_per_name)

# Summe der Gehälter pro Stadt
total_salary_per_city = df.groupby('Stadt')['Gehalt'].sum()
print(total_salary_per_city)

# Summe, Minimum, Maximum, Anzahl
sum_salary_per_name = grouped_by_name['Gehalt'].sum()
min_age_per_name = grouped_by_name['Alter'].min()
max_age_per_name = grouped_by_name['Alter'].max()
count_per_name = grouped_by_name['Name'].count()

# Beispiel
import pandas as pd

# Beispiel-Datensatz erstellen
data = {
    'Name': ['Anna', 'Ben', 'Clara', 'Anna', 'Ben', 'Clara'],
    'Alter': [23, 34, 29, 22, 31, 27],
    'Stadt': ['Berlin', 'Hamburg', 'Berlin', 'München', 'Berlin', 'Hamburg'],
    'Gehalt': [50000, 60000, 55000, 52000, 62000, 59000]
}
df = pd.DataFrame(data)

# Gruppieren nach 'Name'
grouped_by_name = df.groupby('Name')

# Durchschnittliches Gehalt pro Name
avg_salary_per_name = grouped_by_name['Gehalt'].mean()
print("Durchschnittliches Gehalt pro Name:")
print(avg_salary_per_name)

# Summe der Gehälter pro Stadt
total_salary_per_city = df.groupby('Stadt')['Gehalt'].sum()
print("\nSumme der Gehälter pro Stadt:")
print(total_salary_per_city)

# Weitere Aggregatfunktionen
sum_salary_per_name = grouped_by_name['Gehalt'].sum()
min_age_per_name = grouped_by_name['Alter'].min()
max_age_per_name = grouped_by_name['Alter'].max()
count_per_name = grouped_by_name['Name'].count()

print("\nSumme der Gehälter pro Name:")
print(sum_salary_per_name)
print("\nMinimales Alter pro Name:")
print(min_age_per_name)
print("\nMaximales Alter pro Name:")
print(max_age_per_name)
print("\nAnzahl der Einträge pro Name:")
print(count_per_name)

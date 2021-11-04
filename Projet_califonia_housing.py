# Importation des librairies
import pandas as pd  #Faire des manipulation sur les dataframe
import numpy as np  #calcul de tableau a plusieurs dimensions
import matplotlib.pyplot as plt  # Affichage avec la bibliothèque graphique intégrée a 2 dimensions
import seaborn as sns


# Importation des données
df = pd.read_csv("C:/Users/Rafa/Projet kevin/california_housing_train.csv",sep = ";")


# Voir les infos de la BDD et chercher d'éventuels missing values
df.shape
df.columns
df.info()
df.isna().sum()


# Visualiser du jeu de données
pd.set_option('display.max_columns', None) #Visualiser toutes les colonnes
df.head()
df.describe()

df.hist(bins=50, figsize = (20,15)) #le bins définit le nombre de bâtonnet et le figsize la surface de l'histogramme
plt.show()


# Affichage de la boite a moustache du median_house_value
f, axes = plt.subplots()
sns.boxplot(df["median_house_value"])
plt.show()


# Matrice de corrélation 
plt.figure(figsize=(10,5))
corr=df.corr()
ax=sns.heatmap(corr,vmin=-1,vmax=1, center=0, annot=True)


# Nuages de point
df.plot(kind="scatter", x="total_bedrooms", y= "households", s=100, c='coral') #0.98
plt.xlabel("total_bedrooms", fontsize=15, color='#c0392b')
plt.ylabel("households", fontsize=15, color='#c0392b')
plt.title("Corrélation entre le nombre de chambre et le nombre de ménage résidant dans un bloc", fontsize=18, color='#e74c3c')
plt.xticks(rotation= 45) # Rotation des données des absis 
plt.tight_layout()


df.plot(kind="scatter", x="median_house_value", y= "median_income", s=100, c='green') #0.69
plt.xlabel("median_house_value", fontsize=15, color="#095228")
plt.ylabel("median_income", fontsize=15, color="#095228")
plt.title("Corrélation entre la valeur médiane d'une résidence et le revenu médian des ménages dans un bloc", fontsize=18, color="#095228")
plt.xticks(rotation= 45) # Rotation des données des absis 
plt.tight_layout()


# Création d'une carte et exemple de marquage d'une donnée GPS
import folium
c=folium.Map(location = [34.190000, -114.310000])
folium.Marker([34.190000, -114.310000]).add_to(c)
c.save('macarte.html')


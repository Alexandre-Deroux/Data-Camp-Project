import pandas as pd

print("Creating the data...", end=" ", flush=True)

fichiers_csv = [
    "data/operators.csv",
    "data/surface_area_by_production.csv",
    "data/livestock.csv"
]

colonnes = [
    "annee",
    "code_region",
    "region",
    "code_departement",
    "departement",
    "code_epci",
    "epci",
    "code_insee_commune",
    "code_postal_commune",
    "commune"
]

df_op = pd.read_csv(fichiers_csv[0], low_memory=False)
df_op = df_op.rename(columns={
    "coderegion": "code_region",
    "codedepartement": "code_departement",
    "codeepci": "code_epci",
    "codeinseecommune": "code_insee_commune",
    "codepostalcommune": "code_postal_commune",
    "productionprincipale": "production_principale",
    "codesimple_ptdi": "code_activites",
    "nboperateur": "nombre_operateurs"
})
df_op = df_op.dropna(subset=colonnes)

df_surf = pd.read_csv(fichiers_csv[1], low_memory=False)
df_surf = df_surf.rename(columns={
    "coderegion": "code_region",
    "codedepartement": "code_departement",
    "codeepci": "code_epci",
    "codeinseecommune": "code_insee_commune",
    "codepostalcommune": "code_postal_commune",
    "code_groupe": "code_groupe_surface",
    "nb_exp": "nombre_exploitations_surface",
    "surfab": "surface_terme_conversion",
    "surfc1": "surface_conversion_annee_1",
    "surfc2": "surface_conversion_annee_2",
    "surfc3": "surface_conversion_annee_3",
    "surfc123": "surface_totale_conversion",
    "surfbio": "surface_totale_bio"
})
df_surf = df_surf.dropna(subset=colonnes)

df_chep = pd.read_csv(fichiers_csv[2], low_memory=False)
df_chep = df_chep.rename(columns={
    "coderegion": "code_region",
    "codedepartement": "code_departement",
    "codeepci": "code_epci",
    "codeinseecommune": "code_insee_commune",
    "codepostalcommune": "code_postal_commune",
    "code_groupe": "code_groupe_cheptel",
    "nb_exp": "nombre_exploitations_cheptel",
    "tetesab": "cheptel_terme_conversion",
    "tetesconversionsimult": "cheptel_conversion_simultanee",
    "tetesconversionnonsimult": "cheptel_conversion_non_simultanee",
    "tetesbio": "cheptel_total_bio"
})
df_chep = df_chep.dropna(subset=colonnes)

merged_df = pd.merge(
    df_op,
    df_surf,
    on=colonnes,
    how="outer"
)

merged_df_2 = pd.merge(
    merged_df,
    df_chep,
    on=colonnes,
    how="outer"
)

merged_df_2 = merged_df_2.dropna(subset=["code_activites"])

merged_df_2.to_csv("data/agence_bio_2008_2023.csv", index=False, encoding="utf-8")

print("Done")
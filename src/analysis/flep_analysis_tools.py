import pandas as pd


def get_mean_resto_by_day(flep_df, resto_str, filter_student_menus=True, threshold_student_menu=9.5):
    orni_df = flep_df[flep_df["Resto"] == resto_str]
    orni_df = orni_df[["Prix etudiant", "Prix doctorant", "Prix campus", "date"]]
    orni_df.dropna()

    if filter_student_menus:
        orni_df = orni_df[orni_df["Prix etudiant"] <= threshold_student_menu]

    orni_df = orni_df.groupby('date', as_index=False).mean()
    orni_df = orni_df.sort_values('date')
    return orni_df

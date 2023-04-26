import pandas as pd


def get_mean_resto_by_day(flep_df, resto_str, filter_student_menus=True, threshold_student_menu=9.5):
    resto_df = flep_df[flep_df["Resto"] == resto_str]
    resto_df = resto_df[["Prix etudiant", "Prix doctorant", "Prix campus", "date"]].copy()
    resto_df.dropna()

    if filter_student_menus:
        resto_df = resto_df[resto_df["Prix etudiant"] <= threshold_student_menu]

    resto_df = resto_df.groupby('date', as_index=False).mean()
    resto_df = resto_df.sort_values('date')
    return resto_df


def get_mean_all_restos_by_day(flep_df, filter_student_menus=True, threshold_student_menu=9.5):
    restos_df = flep_df[["Prix etudiant", "Prix doctorant", "Prix campus", "date"]].copy()
    restos_df.dropna()

    if filter_student_menus:
        restos_df = restos_df[restos_df["Prix etudiant"] <= threshold_student_menu]

    restos_df = restos_df.groupby('date', as_index=False).mean()
    restos_df = restos_df.sort_values('date')
    return restos_df

import pandas as pd


def get_mean_resto_by_day(
        flep_df,
        resto_str,
        filter_student_menus=True,
        threshold_student_menu=9.5,
        str_student_price="Prix etudiant",
        str_date_col="date",
        resto_col="Resto",
        col_list=None
):
    if col_list is None:
        col_list = ["Prix etudiant", "Prix doctorant", "Prix campus", "date"]

    resto_df = flep_df[flep_df[resto_col] == resto_str]
    resto_df = resto_df[col_list].copy()
    resto_df.dropna()

    if filter_student_menus:
        resto_df = resto_df[resto_df[str_student_price] <= threshold_student_menu]

    resto_df = resto_df.groupby(str_date_col, as_index=False).mean()
    resto_df = resto_df.sort_values(str_date_col)
    return resto_df


def get_mean_all_restos_by_day(
        flep_df,
        filter_student_menus=True,
        threshold_student_menu=9.5,
        str_student_price="Prix etudiant",
        str_date_col="date",
        col_list=None
):
    if col_list is None:
        col_list = ["Prix etudiant", "Prix doctorant", "Prix campus", "date"]

    restos_df = flep_df[col_list].copy()
    restos_df.dropna()

    if filter_student_menus:
        restos_df = restos_df[restos_df[str_student_price] <= threshold_student_menu]

    restos_df = restos_df.groupby(str_date_col, as_index=False).mean()
    restos_df = restos_df.sort_values(str_date_col)
    return restos_df

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


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


def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w


def plot_mean_student_price(
        resto_df: pd.DataFrame,
        moving_average_window=5,
        student_price_col="Prix etudiant",
        date_col="date"
):
    temp = moving_average(resto_df[student_price_col], moving_average_window)
    plt.plot(resto_df[date_col][:len(temp)], temp)


def plot_mean_all_prices(
        resto_df: pd.DataFrame,
        moving_average_window=5,
        col_list=None,
        date_col="date"
):
    if col_list is None:
        col_list = ["Prix etudiant", "Prix doctorant", "Prix campus"]

    for idx, price_range in enumerate(col_list):
        temp = moving_average(resto_df[price_range], moving_average_window)
        plt.plot(resto_df[date_col][:len(temp)], temp)
    plt.show()

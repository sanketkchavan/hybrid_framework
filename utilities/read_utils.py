"""All read, write activities on files can be done using this module"""
import pandas


def get_csv_as_list(file_path):
    df = pandas.read_csv(filepath_or_buffer=file_path, delimiter=";")
    return df.values.tolist()
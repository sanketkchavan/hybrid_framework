""" This file will be deleted. Not part of the framework
To understand - how to read csv, excel, json """
import pandas

df = pandas.read_csv(filepath_or_buffer="../test_data/test_invalid_login_data.csv", delimiter=";")

print(df)
print(df.values.tolist())
print("-" * 100)

print(df.loc[0])


print(df.loc[0].tolist())
print(df.loc[1].tolist())

print(df.index)
print(60 * "-")

"""rows to be converted into list of list or list of tuple"""

lst = []
for i in df.index:
    print(df.loc[i].tolist())
    lst.append(df.loc[i].tolist())

print(lst)

lst = []
for i in df.index:
    print(tuple(df.loc[i]))
    lst.append(tuple(df.loc[i]))

print(lst)

print(df.values)
print(df.values.tolist())

print("-" * 100)
"""Read Json File"""
dic=pandas.read_json(path_or_buf="../test_data/data.json",typ="dictionary")
print(dic)
print(dic['browser'])
print(dic['url'])
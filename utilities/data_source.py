from utilities import read_utils

# test_invalid_login_data = [
#     ("saul", "saul123", "Invalid credentials"),
#     ("kim", "kim123", "Invalid credentials")
# ]
#
# test_invalid_login_data1 = [
#     ["saul", "saul123", "Invalid credentials"],
#     ["kim", "kim123", "Invalid credentials"],
#     ["john", "john123", "Invalid credentials"]
# ]

test_add_valid_employee_data = [
    ["Admin", "admin123", "John", "J", "Wick", "John Wick", "John"],
    ["Admin", "admin123", "Peter", "p", "Wick", "Peter Wick", "Peter"]
]

test_invalid_login_data=read_utils.get_csv_as_list("../test_data/test_invalid_login_data.csv")
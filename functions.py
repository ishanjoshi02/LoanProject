TargetColumn = 'loan_status'

exclude_columns = \
        [TargetColumn,
         'Target',
         'pymnt_plan',
         'application_type',
         'collections_12_mths_ex_med',
         'policy_code',
         'zip_code',
         'title',
         '',
         ]

def string_to_int_list(string_list):

    unique_list = []

    for string in string_list:
        if string not in unique_list:
            unique_list.append(string)

    int_list = []

    for string in string_list:
        try:
            int_list.append(unique_list.index(string))
        except ValueError:
            int_list.append(-99)

    return int_list

def encode_target(df, target_column=TargetColumn):

    df_mod = df.copy()
    targets = df_mod[target_column].unique()
    map_to_int = {name:n for n, name in enumerate(targets)}
    df_mod["Target"] = df_mod[target_column].replace(map_to_int)

    return (df_mod, targets)

def encode_col(df, col):

    df_mod = df.copy()
    values = df_mod[col].values

    return string_to_int_list(values)
c_st_dependency_balance_region = {
    'constraint_class': 'c_st_dependency_balance_region',
    'constraint_parameters': {
        'column_names': ['Balance', 'Region'],
#        'extra_parameter': 10.00
    }
}

c_st_dependency_balance_employment_type = {
    'constraint_class': 'c_st_dependency_balance_employment_type',
    'constraint_parameters': {
        'column_names': ['Balance', 'Employement_Type'],
#        'extra_parameter': 10.00
    }
}

c_st_dependency_tot_transaction_amount_credit_score = {
    'constraint_class': 'c_st_dependency_tot_transaction_amount_credit_score',
    'constraint_parameters': {
        'column_names': ['Tot_Transaction_Amount', 'Credit_Score'],
#        'extra_parameter': 10.00
    }
}

# --------------------------------------------------------------------------- #

c_mt_dependency_balance_region = {
    'constraint_class': 'c_mt_dependency_balance_region',
    'constraint_parameters': {
        'column_names': ['Balance', 'Region'],
#        'extra_parameter': 10.00
    }
}

c_mt_dependency_balance_employment_type = {
    'constraint_class': 'c_mt_dependency_balance_employment_type',
    'constraint_parameters': {
        'column_names': ['Balance', 'Employement_Type'],
#        'extra_parameter': 10.00
    }
}

c_mt_dependency_tot_transaction_amount_credit_score = {
    'constraint_class': 'c_st_dependency_tot_transaction_amount_credit_score',
    'constraint_parameters': {
        'column_names': ['Tot_Transaction_Amount', 'Credit_Score'],
#        'extra_parameter': 10.00
    }
}

# --------------------------------------------------------------------------- #
#                                  FUNCTIONS                                  #
# --------------------------------------------------------------------------- #

# c_st_dependency_balance_region = {
#     'constraint_class': 'FixedIncrements',
#     'constraint_parameters': {
#         'column_name': 'Balance',
#         'increment_value': 2
#             # *2,
#             # *1.5,
#             # *0.5,
#             # *0.1,
#     }
# }
            
# c_st_dependency_balance_employment_type = {
#     'constraint_class': 'FixedIncrements',
#     'constraint_parameters': {
#         'column_name': 'Balance',
#         'increment_value': 1.5
#             # *1.5,
#             # *0.5,
#     }
# }

# c_st_dependency_tot_transaction_amount_credit_score = {
#     'constraint_class': 'FixedIncrements',
#     'constraint_parameters': {
#         'column_name': 'Credit_Score',
#         'increment_value': 2
#             # *2,
#             # *0.1,
#     }  
# }

# # --------------------------------------------------------------------------- #

# c_mt_dependency_balance_region = {
#     'constraint_class': 'FixedIncrements',
#     'table_name': 'd1', # for multi table synthesizers
#     'constraint_parameters': {
#         'column_name': 'Balance',
#         'increment_value': 2
#             # *2,
#             # *1.5,
#             # *0.5,
#             # *0.1,
#     }
# }
            
# c_mt_dependency_balance_employment_type = {
#     'constraint_class': 'FixedIncrements',
#     'table_name': 'd1', # for multi table synthesizers
#     'constraint_parameters': {
#         'column_name': 'Balance',
#         'increment_value': 1.5
#             # *1.5,
#             # *0.5,
#     }
# }

# c_mt_dependency_tot_transaction_amount_credit_score = {
#     'constraint_class': 'FixedIncrements',
#     'table_name': 'd1', # for multi table synthesizers
#     'constraint_parameters': {
#         'column_name': 'Credit_Score',
#         'increment_value': 2
#             # *2,
#             # *0.1,
#     }  
# }

# # --------------------------------------------------------------------------- #

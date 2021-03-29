# from filtration import Expression
# import json
# from boolean_parser import parse
# from sqlalchemy.ext.declarative import as_declarative

# example = 'x > 3 and y <= 2 or not z != 5'

# print(res)

# # print(test(a))

import pyparsing # make sure you have this installed
from pprint import pprint
import pandas as pd

df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
     index=['cobra', 'viper', 'sidewinder'],
     columns=['max_speed', 'shield'])

conditions = [(df['shield'] >1), (df["shield"] == 2), (df['shield'] >3), (df["shield"] == 4), (df['shield'] ==2), (df["shield"] == 6)]

def to_tuple(lst):
    print(lst)

    condition_1, operator, condition_2 = lst

    if (type(condition_1) is pyparsing.ParseResults ) and (type(condition_2 ) is pyparsing.ParseResults):#isinstance(condition_1, list) and isinstance(condition_2, list):

        if operator == "and":
            return (to_tuple(condition_1) & to_tuple(condition_2))

        return (to_tuple(condition_1) | to_tuple(condition_2))

    elif (type(condition_1) is pyparsing.ParseResults ) and (type(condition_2 ) is not pyparsing.ParseResults):
        if operator == "and":
            return (to_tuple(condition_1) & conditions[int(condition_2)-1])

        return (to_tuple(condition_1) | conditions[int(condition_2)-1])



    elif (type(condition_1) is not pyparsing.ParseResults ) and (type(condition_2 ) is pyparsing.ParseResults):
        if operator == "and":
            return (conditions[int(condition_1)-1] & to_tuple(condition_2))

        return (conditions[int(condition_1)-1] | to_tuple(condition_2))

    else:
        # return (condition_1, operator, condition_2)
        
        if operator == "and":
            return (conditions[int(condition_1)-1] & conditions[int(condition_2)-1])

        return (conditions[int(condition_1)-1] | conditions[int(condition_2)-1])

    # for nest in nested_list:
    #     if type(nest) isinstance(list):

    
#     return tuple(to_tuple(i) if isinstance(i, list) else i for i in lst)

thecontent = pyparsing.Word(pyparsing.alphanums) | 'and' | 'or'
parens = pyparsing.nestedExpr( '(', ')', content=thecontent)

test = parens.parseString("(((1 and 2) and (4 or 5)) or (3 and 6))")[0]

print(df)
print(to_tuple(test))

df.loc[to_tuple(test), "max_speed"]=1000

print(df)

# condition = ((df['shield'] >6) | (df["shield"] == 2))

# print(type(condition))
# print(df)
# df.loc[condition, 'max_speed']=100
# print(df)
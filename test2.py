import pandas as pd

possible_pawn_i_combination_i = [[0,1,2,3]]
sum_entrophy = 2.5

d = {'col1': possible_pawn_i_combination_i, 'col2': sum_entrophy}
df = pd.DataFrame(data=d)

print(df)




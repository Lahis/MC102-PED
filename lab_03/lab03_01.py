var_tosse = input()
tosse = var_tosse == "True"
var_febre = input()
febre = var_febre == "True"
var_df_respirar = input()
df_respirar = var_df_respirar == "True"

var_resultado = tosse and febre and df_respirar
resultado = var_resultado == True

print("Tosse:", var_tosse)
print("Febre:", var_febre)
print("Dificuldade para respirar:", var_df_respirar)
print("Provavelmente eh COVID-19:", tosse and febre and df_respirar) 

import pulp

prob = pulp.LpProblem("Maximizar_Lucro_Cadeiras", pulp.LpMaximize)

y1 = pulp.LpVariable('Cadeiras_Branca', lowBound=0, cat='Continuous')
y2 = pulp.LpVariable('Cadeiras_Madeira', lowBound=0, cat='Continuous')

prob += 40 * y1 + 60 * y2, "Lucro_Total"

prob += 3 * y1 + 4 * y2 <= 120, "Restrição_Madeira"
prob += 2 * y1 + 1 * y2 <= 80, "Restrição_Mão_de_Obra"

prob.solve()

print(f"Status: {pulp.LpStatus[prob.status]}")

print(f"Quantidade de Cadeiras Branca: {y1.varValue:.2f}")
print(f"Quantidade de Cadeiras Madeira: {y2.varValue:.2f}")

print(f"Lucro Máximo: R$ {pulp.value(prob.objective):.2f}")

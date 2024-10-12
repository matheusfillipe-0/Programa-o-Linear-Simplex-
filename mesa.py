import pulp

prob = pulp.LpProblem("Maximizar_Lucro_Mesas", pulp.LpMaximize)

x1 = pulp.LpVariable('Mesas_Tipo_A', lowBound=0, cat='Continuous')
x2 = pulp.LpVariable('Mesas_Tipo_B', lowBound=0, cat='Continuous')

prob += 30 * x1 + 50 * x2, "Lucro_Total"

prob += 2 * x1 + 1 * x2 <= 100, "Restrição_Madeira"
prob += 1 * x1 + 3 * x2 <= 90, "Restrição_Mão_de_Obra"

prob.solve()

print(f"Status: {pulp.LpStatus[prob.status]}")

print(f"Quantidade de Mesas Tipo A: {x1.varValue:.2f}")
print(f"Quantidade de Mesas Tipo B: {x2.varValue:.2f}")

print(f"Lucro Máximo: R$ {pulp.value(prob.objective):.2f}")

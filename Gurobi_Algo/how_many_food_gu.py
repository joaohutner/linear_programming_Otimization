from gurobipy import *
#Create a model

m = Model()

#Add variables
#lb (menor numero)
#ub (maior numero)
#obj (valor)
#vtype (continuous, integer, binary(0 ou 1))
x1 = m.addVar(lb = 0, ub = GRB.INFINITY, obj = 20, vtype = GRB.CONTINUOUS, name = 'food1')
x2 = m.addVar(lb = 0, ub = GRB.INFINITY, obj = 10, vtype = GRB.CONTINUOUS, name = 'food2')
x3 = m.addVar(lb = 0, ub = GRB.INFINITY, obj = 31, vtype = GRB.CONTINUOUS, name = 'food3')
x4 = m.addVar(lb = 0, ub = GRB.INFINITY, obj = 11, vtype = GRB.CONTINUOUS, name = 'food4')
x5 = m.addVar(lb = 0, ub = GRB.INFINITY, obj = 12, vtype = GRB.CONTINUOUS, name = 'food5')

#x = m.addVar(items, vtype = GRB.BINARY)

#Att
m.update()

#Constraint #n1 requirements: 21 units #n2 requirements: 12 units
com1 = m.addConstr(2*x1 + 0*x2 + 3*x3 + 1*x4 + 2*x5 >= 21)
com2 = m.addConstr(0*x1 + 1*x2 + 2*x3 + 2*x4 + 1*x5 >= 12)

#Optimize
m.optimize()

#Get the values
print(f"Food1 = {x1.X}")
print(f"Food2 = {x2.X}")
print(f"Food3 = {x3.X}")
print(f"Food4 = {x4.X}")
print(f"Food5 = {x5.X}")

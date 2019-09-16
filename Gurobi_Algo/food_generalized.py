'''
The Diet Problem Generalized

.Sets and Indices
->i in I: nutrients
->j in J: food types

.Data
->cj : per ouce cost food type j
->aij : quantity of nutrient i per ounce food type j
->bi : minimun daily requirements for nutrient i

.Decision Variable
->xj: the number of ounces to consume of food type j.
'''

from gurobipy import *
#Create a model

m = Model()

##Add variables##

#lb (menor numero)
#ub (maior numero)
#obj (valor)
#vtype (continuous, integer, binary(0 ou 1))

#x1 = m.addVar(lb = 0, ub = GRB.INFINITY, obj = 20, vtype = GRB.CONTINUOUS, name = 'food1')
#x2 = m.addVar(lb = 0, ub = GRB.INFINITY, obj = 10, vtype = GRB.CONTINUOUS, name = 'food2')
#x3 = m.addVar(lb = 0, ub = GRB.INFINITY, obj = 31, vtype = GRB.CONTINUOUS, name = 'food3')
#x4 = m.addVar(lb = 0, ub = GRB.INFINITY, obj = 11, vtype = GRB.CONTINUOUS, name = 'food4')
#x5 = m.addVar(lb = 0, ub = GRB.INFINITY, obj = 12, vtype = GRB.CONTINUOUS, name = 'food5')


c = [20,10,31,11,12]
J = [1,2,3,4,5]
x = [m.addVar(obj = c[j]) for j in J]

##Att##
m.update()

#Constraint #n1 requirements: 21 units #n2 requirements: 12 units
#com1 = m.addConstr(2*x1 + 0*x2 + 3*x3 + 1*x4 + 2*x5 >= 21)
#com2 = m.addConstr(0*x1 + 1*x2 + 2*x3 + 2*x4 + 1*x5 >= 12)

a = [[2,0,3,1,2],[0,1,2,2,1]]
b = [21,12]
contraints = [m.addConstr(quicksum(a[i,j]*x[j] for j in J) >= b[i]) for i in I]

#Optimize
m.optimize()

#Get the values
for i in I:
    print(f"Food{i} = {x[i]}")
#print(f"Food1 = {x1.X}")
#print(f"Food2 = {x2.X}")
#print(f"Food3 = {x3.X}")
#print(f"Food4 = {x4.X}")
#print(f"Food5 = {x5.X}")

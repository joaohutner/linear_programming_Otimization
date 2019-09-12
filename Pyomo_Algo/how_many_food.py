from pyomo.environ import *

n1 = {'food1':2,'food2':0,'food3':3,'food4':1,'food5':2}
n2 = {'food1':0,'food2':1,'food3':2,'food4':2,'food5':1}
cost = {'food1':20,'food2':10,'food3':31,'food4':11,'food5':12}
items = list(sorted(cost.keys()))
l1= 21
l2 =12

#Create a model

m = ConcreteModel()

#Add variables
m.x = Var(items, within=Binary)

#Objective
m.value = Objective(expr=sum(cost[i]*m.x[i] for i in items), sense=minimize )

#Constraint #n1 requirements: 21 units #n2 requirements: 12 units
m.req1 = Constraint(expr=sum(n1[i]*m.x[i] for i in items) >= l1)
m.req2 = Constraint(expr=sum(n2[i]*m.x[i] for i in items) >= l2)


#Optimize
solver = SolverFactory('gurobi')
status = solver.solve(m)

print(f"Status {status.solver.termination_condition}")

#Print the value of the bariables at the optimun
for i in items:
    print(f"{m.x[i]} = {value(m.x[i])}")

#Print the value of the objective
print(f"Objective = {value(m.value)}")
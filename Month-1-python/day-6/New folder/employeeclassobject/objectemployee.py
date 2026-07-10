from employee import employee
employee1=employee("jim",20,30000,True)
employee2=employee("krrish",25,25000,True)
employee3=employee("yash",32,32000,False)
print(employee1.name)
print(employee2.name)
print(employee3.on_retirement())
print(employee2.on_retirement())
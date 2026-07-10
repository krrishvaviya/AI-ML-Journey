class employee :
    def __init__(main,name,age,salary,is_promoted):      # its different from normal functions it is understood by python when used 
        main.name=name                                   #employee1=employee("jim",20000,30,True)  here employee after = is 1 st augment that is main 
        main.age=age
        main.salary=salary
        main.is_promoted=is_promoted
    
    def on_retirement(self):
        if self.age >= 30:
            return True
        else :
            return False
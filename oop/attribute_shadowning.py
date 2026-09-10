class Chai:
    temprature = "hot"
    strength = "strong"
    
cutting = Chai()
print(cutting.temprature)

cutting.temprature = "mild"
cutting.cup = "small"
print("After changing ", cutting.temprature)
print("cup size is  ", cutting.cup)
print("direct look into the class", Chai.temprature)

del cutting.temprature
print(cutting.temprature)
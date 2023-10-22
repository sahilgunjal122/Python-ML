#Numeric:
#1.int
empID=20
print(empID)
print(type(empID))

#2.float

price=34.59
print(price)
print(type(price))

#3.complex

num=10+5j
print(num)
print(type(num))

#Boolen
data1=True
print(type(data1))

data2=False
print(type(data2))

#Sequence
#1.String

fri1="Piyush"
print(fri1)
fri2="Vikas"
print(fri2)
print("\n")

#2.List

programming =["C",10,"CPP",20,"Python",30,"JAVA","C"]  #Duplicate Data is also Allowed
print(programming)                                     # Data Can be Change(Mutable)
print(programming[2])
programming[1]=100                                      # Data Can be Change(Mutable)
print(programming)
print("\n")

#3.Tuple

player=(18,"Virat",45,"Rohit",7,7,"Mahi")   #Duplicate Data is also Allowed
print(player)
#player[1]="Gill"                       # Data Can't be Changed(Immutable)
print("\n")

#4.Range
x=range(10)

for i in x:
    print(i)
print("\n")

#Set
maal={10,20,30,40,50,60}            #Duplictae Values not Allowed
print(maal)
#maal[2]=100                    Data Can't be Changed(Immutable)
print("\n")


#Dic

team={23:"Aditya",49:"Piyush",50:"Sahil"}
print(team)

team[23]="Aadi"
print(team)         #Data can be Change(Mutable)








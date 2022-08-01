"""wap to play fortune game
1.declare variable one ,two three ,four, five and six 
and assign a string value fortune for all of them
2. ask user if they want to play more or exit and assign it to variable ui
3.run while loop until ui is exit
4. under while loop ask user to enter one no from 1 to 6 and convert it to integer
5.if user input is 1 then print variable one which will be the fortune do 
same for all the no till 6

"""
one ="you are going to have a good time"
two ="god will be on your side"
three ="desire will be fulfilled"
four ="be thankful"
five ="hope for the best"
six ="you think i will fulfill"
ui=input("you want more or exit ") 

while ui!=exit:
      ui=int(input("choose one number from 1 to 6 "))
      if ui==1:
         print(one)
         ui=input("you want more or exit ")
         ui=ui.lower()
      elif ui==2:
        print(two)  
        ui=input("you want more or exit ")
        ui=ui.lower()

      elif ui==3:
        print(three)  
        ui=input("you want more or exit ")
        ui=ui.lower()

      elif ui==4:
        print(four)  
        ui=input("you want more or exit ")
        ui=ui.lower()

      elif ui==5:
        print(five)  
        ui=input("you want more or exit ")
        ui=ui.lower()

      elif ui==6:
        print(six)  
        ui=input("you want more or exit ")
        ui=ui.lower()
      else:
        print("sorry unavailable")
        ui=input("you want more or exit ")
        ui=ui.lower()
        

#Olivia Tyler/Olt28/Software Testing and QA HW 2
#Due: 3/18/2025

def bmi_calculation(userw, userh):
    calWeight(userw)
    calHeight(userh)
    return round (userw / (userh ** 2), 1) #the actual equation to calculate bmi given by the link in the assignment pdf
#return bmi #returns value that we calculated in previous line
#added round incase we dont get a whole number it doesnt make an infinite amount of decimals

def getInput():

    print("Hello! Today we will be doing a simple BMI calculation!")
   
    while True:
        try:
            userh = float(input("Please enter your height in inches: " )) #prompts the user to input their height
            userw = float(input("Please enter your weight in pounds: ")) #prompts the user to input their weight

            if userh <= 0 or userw <=0:
                raise ValueError("Error: Your input needs to be greater than 0!")

            bodymassindex = bmi_calculation(userw, userh)
            print("Your BMI is:", bodymassindex)
            cat = bmiCAT(bodymassindex)
            print(cat)

        except ValueError:
            print("Error: Please enter a valid numeric input!")
            
            break 


def calWeight(userw):
        return userw * .45 #number was given

def calHeight(userh):
        return userh * 0.025 #number was given

def bmiCAT(bodymassindex):      
            #This is just determining the bmi categroy
            if bodymassindex < 18.5:
                return "Category: Underweight"
            elif 18.5 <= bodymassindex < 24.9:
                return "Category: Normal Weight"
            elif 25 <= bodymassindex < 29.9:
                return "Category: Overweight"
            else:
                return "Category: Obese"
      
if __name__ == "__main__":
    getInput()

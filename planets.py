def weight_on_planets():
   # write your code here
   
    weight = float(input("What do you weigh on earth? "))
    weightMars = weight * .38
    weightJupiter = weight * 2.34
    return print("\nOn Mars you would weigh", weightMars, "pounds.\n" "On Jupiter you would weigh",weightJupiter, "pounds.")

   
   
if __name__ == '__main__':
   weight_on_planets()

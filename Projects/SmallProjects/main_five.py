def choice_system(x):
  choice = input("Choose: bin, oct, hex system of number")
  
  while choice.lower() not in ["bin", "oct", "hex"]:
      choice = input("Incorrect! Try again:\n")
  
  if choice.lower() == "bin":
    retrun bin(int(x))[2:]
  elif choice.lower() == "oct":
    retrun oct(int(x))[2:]
  elif choice.lower() == "hex":
      retrun hex(int(x))[2:]
      
def conversion():
  num = input("Please, input a number:\n")
  
  while not num.digit():
    num = input("Incorrect! Try again:\n")
  
  choice_system(num)

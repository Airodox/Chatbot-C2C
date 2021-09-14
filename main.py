
#introduction
print ("Hello, I am AI, before I help you please answer the following questions.")
answer1 = input ("how is your day (good/bad)")
a=1
while a==1:
  if answer1 == "good":
    print ("great, me too!")
    a=0
     
  
  elif answer1 == "bad":
    print ("hope it gets better!")
    a=0
    
  else:
    print ("I did not get that, can you repeat? (good/bad)")
    
#support qustions
print ("what is it that you need help with?(type 1,2,3,4 or 5)")
print ("1) Tecnology support")
print ("2) Report an employe")
print ("3) Report bug with AI")
print ("4) Other (Experemental option)") 
print ("5) Nevermind")
answer2 = input 
b=1
while b==1:
  #Technolagy support
  if answer2 ==1:
    print("What do you need help with?")
    b=0
  #Report an employe
  elif answer2 ==2:
    print("What is the name of the employe?")
    empName = input ("Employe name: ")
    print("what did they do wrong?")
    input
    print("Thank you for reporting " + empName + ".")
  #Report bug with AI"
  elif answer2 ==3:
    print("ErOrE CaNoT ReCeIvE CoMaNd")
    print("Restarting")
    print("restart complete, pleaze do not chose this option again untill it is fixed")
  #Other (Experemental option)
  elif answer2 ==4:
    print("Not yet implememnted (WIP)")
    b=1
  #Finnish talking
  elif answer2 ==5:
    print("")
  else:
    print("please choose 1,2,3,4 or 5")
    print ("1) Tecnology support")
    print ("2) Report an employe")
    print ("3) Problems with a product")
    print ("4) Report bug with AI") 
    print ("5) Other (Experemental option)")
    b=1


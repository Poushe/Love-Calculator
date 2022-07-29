# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
fullname1=name1+name2
fullname=fullname1.lower()
t=fullname.count('t')
r=fullname.count('r')
u=fullname.count('u')
e=fullname.count('e')
total=t+r+u+e
l=fullname.count('l')
o=fullname.count('o')
v=fullname.count('v')
e=fullname.count('e')
total_Love=l+o+v+e
love_scr=int(str(total)+str(total_Love))
if (love_scr <10) or (love_scr>90):
  print(f'Your score is {love_scr}, you go together like coke and mentos.')
elif (love_scr >= 40) and (love_scr <=50):
  print(f'Your score is {love_scr}, you are alright together.')
else:
  print(f'"Your score is {love_scr}."')



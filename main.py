# Lost wallet adventure
#Interactive Fiction
#Angel De Jesus

print ("Lost Wallet Adventure!")
print ("You're walking around the main place mall with your friend Wilson, out of all days you come at the busiest hour! ")
print ("you see a old man drop his wallet - what do you and your friend do?")
print ("pick up the wallet type 'p' or steal money from wallet type 's' ")
answer = input()

if answer == "p":
  print("YOU picked up")
  print("*security guard Joseph has spotted you!*")
  print("you explain what happened")
  print("security guard joseph asks if you want to give the wallet to him type 'g' to turn in or help him out type 'h'")
  answer = input()
  if answer =="h":
    print("Thank you for letting us help you Mr.Joseph!")
    print("Joseph- alright lets get on my cart and go to the office to report this")
    print("Joseph- This is the office and we're going to look at the security footage")
    print("alright 15 minutes ago he dropped it and lets see.... tell me once you see him in one of those other monitors")
    print("alright!")
    print("*10 minutes later)")
    print("Oh I see the person! He's about to go to the register in the nike store!")
    print("Joseph-hey can you stop the man that's about to go to the register, we've got his wallet")
    print("alright guys thank you for helping me, have a nice day")
    print("SG Joseph goes to the person, and in disbelief he is shocked to meet Elon Musk")

  else:
    print("Security Guard Joseph- Hey reporting lost wallet")
    print("can you make an announcement using the mall speakers?")
    print("Their name is Elon musk")
    print("HEY WILSON THAT WALLET WE TURNED IN, WE COULD HAVE MET ELON MUSK DUDE!")
else:
  print("gained 'lost wallet'!!")
  print("*security guard Joseph spotted you!*")
  print("type 'r' to run with the wallet or type 'y' to yell lost wallet")
  answer = input()
  if answer =="r":
    print("*your friend wilson grabs the wallet from you and is chased*")
    print("yells owners name while running") 
    print("Security guard Joseph bashes wilson to the ground")
    print("Wilson-hey what are you doing?! I'm trying to give back this wallet!")
    print("SG Joseph- Hey you acted without thinking, I assumed you were running!")
    print("Wilson- I thought it would've been faster to just run and yell the owners name!")
    print("SG joseph- next time think before you act, you're off the hook kid ")
    print("*eventually owner comes for the wallet*")
    print("NO WAY IS THAT THE REAL ELON MUSK?!!!")
    print("Elon musk- hey kid thank you for trying to give me my wallet, here take this ")
    print("you and wilson gain 200$ each!!")
  else:
    print("you yell out the owners name from his ID in the wallet")
    print("your recieve accolades from security guard Joseph for integrity of returning wallet")
    print("you realize it's THEE ELON MUSK")
    
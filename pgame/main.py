print ("Welcome to my first game !")
name = input("what is your name ? ")
age = int(input("what is your age ? "))

health = 10

if age >= 18: 
  print("you are older enough to play")
  wants_to_play = input("do you want to play? ").lower()
  if wants_to_play == "yes":

    print("You are starting with ", health, "health")
    print("let's play")

    left_or_right = input("First choice ... Left or Right (left/right)? ")
    if left_or_right == "left":
      ans = input("Nice, you follow the path and reach a lake ...Do you swim across or go around (across/around)? ")

      if ans == "around":
         print("You went around and reach the other side of the lake")
         
      elif ans == "across":
         print("You managed to get across, but were bit by a fish and lost 5 health")  
         health -= 5

         ans = input("You notice a house and a river. Which do you go to (river/house)? ") 
         if ans == "house":  
           print("you go to the house and are greted by the owner ... He doesn't like you and you loss 5 health ")
           health -= 5

           if health <= 0:
             print("you now have 0 health and you lost the game")

           else:
             print("you have survived.... you win ! ")


    else:
         print("you fell down and lost ...")


  else:
     print("see ya ...")

else:
  print("you are not old enough to play")

 
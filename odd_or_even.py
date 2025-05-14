import random 
def less_6():
    while(1):
        try:
            tose=int(input("enter the tose number:"))
            if tose<=6 and tose>=0:
               return tose
            else:
              print("Enter number upto 0 - 6 only 😅")    
        except:
             print("Enter the number upto 0 - 6 only 😅")     

def desider(inputer):
   if (((inputer.upper()).strip())=="ODD" ):
       return 0
   elif(((inputer.upper()).strip())=="EVEN"):
       return 1
   else:
       print("enter even or odd only😅") 
def desider_2nd(inputer):
   if (((inputer.upper()).strip())=="BATTING" ):
       return 0
   elif(((inputer.upper()).strip())=="BALLING"):
       return 1
   else:
       print("enter batting or balling only😅")        
def Ai_player():
     return (random.randint(1,6))      
def game_batting_Ai():
     print("i will bat.....😏")
     print("enter your number")
     score=0
     gest_player=None
     Ai=Ai_player()
     if player_final_score != None:
             while ( score<=player_final_score):
                  Ai=Ai_player()
                  gest_player=less_6()
                  if gest_player >6:
                     print("enter value 0 to less than or 6 😃")
                  else:     
                      if ( Ai == gest_player):
                            print("am out 😭\n")
                            break
                      else:
                            print("am scoring 😃")
                            print(f"my tose number : {Ai}")
                            score += Ai
             if   player_final_score==None:
                    if score <10: 
                          print (f"my total score 🤣 :{score} \n yo  need {score + 1} to win 🙂")
                    else:
                           print (f"my total score 😁:{score} \n you need {score + 1} to win 😏")
     else :
         while ( Ai != gest_player):
             Ai=Ai_player()
             gest_player=less_6()
             if gest_player >6:
                 print("enter value 0 to less than or 6😃")
             else:     
                if ( Ai == gest_player):
                      print("am out 😭\n")
                      break
                else:
                      print("am scoring 😃")
                      print(f"my tose number : {Ai}")
                      score += Ai
         if   player_final_score==None:
               if score <10: 
                    print (f"my total score 🤣 :{score} \n yo  need {score + 1} to win 🙂")
               else:
                    print (f"my total score 😁:{score} \n you need {score + 1} to win 😏")
     return score 
def game_balling_Ai():
         print("I will ball ⚾ u  :) \n") 
         print("enter your number  :")
         score=0
         gest_player=None
         Ai=Ai_player()
         if Ai_final_score != None:
             while ( score<=Ai_final_score):
                     Ai=Ai_player()
                     gest_player=less_6()
                     if gest_player >6:
                          print("enter value 0 to less than or 6😃")
                     else:     
                           if ( Ai == gest_player):
                                  print("you out 🤣_____out_____🤣_____out____🤣_____)\n")
                                  break
                           else:
                               print("good 🏏 shot...")
                               print(f"my tose number : {Ai}")
                               score += gest_player
             if Ai_final_score== None:
                       if score <10: 
                            print (f"your total score 🤣 :{score} \n I need {score + 1} to win 😏\n")
                       else:
                             print (f"your total score 🤩 :{score} \n I need {score + 1} to win 😅\n")
         else:
             while ( Ai != gest_player):
                     Ai=Ai_player()
                     gest_player=less_6()
                     if gest_player >6:
                          print("enter value 0 to less than or 6 😃")
                     else:     
                           if ( Ai == gest_player):
                                  print("you out 🤣_____out_____🤣_____out____🤣_____)\n")
                                  break
                           else:
                               print("good 🏏 shot...")
                               print(f"my tose number : {Ai}")
                               score += gest_player
             if Ai_final_score== None:
                       if score <10: 
                            print (f"your total score 🤣 :{score} \n I need {score + 1} to win 😏\n")
                       else:
                             print (f"your total score 🤩 :{score} \n I need {score + 1} to win 😅\n")
         return score     
#____________MAIN BLOCK ______________#
print ("let's play odd or even")
print("hmm...odd or even 😏??")
player_final_score=None
Ai_final_score=None
ch=None
while ch==None:
    player_choise=input()
    ch=desider(player_choise)
print("let's start😄")   
if ch==1:
    Ai_choos=0#odd
else:
    Ai_choos=1#even
    
tose=less_6()
result_tose=None
if ((Ai_player())%tose==0):
        result_tose=1#even
else:
        result_tose=0#odd    
        
if result_tose==Ai_choos: 
    chooser=random.randint(1,2)#ai deside
    if chooser==1:
       player_final_score= game_balling_Ai()
       Ai_final_score=game_batting_Ai()
    else:
       Ai_final_score=game_batting_Ai()     
       player_final_score=game_balling_Ai()
else:
    desided= None#player deside   
    while (desided != (1 or 0)):
        if (desided != (1 or 0)):     
             print("\n")
             gest_chois=input("your turn enter batting🏏 or balling⚾\n")
             desided=desider_2nd ( gest_chois )
             if  (desided == 1 or desided==0):   
                   break
    if   (desided== 0):
                player_final_score= game_balling_Ai()
                Ai_final_score=game_batting_Ai()
    elif (desided==1):
                 Ai_final_score=game_batting_Ai()     
                 player_final_score=game_balling_Ai()
if Ai_final_score>=player_final_score:
    if Ai_final_score>player_final_score:
        print(f"I am the winner  🏆 you loss 😏my score: {Ai_final_score}")
    else:
        print(f"it's a draw🙂💯 our score: {Ai_final_score}")
else:
    print(f"you are the winner  🏆 ✨ your score: {player_final_score}")
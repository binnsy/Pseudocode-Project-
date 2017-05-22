# ADVENTURE AWAITS is an adventure game!

def greet_user():
    """Prints intro greeting."""

print("\033[1;32;47m \n")
print "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

print "Welcome to Adventure Awaits! \n"

print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

print    "             /\ "
print    "            /  \        /\       "
print    "       /\  /    \      /  \    /\ "
print    "      /  \/      \    /    \  /  \ "
print    " /\  /            \  /      \/    \ "
print    "/  \/              \/              \ "



print "Spring has sprung and adventure awaits! \n"
print("\033[0;32;47m  \n")
print "Your goal in this adventure is to make it to the cabin at the top of the \nmountain before night. This is a 20 mile hike, so do not rush, but be \ncareful how you use your time. Be ware of the heavy flowing \nrivers, fresh spring snowfall, animals, and other obstacles that you may \nencounter. Choose the path that you think it the best fit. \n"   


name = raw_input("What is your name?\n")

print "\n" + name + ", you are in for quite the adventure!"



def ask_if_continue():
    """ask the user if they would like to accept this mission or exit"""
    print("\033[0;36;47m  \n")
    playing = raw_input("Would you like to start an adventure? \n(type exit to exit) \n")
    if playing == "exit":
        exit()
    if playing == "no":
        exit()
    return playing 



def accept_the_journey(): 
    """if user has accepted journey, give them options A or B for the different paths"""
    print("\033[0;35;47m  \n")
    print "\n" + name +", you have accepted this journey. \nNow you have two paths to choose from:"
    print("\033[1;35;47m ")
    print "Terrible Terrain or Simply Safer."


    print("\033[0;35;47m  \n")
    Route_of_choice = raw_input("Enter terrible terrain if you want to hike the shortest distance, \nbut this is the most treacherous route up \nor enter simply safer if you want to take the longer, \nbut safer route to the top. \n")
    
    print("\033[0;34;47m  \n")
    if Route_of_choice == "terrible terrain":
        
        print "\nYou have chosen to take the terrible terrain path to the top. Be careful! \n"

        
        print "Start off by heading North into the dark woods. When you reach mile 4 the path will split. \nYou have the choice of taking the path leading behind the waterfall or the path that leads around the waterfall. \nBe ware when choosing. The temperatures are cold and the water is rushing. "
        path_choice = "terrible terrain"

    else:
        print "You have chosen to take the simply safer path to the top. Better safe than sorry!"
        path_choice = "simply safer"


    

    return path_choice


def Obstacle_one_TT():
    """this is the first obstacle the user will come across"""    
    print("\033[0;32;47m  \n")
    Obstacle_one_TT = raw_input("Enter waterfall to choose the route that cuts behind the waterfall \nor enter around to surpass the waterfall and go around.\n")


    if Obstacle_one_TT == "waterfall":
        print "You chose to take the risk. As you near the falls, the path is getting muddier. \nSoon the water is above the ankles and the path is under water. \nThe only way to continue is by becoming soaked. Would you like to keep going?"

        Continue_through_waterfall = raw_input("Are you sure you would like to contunue? This is a dangerous route.\n")

        if Continue_through_waterfall == "yes":
            print("\033[0;31;47m  \n")
            print "You have made it to the other side, but hypothermia is slowly setting in. You cannot continue on. \nPlease return home and try again tomorrow."
            
            print("\033[1;31;47m  \n")
            print"         =================================="
            print"        ===================================="
            print"       ======================================"
            print"      ========  ====  ==========  ====  ======"
            print"     ==========  ==  ============  ==  ========"
            print"    =============  ================  =========="
            print"   ============  ==  ============  ==  ========="
            print"  ============  ====  ==========  ====  ========="
            print"  ==============================================="
            print"  ==============================================="
            print"  ==============================================="
            print"   =============================================="
            print"    ===============                ============="
            print"     =========================================="
            print"      ======================================="
            print"       ===================================="
            print"        ================================="

            print"                    GAME OVER\n"

            return True     


        if Continue_through_waterfall == "no":
            print "You have become damp and cold and lost some time, but you are still able to continue the trek \nbecause you were smart and chose to retreat from that path."

    else:
        print "You chose to go around the waterfall. Smart choice because the rest of the crew was sent back \nfrom the waterfall or did not make it."

    return False



def Obstacle_two_TT():
    """this is the second obstacle the user will come across"""
    print("\033[0;30;47m  \n")
    print "\nNext you come to a dead end, the only way out is up. There is a rope and a ladder that lead up. \nBoth look a little timeworn, but the only other route is an hour out of the way.  \nYou can either choose to proceed up or take the long route.\n "

    Obstacle_two_TT = raw_input("Enter up to proceed up or around to proceed around this obstacle.\n")

    if Obstacle_two_TT == "up":
        print "It looks a little scary, but you can do it. Be careful."
        print "Oh no your water fell out of your pack as soon as your reached the top \nand burst about 30 feet below."


    if Obstacle_two_TT == "around":
        print "Turns out you do not have time for this route, you must return to the ladder and rope to get up. \n Somewhere along the way you lost your water."


        


def Obstacle_three_TT():
    """this is the third obstacle the user will come across"""
    print("\033[0;35;47m  \n")
    print "After making it to the top, you are thirsty and need water. What should you do? \nYou check the map. There is a pond right along the path or there is a stream about a mile out of the way. \nBe careful with the sanitation of the water.\n"
    
    Obstacle_three_TT = raw_input("Would you rather drink from the pond or stream?\n")

    if Obstacle_three_TT == "pond":
        print("\033[0;31;47m  \n")
        print "You choose to drink from the pond. After a few sips, your stomach is turning and you are getting dizzy. \nThere was a still water bacterium in the water from sitting. You should have chosen the stream. \nYou have to call in medics and are too weak to reach the top tonight.\n"
        print("\033[1;31;47m  \n")
        print"         =================================="
        print"        ===================================="
        print"       ======================================"
        print"      ========  ====  ==========  ====  ======"
        print"     ==========  ==  ============  ==  ========"
        print"    =============  ================  =========="
        print"   ============  ==  ============  ==  ========="
        print"  ============  ====  ==========  ====  ========="
        print"  ==============================================="
        print"  ==============================================="
        print"  ==============================================="
        print"   =============================================="
        print"    ===============                ============="
        print"     =========================================="
        print"      ======================================="
        print"       ===================================="
        print"        ================================="

        print"                    GAME OVER\n"


        return True
        """Would you like to start a new game or exit?"""

    if Obstacle_three_TT == "stream":
        print "You have chosen to drink from the heavy flowing stream. Good idea! \nAlthough this is further out of the way, there is less bacteria in water that flows.\n"

    return False




def Obstacle_four_TT():
    print("\033[0;32;47m  \n")
    print "You are nearing the top and the snow is getting thick. \nThere was a fresh snow at the top of the mountain from the night before. \nThe sun is still awake, but lowering in the sky. You have to reach camp before the sun sets. \nTaking the straight up path is risky due to the snow. Going around may be the safer route."

    Obstacle_four_TT = raw_input("Would you like to go straight up?\n")

    if Obstacle_four_TT == "yes":
        print "Watch where you are stepping because the snow is thick.\n" 

        Continue_obstacle_four_TT = raw_input("Are you sure you want to continue?\n")

        if Continue_obstacle_four_TT == "yes":
            print("\033[0;31;47m  \n")
            print "Ut oh, your foot slips and you try to throw your ice pick into the snow, \nbut that makes it worse. An avalanche is happening. \nYou got swept away down the mountain and berried.\n"
            print("\033[1;31;47m  \n")
            print"         =================================="
            print"        ===================================="
            print"       ======================================"
            print"      ========  ====  ==========  ====  ======"
            print"     ==========  ==  ============  ==  ========"
            print"    =============  ================  =========="
            print"   ============  ==  ============  ==  ========="
            print"  ============  ====  ==========  ====  ========="
            print"  ==============================================="
            print"  ==============================================="
            print"  ==============================================="
            print"   =============================================="
            print"    ===============                ============="
            print"     =========================================="
            print"      ======================================="
            print"       ===================================="
            print"        ================================="

            print"                    GAME OVER\n"

            return True

        if Continue_obstacle_four_TT == "no":
            print "Great choice! I know you are tired, but this is the safest bet. \nProceed around the peak with caution.\n"

    if Obstacle_four_TT == "no":
        print "Great choice! I know you are tired, but this is the safest bet. \nProceed around the peak with caution.\n"

    return False   



def Obstacle_five_TT():
    print("\033[0;30;47m  \n")
    print "You can see the glow of the fire in the cabin at the top. \nOnly about a mile left, when all of a sudden you hear something like a branch breaking behind you. \nYou slowly turn around. There is a 10 foot bear about 20 feet away.\n"

    Obstacle_five_TT = raw_input("Do you want to run, play dead, or fight the bear?\n")

    if Obstacle_five_TT == "run":
        print("\033[0;31;47m  \n")
        print "The snow is so thick and the bear is catching up. There is no way you can outrun the bear. \nHe catched up and attacks. So close, yet so far from the top. \nToo injured to continue on. You will not make it today.\n"
        print("\033[1;31;47m  \n")
        print"         =================================="
        print"        ===================================="
        print"       ======================================"
        print"      ========  ====  ==========  ====  ======"
        print"     ==========  ==  ============  ==  ========"
        print"    =============  ================  =========="
        print"   ============  ==  ============  ==  ========="
        print"  ============  ====  ==========  ====  ========="
        print"  ==============================================="
        print"  ==============================================="
        print"  ==============================================="
        print"   =============================================="
        print"    ===============                ============="
        print"     =========================================="
        print"      ======================================="
        print"       ===================================="
        print"        ================================="

        print"                    GAME OVER\n"

        return True


    if Obstacle_five_TT == "fight the bear":
        print("\033[0;31;47m  \n")
        print "You take out your ice pick and slash the bear coming at you. \nBAD DECISION! \nYou just made the bear very angry and he fights back and wins. \nYou will not be making it to the top.\n"
        print("\033[1;31;47m  \n")
        print"         =================================="
        print"        ===================================="
        print"       ======================================"
        print"      ========  ====  ==========  ====  ======"
        print"     ==========  ==  ============  ==  ========"
        print"    =============  ================  =========="
        print"   ============  ==  ============  ==  ========="
        print"  ============  ====  ==========  ====  ========="
        print"  ==============================================="
        print"  ==============================================="
        print"  ==============================================="
        print"   =============================================="
        print"    ===============                ============="
        print"     =========================================="
        print"      ======================================="
        print"       ===================================="
        print"        ================================="

        print"                    GAME OVER\n"

        return True 

    if Obstacle_five_TT == "play dead":
        print "Playing dead is the best option. The bear is still coming towards you, \nbut you stay down in a ball. He sniffs you and sticks out his paw to pet you, \nbut then walks away. You wait a little until he is gone. Then continue on. \nFEW! That was a close one.\n"

    return False 


def Made_it_to_the_top_TT():
    print("\033[1;32;47m  \n")
    print "It is now dusk and you are cold and scared. \nYou have made it this far, keep it going. \n"
    print "CONGRADULATIONS!! \nFinally you have made it to the top where a warm fire and dinner awaits with companions.\n"
 
 



    print"         =================================="
    print"        ===================================="
    print"       ======================================"
    print"      ========================================"
    print"     ===========    =============    =========="
    print"    ===========      ===========      =========="
    print"   =============    =============    ============"
    print"  ==============================================="
    print"  ==============================================="
    print"  ==============================================="
    print"  ============   ===================   =========="
    print"   =============   ===============   ==========="
    print"    ==============   ===========   ============"
    print"     ===============   =======   ============="
    print"      =================        =============="
    print"       ====================================="
    print"        =================================="
  

    return True


"""SIMPLY SAFERRRRRRRRR"""

def Obstacle_one_SS():
    print("\033[0;35;47m  \n")
    print "\nStart off by heading west past the meadows into the canyon. \nYou come across a sign that says be ware, flash floods ahead. \nThe weather does look a little iffy.\n"    
    
    Obstacle_one_SS = raw_input("would you rather continue ahead ignoring the signs \nor bypass the canyon going an extra 4 miles out of the way? \nEnter continue or bypass\n")
    print("\033[0;30;47m  \n")
    if Obstacle_one_SS == "continue":
        print("\033[0;31;47m  \n")
        print "You chose to risk the path of the canyon. The clouds are getting darker and darker. \nTwo miles into the canyon, the skys release. \nFirst with the hail, then comes the rain. \nThere is no shelter and no way out. The water gets highter and highter and eventually \nyou are swept up in the strong current. You have lost too much time \nand are not in healthy enough condition to continue on today.\n"
        print("\033[1;31;47m  \n")
        print"         =================================="
        print"        ===================================="
        print"       ======================================"
        print"      ========  ====  ==========  ====  ======"
        print"     ==========  ==  ============  ==  ========"
        print"    =============  ================  =========="
        print"   ============  ==  ============  ==  ========="
        print"  ============  ====  ==========  ====  ========="
        print"  ==============================================="
        print"  ==============================================="
        print"  ==============================================="
        print"   =============================================="
        print"    ===============                ============="
        print"     =========================================="
        print"      ======================================="
        print"       ===================================="
        print"        ================================="

        print"                    GAME OVER\n"

        return True 

    if Obstacle_one_SS == "bypass":
        print "Great decision. The path may be a little longer, \nso you may have to walk a little faster, but this was the smartest choice. \n"

    return False


def Obstacle_two_SS():
    print("\033[0;30;47m  \n")
    print "After detouring around the canyon and now heading up into the woods, \nyou come across a heavy flowing river. The water only comes up to your waist, \nbut it is rapid and unsteady. You can either try and walk/jump across \nor build a bridge with wood nearby. \n"

    Obstacle_two_SS = raw_input("Would you like to jump across or build a bridge?\n")

    if Obstacle_two_SS == "jump":
        print("\033[0;31;47m  \n")
        print "Unfortunately, the river is too wide to jump across, so you step your foot in and \nfirst thing you are pulled under by the raging river. \nSoaked and lost too much time by being pulled a few miles down stream, \nyou have to return home. \n"
        print("\033[1;31;47m  \n")
        print"         =================================="
        print"        ===================================="
        print"       ======================================"
        print"      ========  ====  ==========  ====  ======"
        print"     ==========  ==  ============  ==  ========"
        print"    =============  ================  =========="
        print"   ============  ==  ============  ==  ========="
        print"  ============  ====  ==========  ====  ========="
        print"  ==============================================="
        print"  ==============================================="
        print"  ==============================================="
        print"   =============================================="
        print"    ===============                ============="
        print"     =========================================="
        print"      ======================================="
        print"       ===================================="
        print"        ================================="

        print"                    GAME OVER\n"

        return True

    if Obstacle_two_SS == "build a bridge":
        print "This may take a little longer, but it is the safest bet. \nThere is only enough wood to make a small bridge. \nYour pack weighs 70 lbs, but both you and your pack probably cant make it.\n"
    return False
    if Obstacle_two_SS == "build":
        print "This may take a little longer, but it is the safest bet. \nThere is only enough wood to make a small bridge. \nYour pack weighs 70 lbs, but both you and your pack probably cant make it.\n"
    return False



def Obstacle_two_SS_Cross_Bridge():
        print("\033[0;32;47m  \n")
        Obstacle_two_SS_Cross_Bridge = raw_input("Enter A to cross the bring only a few things across \nor enter B to try and throw your pack across the river.\n")

        if Obstacle_two_SS_Cross_Bridge == "A":
            print "Take only a few things you need. \nOver half way to the top, you take the bare minimum and make it across.\n"

        if Obstacle_two_SS_Cross_Bridge == "B":
            print "You thought you could make it across, but the bag hits off the edge of the other side of the river\n and gets taken down stream. Left with nothing. \nLuckily if you are smart, you can still make it. \n"

def Obstacle_three_SS():
    print("\033[0;35;47m  \n")
    print "You are safely across the bridge, but with little to nothing left. \nYou continue walking and realize you grabbed your water, but forgot any sort of food. \nYour muscles are tired and need to be fueled before moving on. \nYou see a patch of mushrooms and a raspberry bush. \nYou read that the mushrooms were safe, \nbut there was nothing in the book about rasberries. \n"

    Obstacle_three_SS = raw_input("Even though you hate mushrooms, do you eat the mushrooms \nor take a risk on the rasberries?\n")

    if Obstacle_three_SS == "mushrooms":
        print "Good choice. Better to be safe then sorry. Hold your nose and swallow. \nWe only need a little fuel to reach the top. \n"

    if Obstacle_three_SS == "rasberries":
        print("\033[0;31;47m  \n")
        print "Risky choice. These are not actually raspberries. \nThey are a poisonous berry that has required immediate medical attention. \nYou will have to be medivacked out and can no longer continue on this trek. \n"
        print("\033[1;31;47m  \n")
        print"         =================================="
        print"        ===================================="
        print"       ======================================"
        print"      ========  ====  ==========  ====  ======"
        print"     ==========  ==  ============  ==  ========"
        print"    =============  ================  =========="
        print"   ============  ==  ============  ==  ========="
        print"  ============  ====  ==========  ====  ========="
        print"  ==============================================="
        print"  ==============================================="
        print"  ==============================================="
        print"   =============================================="
        print"    ===============                ============="
        print"     =========================================="
        print"      ======================================="
        print"       ===================================="
        print"        ================================="

        print"                    GAME OVER\n"

        return True

    return False



def Obstacle_four_SS():
    print("\033[0;30;47m  \n")
    print "After more hours of hiking, the sun is setting and you become very tired.  \nThere is a shortcut up the face of this rock that you can free climb or you can go around.\n"

    Obstacle_four_SS = raw_input("Do you want to climb or go around?")

    if Obstacle_four_SS == "climb":
        print("\033[0;31;47m  \n")
        print "You are too tired and your foot slips and you are no longer able to hold on. \nYou land about 20 feet below and can not move your legs. \nYOu have to call medical help and get to a hospital right away. \n"
        print("\033[1;31;47m  \n")
        print"         =================================="
        print"        ===================================="
        print"       ======================================"
        print"      ========  ====  ==========  ====  ======"
        print"     ==========  ==  ============  ==  ========"
        print"    =============  ================  =========="
        print"   ============  ==  ============  ==  ========="
        print"  ============  ====  ==========  ====  ========="
        print"  ==============================================="
        print"  ==============================================="
        print"  ==============================================="
        print"   =============================================="
        print"    ===============                ============="
        print"     =========================================="
        print"      ======================================="
        print"       ===================================="
        print"        ================================="

        print"                    GAME OVER\n"

        return True 

    if Obstacle_four_SS == "around" or "go around":
        print " You are tired, but this is the safest bet for you and after seeing the light \nfrom the fire in the cabin, you regain a little strength \nand are able to make it to the top! \n"

    return False 


def Made_it_to_the_top_SS():
    print("\033[1;32;47m  \n")
    print "It is now dusk and you are cold and scared. \nYou have made it this far, keep it going.\n"
    print "CONGRADULATIONS!! \nFinally you have made it to the top where a warm fire and dinner awaits with companions.\n"

    

    print"         =================================="
    print"        ===================================="
    print"       ======================================"
    print"      ========================================"
    print"     ===========    =============    =========="
    print"    ===========      ===========      =========="
    print"   =============    =============    ============"
    print"  ==============================================="
    print"  ==============================================="
    print"  ==============================================="
    print"  ============   ===================   =========="
    print"   =============   ===============   ==========="
    print"    ==============   ===========   ============"
    print"     ===============   =======   ============="
    print"      =================        =============="
    print"       ====================================="
    print"        =================================="
  

    return True


def main():
    """Runs the horiscope games"""


    greet_user()

    playing = True

    while playing:

        playing = ask_if_continue()

        path_of_choice = accept_the_journey()
        if path_of_choice == "terrible terrain":



            is_game_over = Obstacle_one_TT()
            if is_game_over:
                continue

            Obstacle_two_TT()


            is_game_over = Obstacle_three_TT()
            if is_game_over:
                continue 

            is_game_over = Obstacle_four_TT()
            if is_game_over:
                continue

            is_game_over = Obstacle_five_TT()
            if is_game_over:
                continue

            is_game_over = Made_it_to_the_top_TT()
            if is_game_over:
                continue 



        if path_of_choice == "simply safer":

            is_game_over = Obstacle_one_SS()
            if is_game_over:
                continue 
            
            is_game_over = Obstacle_two_SS()
            if is_game_over:
                continue 
            
            is_game_over = Obstacle_three_SS()
            if is_game_over:
                continue 
            
            is_game_over = Obstacle_four_SS()
            if is_game_over:
                continue 
            
            is_game_over = Obstacle_five_SS()
            if is_game_over:
                continue 
            
            is_game_over = Made_it_to_the_top_SS()
            if is_game_over:
                continue 

        else:
            print "please enter terrible terrain or simply safer"

main()

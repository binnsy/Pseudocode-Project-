# ADVENTURE AWAITS!

def greet_user():
    """Prints intro greeting."""

print "Welcome to Adventure Awaits!"

"""space"""

print "Spring has sprung and adventure awaits. Your goal in this adventure is to make it to the cabin at the top of the mountain before night. This is a 20 mile hike, so do not rush, but be careful how you use your time. Be ware of the heavy flowing rivers, fresh spring snowfall, animals, and other obstacles that you may encounter. Choose the path that you think it the best fit."   

"""space"""

name = raw_input("What is your name?") 

print name + ", you are in for quite the adventure!"



def ask_if_continue():
    """ask the user if they would like to accept this mission or exit"""

playing = raw_input("Would you like to accept this adventure?(type exit to exit) ")




def accept_the_journey(): 
    """if user has accepted journey, give them options A or B for the different paths"""

print name +", you have accepted this journey. Now you have two paths to choose from: Terrible Terrain or Simply Safer."



Route_of_choice = raw_input("Enter terrible terrain if you want to hike the shortest distance, but this is the most treacherous route up or enter simply safer if you want to take the longer, but safer route to the top.")
    
if Route_of_choice == "terrible terrain":
    print "You have chosen to take the terrible terrain path to the top. Be careful!"

    """space"""
    print "Start off by heading North into the dark woods. When you reach mile 4 the path will split. You have the choice of taking the path leading behind the waterfall or the path that leads around the waterfall. Be ware when choosing. The temperatures are cold and the water is rushing. "


else:
    print "You have chosen to take the simply safer path to the top. Better safe than sorry!"

"""HOW DO I MAKE ANOTHER PATH?!"""



def Obstacle_one_TT():
    """this is the first obstacle the user will come across"""    

    Obstacle_one_TT = raw_input("Enter waterfall to choose the route that cuts behind the waterfall or enter around to surpass the waterfall and go around.")


    if Obstacle_one_TT == "waterfall":
        print "You chose to take the risk. As you near the falls, the path is getting muddier. Soon the water is above the ankles and the path is under water. The only way to continue is by becoming soaked. Would you like to keep going?"

    Continue_through_waterfall = raw_input("Are you sure you would like to contunue?")

    if Continue_through_waterfall == "yes":
        print "You have made it to the other side, but hypothermia is slowly setting in. You cannot continue on. Please return home and try again tomorrow. END"
    if Continue_through_waterfall == "no":
        print "You have become damp and cold and lost some time, but you are still able to continue the trek because you were smart and chose to retreat from that path."

    else:
        print "You chose to go around the waterfall. Smart choice because the rest of the crew was sent back from the waterfall or did not make it."





def Obstacle_two_TT():
    this is the second obstacle the user will come across

    print "Next you come to a dead end, the only way out is up. There is a rope and a ladder that lead up. Both look a little timeworn, but the only other route is an hour out of the way.  You can either choose to proceed up or take the long route. "

    Obstacle_two_TT = raw_input("Enter up to proceed up or around to proceed around this obstacle.")

    if Obstacle_two_TT == "up":
        print "It looks a little scary, but you can do it. Be careful."
        print "Oh no your water fell out of your pack as soon as your reached the top and burst about 30 feet below."


    if Obstacle_two_TT == "around":
        print "Turns out you do not have time for this route, you must return to the ladder and rope to get up."


        LOOP BACK TO UP!!!!!!!!!!



def Obstacle_three_TT():
    this is the third obstacle the user will come across

    print "After making it to the top, you are thirsty and need water. What should you do? You check the map. There is a pond right along the path or there is a stream about a mile out of the way. Be careful with the sanitation of the water."
    
    Obstacle_three_TT = raw_input("Would you rather drink from the pond or stream?")

    if Obstacle_three_TT == "pond":
        print "You choose to drink from the pond. After a few sips, your stomach is turning and you are getting dizzy. There was a still water bacterium in the water from sitting. You should have chosen the stream. You have to call in medics and are too weak to reach the top tonight."

        ENDDDDDDDDDDDDDDD. Would you like to start a new game or exit?

    if Obstacle_three_TT == "stream":
        print "You have chosen to drink from the heavy flowing stream. Good idea! Although this is further out of the way, there is less bacteria in water that flows."



def Obstacle_four_TT():
    print "You are nearing the top and the snow is getting thick. There was a fresh snow at the top of the mountain from the night before. The sun is still awake, but lowering in the sky. You have to reach camp before the sun sets. Taking the straight up path is risky due to the snow. Going around may be the safer route."

    Obstacle_four_TT = raw_input("Would you like to go straight up?")

    if Obstacle_four_TT == "yes":
        print "Watch where you are stepping because the snow is thick." 

    if Obstacle_four_TT == "no":
        print "Great choice! I know you are tired, but this is the safest bet. Proceed around the peak with caution."


def Continue_obstacle_four_TT():

    Continue_obstacle_four_TT = raw_input("Are you sure you want to continue?")

    if Continue_obstacle_four_TT == "yes":
        print "Ut oh, your foot slips and you try to throw your ice pick into the snow, but that makes it worse. An avalanche is happening. You got swept away down the mountain and berried."

        ENDDDDDDDDDD

    if Continue_obstacle_four_TT == "no":
        print "Great choice! I know you are tired, but this is the safest bet. Proceed around the peak with caution."




def Obstacle_five_TT():
    print "You can see the glow of the fire in the cabin at the top. Only about a mile left,  when all of a sudden you hear something like a branch breaking behind you. You slowly turn around…There is a 10 foot bear about 20 feet away."

    Obstacle_five_TT = raw_input("Do you want to run, play dead, or fight the bear?")

    if Obstacle_five_TT == "run":
        print "The snow is so thick and the bear is catching up. There’s no way you can outrun the bear. He catched up and attacks. So close, yet so far from the top. Too injured to continue on. You will not make it today."

        ENDDDDDDDDDD

    if Obstacle_five_TT == "play dead":
        print "Playing dead is the best option. The bear is still coming towards you, but you stay down in a ball. He sniffs you and sticks out his paw to pet you, but then walks away. You wait a little until he is gone. Then continue on. Few! That was a close one."

    if Obstacle_five_TT == "fight" or "fight the bear":
        print "You take out your ice pick and slash the bear coming at you. Bad decision. You just made the bear very angry and he fights back and wins. You will not be making it to the top."

        ENDDDDDDDDDD



def Made_it_to_the_top_TT():

    print "It is now dusk and you are cold and scared. You have made it this far, keep it going."
    print "Congradualtions!! Finally you have made it to the top where a warm fire and dinner awaits with companions."






SIMPLY SAFERRRRRRRRR


def Obstacle_one_SS():
    
    print "Start off by heading west past the meadows into the canyon. You come across a sign that says be ware, flash floods ahead. The weather does look a little iffy."    
    
    Obstacle_one_SS = raw_input("would you rather continue ahead ignoring the signs or bypass the canyon going an extra 4 miles out of the way? Enter continue or bypass")

    if Obstacle_one_SS == "continue":
        print "You chose to risk the path of the canyon. The clouds are getting darker and darker. Two miles into the canyon, the skys release. First with the hail, then comes the rain. There is no shelter and no way out. The water gets highter and highter and eventually you are swept up in the strong current. You have lost too much time and are not in healthy enough condition to continue on today."

    if Obstacle_one_SS == "bypass":
        print "Great decision. The path may be a little longer, so you may have to walk a little faster, but this was the smartest choice. "

def Obstacle_two_SS():

    print "After detouring around the canyon and now heading up into the woods, you come across a heavy flowing river. The water only comes up to your waist, but it is rapid and unsteady. You can either try and walk/jump across or build a bridge with wood nearby. "

    Obstacle_two_SS = raw_input("Would you like to walk/jump across or build a bridge?")

    if Obstacle_two_SS == "walk" or "jump" or "walk/jump":
        print "Unfortunately, the river is too wide to jump across, so you step your foot in and first thing you are pulled under by the raging river. Soaked and lost too much time by being pulled a few miles down stream, you have to return home. "

    if Obstacle_two_SS == "build a bridge":
        print "This may take a little longer, but it is the safest bet. There is only enough wood to make a small bridge. Your pack weighs 70 lbs, but both you and your pack probably cant make it."

def Obstacle_two_SS_Cross_Bridge():

        Obstacle_two_SS_Cross_Bridge = raw_input("Enter A to cross the bring only a few things across or enter B to try and throw your pack across the river.")

        if Obstacle_two_SS_Cross_Bridge == "A":
            print "Take only a few things you need. Over half way to the top, you take the bare minimum and make it across."

        if Obstacle_two_SS_Cross_Bridge == "B":
            print "You thought you could make it across, but the bag hits off the edge of the other side of the river and gets taken down stream. Left with nothing. Luckily if you are smart, you can still make it. "

def Obstacle_three_SS():

    print "You are safely across the bridge, but with little to nothing left. You continue walking and realize you grabbed your water, but forgot any sort of food. Your muscles are tired and need to be fueled before moving on. You see a patch of mushrooms and a raspberry bush. You read that the mushrooms were safe, but there was nothing in the book about rasberries. "

        Obstacle_three_SS = raw_input("Even though you hate mushrooms, do you eat the mushrooms or take a risk on the rasbetties?")

        if Obstacle_three_SS == "mushrooms":
            print "Good choice. Better to be safe then sorry. Hold your nose and swallow. We only need a little fuel to reach the top. "

        if Obstacle_three_SS == "rasberries":
            print "Risky choice. These are not actually raspberries. They are a poisonous berry that has required immediate medical attention. You will have to be medivacked out and can no longer continue on this trek. "

            ENDDDDDDDDDDDDDDD

def Obstacle_four_SS():

    print "After more hours of hiking, the sun is setting and you become very tired.  There is a shortcut up the face of this rock that you can free climb or you can go around."

    Obstacle_four_SS = raw_input("Do you want to climb or go around?")

    if Obstacle_four_SS == "climb":
        print "You are too tired and your foot slips and you are no longer able to hold on. You land about 20 feet below and can not move your legs. yOu have to call medical help and get to a hospital right away. "

        ENDDDDDDDDDDDDDDD

    if Obstacle_four_SS == "around" or "go around":
        print " You are tired, but this is the safest bet for you and after seeing the light from the fire in the cabin, you regain a little strength and are able to make it to the top! "


def Made_it_to_the_top_SS():

    print "It is now dusk and you are cold and scared. You have made it this far, keep it going."
    print "Congradualtions!! Finally you have made it to the top where a warm fire and dinner awaits with companions."














def main():
    """Runs the horiscope games"""


    greet_user()

    ask_if_continue()

    accept_the_journey()

    playing = True

    while playing:

        playing = ask_if_continue()

    Obstacle_one_TT()
    Obstacle_two_TT()
    Obstacle_three_TT()
    Obstacle_four_TT()
    Obstacle_five_TT()
    Made_it_to_the_top_TT()



    Obstacle_one_SS()
    Obstacle_two_SS()
    Obstacle_two_SS_Cross_Bridge()
    Obstacle_three_SS()
    Obstacle_four_SS()
    Obstacle_five_SS()
    Made_it_to_the_top_SS()



main()

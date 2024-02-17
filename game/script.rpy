# The script of the game goes in this file.
#python:
 #   userName = renpy.input("What is your discord user? (or name if you're bold like that)")
  #  userName=userName.strip()

   # if not YN:
    #     YN = "neet246"
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define softie_nvl = Character("snugglebunni", kind=nvl, image="softie.png", callback=Discord_Ping)
define edater_nvl = Character("eddi", kind=nvl, image="edater.png", callback=Discord_Ping)
define incel_nvl = Character("D4RK", kind=nvl, image="incel.png", callback=Discord_Ping)

define user_nvl = Character("[username]", kind=nvl, image="user.png", callback=Discord_Ping)
default username = "neet246"

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

define nvl_mode = "phone"

#image variables
image death ="You Died.jpg"
image ban_msg = "ban message.png"
image discord_darkgrey = "#2D2F34"

#SetScreenVariable = renpy.input("What is your name?", "neet246", length=32).strip()

# The game starts here.
label main_menu:
    return

label start:
    window hide
    $ username = renpy.input("What is your discord user? (or name if you're bold like that)")
    $ username = username.strip()

    

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.
    label intro:
    nvl_narrator "You're in your favorite discord server, populated with fellow chronically online (terminally online even) internet dwellers."
    nvl_narrator "Today's a good day. Your messages are getting ~5 reactions each with at least one being a laughing emoji. You Are On Cloud Nine!"
    nvl_narrator "But perhaps you get a little too bold.. and decide to post a meme"
    nvl_narrator "In" with vpunch
    nvl_narrator "General" with vpunch

    user_nvl "{image=hellochat.png}"

    nvl_narrator "You've flown too close to the sun. Now the mods are on you fr."

    softie_nvl "a reminder! please no memes in gen chat!! (>_<)"

    edater_nvl "yah it makes @D4RK sad"

    incel_nvl "This is the third time you have done this @[username]. If you can't follow the simplest of rules, then we're going to have to ban you."

    edater_nvl "uh oh didnt mean to ping the beast lmao"

    scene discord_darkgrey
    with Dissolve (0.6)
    show ban_msg
    with Dissolve (0.6)

    pause(3.5)

    "Uh Oh! Someone just got banned. Send in an appeal to one of the mods?"

    hide ban_msg
    scene black
    with Dissolve (0.25)

    menu meet_the_mods:

        "Plead with one of the mods":
            jump appeal

        "There are other things in life more important than Discord. Go Outside!":
            jump outdoors

    label appeal:
        #maybe add ban appeal here or in a different file
        nvl_narrator "ok"
    return
    
    label outdoors:
        hide ban_msg
        "You turn off your phone and go outside, and let the sun hit your face."
        "Unfortunately, you have a lack of experience in navigating the outside world"
        "BANG!!!" with hpunch
        "You have been hit by a car. Given that you are uninsured and unwilling to call for an ambulance, you die of your injuries."
        show death
        with Dissolve (1.5)
        "choose again :3"

        hide death
        scene black

        jump meet_the_mods 
    # This ends the game.



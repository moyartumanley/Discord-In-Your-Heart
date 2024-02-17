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

    softie_nvl "You've created a new Ren'Py game."

    softie_nvl "Once you add a story, pictures, and music, you can release it to the world!"

    user_nvl "I'm the other kid texting right now.."

    user_nvl "I'm a double texter"

    nvl_narrator "I have no clue how this works tbh"

    # This ends the game.

    return

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define n_nvl = Character("Nighten", kind=nvl, image="nighten", callback=Discord_Ping)
define e_nvl = Character("Eileen", kind=nvl, callback=Discord_Ping)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

define nvl_mode = "phone"


# The game starts here.
label main_menu:
    return

label start:
    window hide
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    e_nvl "You've created a new Ren'Py game."

    e_nvl "Once you add a story, pictures, and music, you can release it to the world!"

    n_nvl "I'm the other kid texting right now.."

    nvl_narrator "I have no clue how this works tbh"

    # This ends the game.

    return

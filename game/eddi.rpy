# eddi dialogue memory
default d_list = []

define nvl_mode = "phone"


# appending to a list
# $ d_list.append("1 one 1")

# access element in list
# user_nvl "[d_list[1]]"

# SCREEN : EDDI_DISCORD SCREEN ================================================
screen EddiDialogue():
    
    style_prefix "phoneFrame"

    frame:
        background "#424549"    
        
    # if d_list not empty, populate the last two messages. 

    # proceed in text 

# LABEL : EDDI_INTRO ================================================
label eddi_intro:
    #call screen EddiDialogue()
    edater_nvl "I gifted u Nitro- sorry about getting kicked out"
    
    user_nvl "..."
    edater_nvl "D4RK did it not me"
    "Your eyes shift to the side, annoyed. These damn mods never want to take ownership over their actions."

    menu:

        "Play dumb":
            # jump appeal
            jump eddi_who

        "Beg to be unbanned":
            jump eddi_pls

    jump outdoors



# LABEL : EDDI_WHO ================================================
label eddi_who:
    user_nvl "who's D4RK..."
    edater_nvl "you don't kno D4RK?"
    edater_nvl "this guy???"
    # TODO: Profile picture!!
    edater_nvl "he literally does all the announcement posts"
    user_nvl "o"

    menu:
        "Beg to be unbanned":
            # jump appeal
            jump eddi_pls

    jump outdoors

# LABEL : EDDI_PLS ================================================
label eddi_pls:
    "Now's the chance. You decide to ask for the unban."
    user_nvl "could u ask them to unban me??"
    nvl_narrator "eddi types for awhile."
    play music "audio/heartbeat.mp3" volume 8.0
    "Your heart begins to beat."
    "..."
    "Is this... love? Anxiety??? Blood rushes to your head and.."
    stop music 
    edater_nvl "i can do it"
    user_nvl "waaaaaa really!??!?1111 " #TODO: insert puppy eye emojis
    edater_nvl "ya but since i gave u nitro, do you think u can do something for me?"
    "You think really hard... you hope it's not a weird favor or request..."


    jump outdoors






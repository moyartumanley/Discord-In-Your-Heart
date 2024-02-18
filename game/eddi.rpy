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

# LABEL : EDDI_PLS ================================================
label eddi_pls:
    "Now's the chance. You decide to ask for the unban."
    user_nvl "could u ask them to unban me??"
    nvl_narrator "eddi types for awhile."
    play music "audio/heartbeat.mp3" volume 8.0 #play sound 
    "Your heart begins to beat."
    "..."
    "Is this... love? Anxiety??? Blood rushes to your head and.."
    stop music 
    edater_nvl "i can do it"
    user_nvl "waaaaaa really!??!?1111 " #TODO: insert puppy eye emojis
    edater_nvl "ya but since i gave u nitro, do you think u can do something for me?"
    user_nvl "?????"
    edater_nvl "can you lend me $20"
    user_nvl "dude wtf"
    edater_nvl "okay... how about now?? " #TODO: add smirking emoji
    edater_nvl "{image=hotdogs.png}"
    edater_nvl "i can send more if u want"
    "You are dumbstruck. All you wanted to be was unbanned and now you're being sent thirst traps..."
    "But you're curious to see more..."

    menu:
        "feed your curiousity":
            jump eddi_curious

        "call it quits":
            jump outdoors

# LABEL : EDDI_CURIOUS ================================================
label eddi_curious:
    user_nvl "yea send more"
    edater_nvl "my cashcapp is @eddi_5"
    user_nvl "fine"

# LABEL : EDDI_CASHAPP ================================================
    label eddi_cashapp:
    nvl_narrator "You send eddi $20"
    edater_nvl "thanks"
    edater_nvl "{image=hotdogs2.png}"
    nvl_narrator "A moment passes and you wait for your account to be unbanned"
    nvl_narrator "Nothing happens."
    user_nvl "dude"
    user_nvl "can u unban me now???"
    edater_nvl "oh sorry i thought the $20 was for another pic"
    nvl_narrator "This isn't going to work. eddi's not interested in unbanning you..."
    nvl_narrator "You need to take it up a notch..."
    # BREAK IN GAME
    jump pick_another_mod

    # menu:
    #     "{image=roblox_choice.png}":
    #         jump eddi_roblox
    #     "{image=legs_choice.png}":
    #         jump eddi_legs
    #     "{image=jollibee_choice.png}":
    #         jump eddi_jolli

# LABEL : EDDI_ROBLOX ================================================
    label eddi_roblox:
        

# LABEL : EDDI_LEGS ================================================
    label eddi_legs:

# LABEL : EDDI_JOLLI ================================================
    label eddi_jolli:
        user_nvl "{image=jollibee.png}"














# eddi dialogue memory
default d_list = []

define nvl_mode = "phone"


# appending to a list
# $ d_list.append("1 one 1")

# access element in list
# user_nvl "[d_list[1]]"

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
    user_nvl "could u unban me??"
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
    # BREAK IN GAME
    jump pick_another_mod


# LABEL : EDDI_PICK ================================================
    label eddi_final:
    "You decide that eddi is your best bet to getting unbanned." 
    "You just need to take it up a notch and get him on your side." 
    "Let's rizz him up!!" 
    "Which picture should we send him?" 

    menu:
        "{image=roblox_choice.png}":
            user_nvl "{image=roblox.png}"
            jump eddi_roblox
        "{image=legs_choice.png}":
            user_nvl "{image=legs.png}"
            jump eddi_legs



# LABEL : EDDI_ROBLOX ================================================
    label eddi_roblox:
    edater_nvl "whats up lol"
    user_nvl "this could be us but you keep playing around :3" #TODO: insert cringe emoji
    nvl_narrator "You cringe at yourself."
    nvl_narrator "But it's all in a good day's work."
    user_nvl "mmm if you're trying to suck up to me, it's not gonna werk"

    "Oops. Looks like you suck."
    "You're not too good at this romance stuff, are you?"
    return 

        

# LABEL : EDDI_LEGS ================================================
    label eddi_legs:
        edater_nvl "what the lol"
        user_nvl ":3 do u like the legs?"
        user_nvl "they reminded me of the picture u sent~"
        edater_nvl "LMAOOOOOOOOOO those were just hotdogs"
        user_nvl "omg ur so funny"
        user_nvl "..."
        user_nvl "you know, i really liked talkign to u" #TODO: Insert cute emoji
        user_nvl "but now that i'm not in the server,,,.. its been really lonely"
        user_nvl "ive missed u"
        nvl_narrator "eddi is typing"
        nvl_narrator "You feel your heart beat faster and faster"
        play music "audio/heartbeat.mp3" volume 8.0
        nvl_narrator "do you perhaps have a heart condition...?"
        edater_nvl "me too :)"
        stop music 
        nvl_narrator "it seems to have worked!!!!"
        user_nvl "... do you perhaps want to be my bf"
        #TODO: lame proposal picture
        edater_nvl "omg... yes babeeeee"
        edater_nvl "could you lend me $20"
        "Yeah- this relationship was never meant to be"
        "Nor was your existence in the server"

        return














#chat variables
default edater_talk = False
default incel_talk = False
default softie_talk = False

screen appeal_screen():
    frame: 
        background "#554509" 
        text "WHAOOIF"
        xfill False
        yfill False

label appeal:
    #maybe add ban appeal here or in a different file
    show screen chat_bubbles()
    nvl clear
    "You groan in frustration."
    "You're going to have to suck up to these mods if you wanna get unbanned..."

    menu:
        "The question is... which mod?"

        "snugglebunny" if softie_talk == False:
            $ softie_talk = True
            jump sb_intro
        "D4RK" if incel_talk == False:
            $ incel_talk = True
            jump D4RK_intro
        "eddi" if edater_talk == False:
            $ edater_talk = True
            jump eddi_intro
            
            
        # "{image=icon_action.png} D4RK    ":
        #     jump appeal
        # "{image=icon_action.png} eddi    ":
        #     jump appeal

        # "{image=icon_action.png} snugglebunny":
        #     jump appeal
    return


label pick_another_mod: 
    nvl clear
    nvl_narrator "The conversation is going nowhere... You decide to appeal to another mod."

    menu:
        "snugglebunny" if softie_talk == False:
            $ softie_talk = True
            jump sb_intro
        "D4RK" if incel_talk == False:
            $ incel_talk = True
            jump D4RK_intro
        "eddi" if edater_talk == False:
            $ edater_talk = True
            jump eddi_intro

    
#chat variables
default edater_talk = False
default incel_talk = False
default softie_talk = False


label appeal:
    #maybe add ban appeal here or in a different file
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
    nvl clear

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
        
        #rizz label 
        "You've exhausted your options." if softie_talk and incel_talk and edater_talk:
            "It seems like these moderators will need more than convincing..."
            "Good thing love is an easy manipulating tool."
            jump final_pick

label final_pick:
    nvl clear
    "Pick one mod to rizz up:"
    menu:
        "snugglebunny":
            $ softie_talk = True
            jump sb_rizz
        "D4RK":
            $ incel_talk = True
            jump lock_in_D4RK
        "eddi":
            $ edater_talk = True
            jump eddi_final

    
        

    
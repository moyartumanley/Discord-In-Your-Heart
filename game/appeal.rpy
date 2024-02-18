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

        "test":
            jump test_intro

        "snugglebunny":
            jump sb_intro
        "D4RK":
            jump D4RK_intro
        "eddi":
            jump eddi_intro
            
            
        # "{image=icon_action.png} D4RK    ":
        #     jump appeal
        # "{image=icon_action.png} eddi    ":
        #     jump appeal

        # "{image=icon_action.png} snugglebunny":
        #     jump appeal
    return
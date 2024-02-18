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
    user_nvl "who's dark..."

    jump outdoors

# LABEL : EDDI_PLS ================================================
label eddi_pls:
    user_nvl "could u please unban me??"
    jump outdoors






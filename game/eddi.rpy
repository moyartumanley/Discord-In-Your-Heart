# eddi dialogue memory
default d_list = []


# appending to a list
# $ d_list.append("1 one 1")

# access element in list
# user_nvl "[d_list[1]]"

# LABEL : EDDI_INTRO ================================================
label eddi_intro:
    edater_nvl "I gifted u Nitro- sorry about getting kicked out"
    
    user_nvl "..."
    edater_nvl "D4RK did it not me"
    "Your eyes shift to the side, annoyed. These damn mods never want to take ownership over their actions."

    menu:

        "Plead with one of the mods":
            # jump appeal
            jump eddi_intro

        "There are other things in life more important than Discord. Go Outside!":
            jump ending

    jump ending


# LABEL : EDDI_WHO ================================================
label eddi_who:

    jump ending

# LABEL : EDDI_PLS ================================================
label eddi_pls:
    jump ending

# SCREEN : EDDI_DISCORD SCREEN ================================================
screen eddi_screen():
    zorder 100
    
    # if d_list not empty, populate the last two messages. 

    # proceed in text 





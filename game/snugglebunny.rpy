# snugglebunny dialogue memory
# default d_list = []

define nvl_mode = "phone"

image discord_darkgrey = "#2D2F34"
image blocked_msg = "blocked.png"

# appending to a list
# $ d_list.append("1 one 1")

# access element in list
# user_nvl "[d_list[1]]"

# SCREEN : EDDI_DISCORD SCREEN ================================================
screen SbDialogue():
    
    style_prefix "phoneFrame"

    frame:
        background "#424549"    
        
    # if d_list not empty, populate the last two messages. 

    # proceed in text 

# LABEL : EDDI_INTRO ================================================
label sb_intro:
    #call screen SunnyglebunnyDialogue()
    softie_nvl "omg im so sry u got banned :( u didnt deserve it <3"

    nvl_narrator "You know snugglebunny would be the easiest mod to convince to get you unbanned because he is a self-proclaimed 'empath.'"
    nvl_narrator "Easy peasy you think. I just need to put up an innocent act and rizz them up and this will all be over in no time."
    nvl_narrator "But the thought of doing that is already making you gag on the inside."
    nvl_narrator "What will you message him? Do you cut right to the chase or put on an act?"

    menu:
        "for real, can u unban me tho??":
            jump sb_unban

        "thank u snuggles!! i just lost control :(":
            jump sb_act


# LABEL : SB_UNBAN ================================================
label sb_unban:
    user_nvl "for real, do you think u unban me??"

    softie_nvl "i dont know abt that… the other mods are v mad"

    user_nvl "dude come on" 
    user_nvl "just put in a word for me"

    softie_nvl "i can try but no guarentees"

    nvl_narrator "At least, they're trying you think. But your patience is low. Your already missing out on all the memories the rest of them are making on the server."

    user_nvl "any updates??"

    softie_nvl "no yet but ill let yk asap ~"

    nvl_narrator "Ten minutes has passed. You're aggitated. You're raking your hands through your hair. You know these mods check discord every chance they get."
    nvl_narrator "If there's no response now, it's unlikely there'll be more."

    user_nvl "have they said anything yet?"

    nvl_narrator "No response. Maybe you should talk to someone else?"

    nvl_narrator "You think, am I really about to double text this man right now."

    user_nvl "??"
    user_nvl "i know yall spend every minute of the day on this app"

    softie_nvl "omg chill"
    softie_nvl "ur scaring me :/"
    softie_nvl "the other mods don't think you should be unbanned"

    nvl_narrator "Maybe snugglebunny wasn't the right person afterall. Maybe you should try to rizz up the other mods."

    jump pick_another_mod


# LABEL : SB_ACT ================================================
label sb_act:
    user_nvl "thank u snuggles!! i just lost control :("
    
    softie_nvl "pls dont apologize >.<"
    softie_nvl "theyre way too harsh"

    nvl_narrator "It's working. Do you pile on more compliments or cut to the chase?"

    menu: 
        "youre literally the only mod that actually care about us.":
            jump sb_cute
        "for real, can u unban me tho??":
            jump sb_unban

# LABEL : SB_CUTE ================================================
label sb_cute:
    user_nvl "youre literally the only mod that actually care about us."
    user_nvl "i appreciate you man"

    softie_nvl "awww"
    softie_nvl "*blushes*"
    softie_nvl "let me talk to the other mods and see if u can be unbanned"

    nvl_narrator "You plan is working. You didn't even need to ask to get unbanned. Flattery was enough for snugglebunny to do the hard work for you."
    nvl_narrator "But maybe snugglebunny won't be enough. "

    jump pick_another_mod

# LABEL : SB_RIZZ ================================================
label sb_rizz:
    user_nvl "thank u so much for talking to them for me, you don't have to do all that"

    softie_nvl "no this is unfair"
    softie_nvl "i will fight for whats right"

    nvl_narrator "You start to wonder why he even cares so much."

    user_nvl "Ok if you insist"
    user_nvl "You know what I'm starting to think you're actually an empath"

    softie_nvl "haha >.<"
    softie_nvl "what do u mean actually"

    user_nvl "I mean that you actually act like this irl"

    softie_nvl "of course i do!"

    nvl_narrator "You begin to put down your guard."
    nvl_narrator "Maybe snugglebunny is actually a nice guy afterall."
    nvl_narrator "Snugglebunny and you get really close you guys end up bonding and you forget about your plan in the first place"
    nvl_narrator "They're actually kinda sweet. You begin to see them as more than friends." 
    nvl_narrator "You open up to snugglebunny about your struggles in life and that was what caused you to break the rules in the server in the first place."

    play sound "audio/heartbeat.mp3" volume 8.0

    user_nvl "Hey, I've been meaning to tell you something..."

    softie_nvl "what is it?"
    softie_nvl "wait!"
    softie_nvl "i have smt to tell u"
    softie_nvl "im in love with you"

    play sound "audio/heartbeat.mp3" volume 8.0

    nvl_narrator "You can't believe it. He confessed to you before you."

    user_nvl "I can't belive it."
    user_uvl "im in love with you too"

    nvl_narrator "You guys become a 'thing'. You love him and vice versa. Getting banned from that server was the best thing that has EVER happened to you."
    nvl_narrator "But somethings not quite right."

    user_nvl "Hey, you haven’t been answering recently. where have you been??"

    softie_nvl "sry ive been rlly busy"

    nvl_narrator "You’re unconvinced and you keep pushing."
    
    user_nvl "tell me what’s going on! this isn’t like you!"

    softie_nvl "ok i confess. i havent been truthful. i actually have a wife and kids"

    nvl_narrator "What the actual f-"
    nvl_narrator "This past few days have all been a lie."
    nvl_narrator "Your ears start ringing and you can feel the tears welling up in your eyes."

    user_nvl "what?? you’re telling me now."
    user_nvl "how could you"
    user_nvl "i trusted you"

    softie_nvl "I’m so sorry."
    softie_nvl "I never meant to hurt you..."
    softie_nvl "We just got along so well. I didn't want to let you go."
    softie_nvl "Please give me time. I'll fix this!"

    nvl_narrator "You think Snugglebunny is sincere because he never uses capital letters, but he did this time."

    softie_nvl "i will leave my wife. i swear. just give me time."

    nvl_narrator "You're at crossroads. You don't know if you should believe him or not. Do you want to talk to someone else?"

    user_nvl "ive thought about it for a long time. ill give you sometime to figure it out with your wife and stuff"
    user_nvl "you're the best thing that has happened to me and i want you in my life"
    user_nvl "i was also thinking"

    nvl_narrator "You are ready to ask the question to snugglebunny. You are going to ask to meet him in real life."
    nvl_narrator "Then right as you're about to ask him. Something happens."

    hide screen chat_bubbles
    scene discord_darkgrey
    with Dissolve (0.6)
    show blocked_msg
    with Dissolve (0.6)

    pause(3.5)

    hide blocked_msg
    scene black
    with Dissolve (0.25)

    "Snugglebunny has blocked you. You feel feelings that you've never felt before. You're so betrayed by this. You rage."
    "You begin smashing your laptop until the screen smashes and you are left with nothing but a broken laptop and heart."





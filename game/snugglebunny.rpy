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
    softie_nvl "omg im so sry u got banned :( u didnt deserve it"

    nvl_narrator "You know snugglebunny would be the easiest mod to convince to get you unbanned because he is a self-proclaimed 'empath.'"
    nvl_narrator "Easy peasy you think. I just need to put up an innocent act and rizz them up and this will all be over in no time."
    nvl_narrator "But the thought of doing that is already making you gag on the inside."
    nvl_narrator "Do you cut right to the chase or put on an act?"

    menu:
        "For real, can u unban me tho??":
            jump sb_unban

        "Thank you, snuggle!! I just lost control :(":
            jump sb_act


# LABEL : SB_UNBAN ================================================
label sb_unban:
    user_nvl "For real, can u unban me tho??"

    softie_nvl "i dont know abt that… the other mods are v mad"

    user_nvl "Come on, man. just put in a word for me"

    softie_nvl "i can try but no guarentees"

    nvl_narrator "At least, they're trying you think. But your patience is low. Your already missing out on all the memories the rest of them are making."

    user_nvl "any updates??"

    softie_nvl "no yet but ill let yk asap"

    nvl_narrator "Ten minutes has passed. You're aggitated. You know these mods check discord every chance they get."
    nvl_narrator "If there's no response now, it's unlikely there'll be more."

    user_nvl "any updates?"

    nvl_narrator "No response."
    nvl_narrator "You think, am I about to double text this man right now."

    user_nvl "??"
    user_nvl "oh come on. I know yall spend every minute of the day on this app"

    softie_nvl "omg chill"
    softie_nvl "the other mods don't think you should be unbanned"

    user_nvl "I knew it. You were useless from the start."
    user_nvl "You know what you are?"
    user_nvl "U"
    user_nvl "ARE"
    user_nvl "A"
    
    nvl_narrator "You are ready to unlease all your pent up rage on snugglebunny. You will tell them how they are a pushover and that's how they became a mod in the first place."
    nvl_narrator "The other mods just wanted to use them. They're pathetic and don't deserve to be a mod."

    hide screen chat_bubbles
    scene discord_darkgrey
    with Dissolve (0.6)
    show blocked_msg
    with Dissolve (0.6)

    pause(3.5)

    hide blocked_msg
    scene black
    with Dissolve (0.25)

    "Snugglebunny out of all the mods have decided to block you. Maybe you have actually gone too far this time."
    "You feel kinda bad. Today has been too long. Maybe you should log off and go touch grass."
    
    jump outdoors

# LABEL : SB_ACT ================================================
label sb_act:
    user_nvl "Thank you, snuggle!! I just lost control :("
    
    softie_nvl "pls dont apologize"
    softie_nvl "theyre way too harsh"

    user_nvl "You're literally the only mod that actually care about us."
    user_nvl "I appreciate you."

    softie_nvl "awww"
    softie_nvl "*blushes*"
    softie_nvl "let me talk to the other mods and see if u can be unbanned"

    nvl_narrator "You plan is working. You didn't even need to ask to get unbanned. Flattery was enough for snugglebunny to do the hard work for you."
    nvl_narrator "But just a little more you think."

    user_nvl "No it's ok, I don't want you to get on their bad side too."

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

    user_nvl "Me too!"

    nvl_narrator "You guys become boyfriend and boyfriend. You love him and vice versa. Getting banned from that server was the best thing that has EVER happened to you."
    nvl_narrator "But somethings not quite right."

    user_nvl "Hey, you haven’t been answering recently. Where have you been??"

    softie_nvl "sry ive been rlly busy"

    nvl_narrator "You’re unconvinced and you keep pushing."
    
    user_nvl "Tell me what’s going on. This isn’t like you."

    softie_nvl "ok i confess. i havent been truthful. i actually have a wife and kids"

    nvl_narrator "What the actual f-"
    nvl_narrator "This past few days have all been a lie."
    nvl_narrator "Your ears start ringing and you can feel the tears welling up in your eyes."

    user_nvl "What?? You’re telling me now."
    user_nvl "How could you"
    user_nvl "I trusted you"

    softie_nvl "I’m so sorry."
    softie_nvl "I never meant to hurt you..."
    softie_nvl "We just got along so well. I didn't want to let you go."
    softie_nvl "Please give me time. I'll fix this!"

    nvl_narrator "You think Snugglebunny is sincere because he never uses capital letters, but he did this time."

    softie_nvl "i will leave my wife. i swear. just give me time."

    jump outdoors






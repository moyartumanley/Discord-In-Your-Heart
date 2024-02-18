#continue from here
label D4RK_cont:
   user_nvl "alright,,, give me an example of how ur nice to women"

   nvl_narrator "You watch typing bubbles appear, disappear, and then reappear on screen. D4RK seems to be thinking long and hard about this."

   incel_nvl """
   Well… I always make sure to hold open doors for females anytime I’m outside— 
   
   and I always compliment their clothes and makeup. 
   
   It’s not every guy who’s willing to treat women like queens, but that doesn't seem to faze women at all–
   """
   nvl_narrator "D4RK continues to rant"

   user_nvl "OKAY!" with vpunch

   nvl_narrator "You attempt to stop his rant. What advice will you provide?"

   menu advice:
      "Stop blaming others and look towards self-improvement!":
         jump self_improvement
      "Give into his delusions.":
         jump delusions

label self_improvement:
   user_nvl "stop focusing on women… and whatever the fuck “chads” are. quit trying to change other people! focus on changing urself!"

   incel_nvl """
   Like looksmaxxing? 
   
   I’ve seen mentions of that in the forums, and I’ve tried mewing. 
   
   However, the concept of bonesmashing scares me.
   
   But, I am willing to sacrifice it all for the pursuit of love–
   """
   user_nvl "what the fuck is mewing. why are u meowing at women? what the hell is bonesmashing–"

   incel_nvl "{i}Sigh.{/i} Normies like you wouldn’t understand."

   user_nvl """
   just looked it up. 
   
   what the fuck dude. 
   
   u dont have to take a hammer to your face to improve yourself! 
   
   ur fixable! 
   
   i can fix u! 
   
   trust!"""

   nvl_narrator "Once again, D4RK types and then stops typing, and then types again, and then stops." 
   
   nvl_narrator "You sit in anticipation, waiting for his repsonse. After two minutes of this, you’re greeted with an image."

   incel_nvl "{image=blushing-anime-girl.png}"

   nvl_narrator """
   You smile a bit. 
   
   Not a real big smile with teeth. 
   
   More like a small friendly grimmace. 
   
   Kind of like when a child gives their parent and or guardian macaroni art.
   
   Realistically, I personally wouldn't want the macaroni art. I just don't think it would suit the decor of a home. 
   
   But you can't tell a small child that their macaroni art ruins your dream of having the  perfect midcentury modern kitchen with warm colors and a cozy vibe, so you begrudgingly accept it anyway.
   """

   incel_nvl "I've- uh- always wanted someone to, uhm- 'fix me'."

   nvl_narrator "Given the fact that D4RK is stuttering over text, looks like your getting somewhere! What do you want to do next?"

   menu rizzler:
      "maybe we can seek self-improvement together!":
         jump bonding
      "bro why are you stuttering over text. this isnt warrior cats rp. you will scare women away with this behavior":
         jump insane_fumbling

#Bad Ending 2
label delusions:
   user_nvl "omg so true king, i too hate women"

   incel_nvl "What do you mean hate women? Have you not been reading my messages? I open the door for them and give them compliments. Sometimes I Tier 5 Twitch sub female twitch streamers I enjoy as well. I don't even get {b}that{/b} mad when they don't read my donos." with hpunch

   incel_nvl "I'm fucking 10k in debt to these female twitch streamers and you're telling me {b}I{/b} hate women?" with hpunch

   incel_nvl"""
   God! Why did I even bother asking for your help!
   
   You're clearly a CIA operative pretending to have intrest in me in order to gain access and investigate my server."""

   nvl_narrator"{i}D4RK blocks you{/i}"

   "What the fuck is in that server for the CIA to investigate?" with hpunch

   "Anyways! Your attempt to get back into the server with D4RK's help has failed. He's probably ranting about you to the other mods too, so GG. Maybe give better advice?"

   pause(3)

   jump advice

#Bad Ending 3
label insane_fumbling:
    nvl_narrator """
    D4RK takes this to heart. 
    
    Deeply. 
    
    He broke his mostly gramatically correct demeanor and revealed his flustered kawaii dokidoki anime girl heart to you. 
    
    In turn, you have essentially told him that this sort of behavior will scare people away.
    
    Why would you do this [username]?"""

    incel_nvl """Ah. I see. I apologize for my behavior [username]. This will never happen again.

    I feel that I may have been overstepping my boundaries as your former moderator.

    Thank you for your advice, I may watch Andrew Tate for further advice on how to be a real man.

    Goodbye [username].
    """

    nvl_narrator "Horrible. You drove the man to seek advice from a bald misogynist living in Romania."

    nvl_narrator """
    How do you even fumble that bad?"
    
    Choose a better answer next time."""

    jump rizzler

#Bonding
label bonding:
    user_nvl "yeah dude! i feel like ur maybe a nice person once u look over those self-confidence issues"

    incel_nvl "Ah... no one's ever told me that before."

    incel_nvl "{image=blushing-anime-girl2.jpg}"

    incel_nvl "Uhm.. d-do you want to see me play League of Legends? Or- uhm, if you want.. we could play Overwatch together?"

    nvl_narrator "Horrible videogame selection. Anyways pick a game."

    menu videogame:
      "League of Legends (HORRIBLE)":
         jump league
      "Overwatch 2 Post Season 9 DPS Rework (GENUINELY AWFUL BUT LESS AWFUL THAN LEAGUE)":
         jump overwatch

label league:
    user_nvl "im down to watch some league :3"

    nvl_narrator "What is wrong with you."

    incel_nvl "{image=blushing-anime-girl.png}"

    incel_nvl "S-streaming now."

    nvl_narrator """
    You tune into his DM stream. He queues comp and within 5 minutes begins screaming into his mic.

    You have no clue what is going on. What is a mid-laner? Why does this game actually look like Ants Fighting Over A Dorito Simulator?

    Anyways, D4RK loses the match and loses 15 LP.
    """
    "I FUCKING HATE THIS GAME!!!!" with hpunch
    "Out of sheer rage, he breaks his computer"
    "{i}Happiest League player by the way.{/i}"
    
    "Anyways, given that his PC is now broken, I guess you aren't getting unbanned now. Pick a different game next time."

    jump videogame

label overwatch:
    nvl_narrator """Unfortunately, you already have Overwatch installed. And you have 300 hours on Mercy, level 5 endorsement, and the 2018 Pink Mercy Skin equipped. 
    
    I Know What You Are."""

    user_nvl "lets play overwatch! im plat in support so i can pocket u~"

    incel_nvl "S-sure. Here's my Blizzard user."

    nvl_narrator """
    Unsuprisingly, given your skin choice and endorsement level, you yellow beam all game. 
    
    Actual 5 percent blue beam in a 12 minute game. 
    
    Thats less than a minute of damage boosting man. It may work in the current meta, but that is genuinely not sustainable.

    And your team voices that in teamchat.
    
    """

    user_nvl "aaa i didnt expect the team to get that mad... like im literally healing them tho? like i have most heals in the game?"

    nvl_narrator "You're under utilizing your kit."

    incel_nvl "Don't listen to them!" with hpunch
    
    incel_nvl "Besides you're rezzes were on point. What's your DPI?"

    user_nvl "3000 :3"

    nvl_narrator "I hate 2018 pink skin mercys."

    incel_nvl "That's so high, LMAO."

    nvl_narrator "Too high."

    incel_nvl """
    Hey [username]... this.. was fun.
    
    Uhm- I really enjoy messaging you!

    A-and I like the way you type!-

    Although this is meant to be a BL, your usage of "u" and "ur" is very feminine and cute!
    """
    user_nvl "uh. thanks man"

    incel_nvl """
    W-would you like to be my discord kitten? 
    
    I-I can reverse your ban and give you special server perms and we can meet up IRL and maybe play Valorant together! 
    
    And I can gift you nitro once I settle my 10k debt! 
    
    Um- I'll try and take care of you, I guess.

    {image=blushing-anime-girl3.jpg}
    """

    nvl_narrator "Make your choice 2018 Pink Mercy Skin User."

    menu final_choice:
        "Become D4RK's discord kitten.":
            jump kitten

        "Politely decline":
            jump friendship

label kitten:
    user_nvl "sure! :33"

    incel_nvl "{image=blushing-anime-girl.png}"

    nvl_narrator "You become D4RK's kitten. Sometimes he asks you to wear maid outfits and get on vc but he's improving as a person and I guess that's all that matters in the end. "

    "You have successfully been unbanned and found love along the way! Congratulations!"

    return main_menu

label friendship:
    user_nvl "sorry... i dont think the kitten life is for me"

    incel_nvl "Ah. I see..."

    user_nvl "but im always down to queue whenever! >:3"

    incel_nvl "Y-yeah! Lets play again together sometime! Let me unban you from the server as well, it's easier to vc in there."

    nvl_narrator "You become gaming buddies with D4RK. Sometimes he rages and breaks his keyboard but I think he's improving as a person and I guess that's all that matters in the end. "

    "You have successfully been unbanned and found friendship along the way! Congratulations!"

    return main_menu

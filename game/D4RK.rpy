label D4RK_intro:
   incel_nvl "You should have followed the rules, man. {b}WE WARNED YOU 3 TIMES.{/b}"
   user_nvl "is it a crime to post gifs in gen? i was just having fun dude…"
   incel_nvl "You dare speak to me after not following the rules I laid out so explicitly? Well, newsflash bud, you can beg and cry and complain all you want… but that isn’t going to get you back into {b}my{/b} server."

   nvl_narrator "You remember all the fun times you had in that server, the people you met, the funny pinned messages, the server stickers… the gifs that eventually led to you getting banned. You can’t give that up!"

   user_nvl "wait!!!!!" with hpunch
   user_nvl "alright..."
   user_nvl "how can I fix this"

   nvl_narrator "You watch the typing notification pop up in the DM window, then stop, then continue… and then stop again. And then continue. And then stop-"

   user_nvl "for gods sake man, just press enter already"
   incel_nvl "Well.. I suppose I could consider letter you back in– IF! you help me on my girlfriend quest!"
   nvl_narrator "You stare at your screen in disgust and wonder what went wrong in your life to get you to this point."

   menu quest_helper:
      "Help the man on his “girlfriend quest”...":
         jump gf_quest
      "No discord server is worth this… go outside and touch grass":
         jump D4RK_outside
      "Talk to a different mod "if softie_talk == False or edater_talk == False:
         jump pick_another_mod


label gf_quest: #rizz label
   user_nvl "what the fuck is a girlfriend quest"
   incel_nvl "Hark former serverling! Listen to my plight!"

   nvl_narrator "D4RK proceeds to painstakingly type his entire life’s story."

   incel_nvl """
   From a young age, I’ve been a nice guy. Nothing but courteous to women. 

   But you see, [username], women are attracted to bad boys. 

   I’m too respectful and courteous towards females– that’s why they’ll never go out with me. 

   However, as I approach 21 years of age, I long to feel the touch of a woman. 

   Something needs to change @[username]!

   Thus I must embark on a quest to find a girlfriend… possibly even a wife! 
   """

   nvl_narrator "You cringe."

   incel_nvl "…Preferably someone submissive and willing to tend to my needs."

   nvl_narrator "You cringe even more."

   user_nvl """
   ok.
   
   yeah. 
   
   sure man. 
   
   ill help u with ur quest."""

   jump D4RK_cont


#Bad Ending 1
label D4RK_outside:

   user_nvl """
   Brother that shit sounds cringe as hell, im not gonna lie. 
   
   I’m out.
   """
   nvl_narrator "You block D4RK and accept that the memories you’ve made on that server are gone forever."

   # jumpstatement
   jump outdoors


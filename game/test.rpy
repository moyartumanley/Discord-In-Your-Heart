define test_nvl = Character("test", kind=nvl, image="pfps/softie.jpg", callback=Discord_Ping)

default intro_0 = Node("You're in the testing stage now", test_nvl)
default intro_1 = Node("I'll do another bubble", test_nvl)
default intro_1a = Node("this is left branch", test_nvl) #left branch
default intro_1b = Node("this is the option that is the right branch", test_nvl) #right branch
default intro_2a = Node("Can i print??", test_nvl)

default all_messages = ["You're in the testing stage now", "I'll do another bubble", "and test this", "this is the message you should see when you return"]
default last_message = Node("old message", test_nvl)
# default current_message = Node(all_messages[0], test_nvl)
default current_message = intro_0
            
label test_resume:
    # $ intro_0.insert(intro_1) # put intro_1 at the left branch
    # $ intro_1.insert(intro_1a) # intro_1a should be left branch
    # $ intro_1.insert(intro_1b) # intro_1b should be right branch

    nvl clear
    $ resume()

label test_intro: 
    # $ intro_0.insert(intro_1) # put intro_1 at the left branch
    # $ intro_1.insert(intro_1a) # intro_1a should be left branch
    # $ intro_1.insert(intro_1b) # intro_1b should be right branch

    "DOES THIS STILL WORK?? :()"
    # $ intro_0.insert(intro_1) # put intro_1 at the left branch
    "LEFT: [intro_0.left]"
    "LEFT message: [intro_0.left.message]"
    "LEFT character: [intro_0.left.character]"
    "RIGHT:[intro_0.right]"


init python:
    
    def make_tree():
        global intro_0, intro_1, intro_1a, intro_1b
        
        intro_0.insert(intro_1) # put intro_1 at the left branch
        intro_1.insert(intro_1a) # intro_1a should be left branch
        intro_1.insert(intro_1b) # intro_1b should be right branch
        intro_1a.insert(intro_2a) 
        # renpy.say(intro_1.left.character, "Intro 1's left branch")
        # renpy.say(intro_1.left.character, intro_1.left.message)

        # renpy.say(intro_1.left.character, "Intro 1's right branch")
        # renpy.say(intro_1.left.character, intro_1.right.message)

    def speak(node):
        global current_message, last_message
        new_node = Node("EMPTY", test_nvl)
  
        while (current_message.left):
            renpy.say(nvl_narrator, "IN THIS WHILE LOOP")
            renpy.say(current_message.character, current_message.message)
            #last_message.append(all_messages[index])
            last_message = current_message
            current_message = current_message.left
            # new_node = current_message.left
            # current_message = new_node
            # renpy.say(current_message.character, current_message.left)
            # if (not current_message.isMenu()):
            #     current_message = current_message.left
        renpy.say(nvl_narrator, "OUTSIDE LOOP")
        renpy.say(current_message.character, current_message.message)
        if (current_message.left):  
            renpy.say(current_message.left.character, current_message.left.message)
        else:
            renpy.say(test_nvl, "DOESN'T EXIST ODDLY")

    def generate_old_message(character, node):
        message = node.message
        message += "{nw}"
        renpy.say(node.character, message)

    def resume():
        # if last_message.message == "empty":
        #     renpy.jump('test_intro')
        # else:
            make_tree()
            generate_old_message(test_nvl, last_message)
            speak(current_message)
            

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define config.layers = [ 'master', 'transient', 'screens', 'overlay' ]
define e = Character("Matthew")
define main = Character("New Student")
define diss = Dissolve(1.0)
define ambi = Character("Random Voice")
define bl = Character("Mr. Blankenship")
# The game starts here.

label start:
    play music "Maid with the Flaxen Hair.mp3"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.

    main "{cps=30}It's a warm summer day{/cps}, {cps=30}my first day at Allen High School.{/cps}"
    main "{cps=30}I'm nervous about this place, I've heard some weird rumors surrounding the school.{/cps}"
    scene bg front
    with diss
    main "{cps=30}So where do I go now?{/cps}"
    ambi "{cps=30}Oh, you must be the new student.{/cps}"
    main "{cps=30}Ah, yes that's me.{/cps}"
    show blanky:
        xalign 0.5
        yalign 3.5
    bl "{cps=30}I'm the principal Joshua Blankenship. But you can call me Josh.{/cps}"
    bl "{cps=30}What's your name bud?{/cps}"
    python:
        name = renpy.input("Pick a name")
        name = name.strip()
        main = Character("[name]")
    main "{cps=30}I'm [name] sir.{/cps}"
    bl "{cps=30}Nice to meet ya, [name], but try not to call me sir{/cps}"
    main "{cps=30}Oh sorry sir.{/cps}"
    bl "{cps=10}...{/cps}"
    bl "{cps=30}Anyway, you should be on your way to first period, I would also implore you to check out some of the clubs after school.{/cps}"
    main "{cps=30}Alright then, thanks for your help Mr. Blankenship{/cps}"
        # School bell here?
    scene bg classroom
    with diss
    main "Sigh..."
    main "New school, still boring I guess..."
    main "Well may as well look at some clubs."
    scene hall1
    with diss
    main "Man all these clubs don't feel right to me..."
    ambi "Hey bro!"
    ambi "Wait up [name]!"
    main "?"
    show justin
    jus "Hey I'm Justin from your first period class!"
    jus "I see your looking for a club to join, right?"
    main "I mean, I guess so..."
    jus "Well you should join my club, Boy's Club!"
    main "Boy's Club? Sounds pretty sus to me..."
    jus "Nah it's not like that... well most of the time."
    jus "Anyway, it's really just a bunch of friends that hang out and stuff"
    jus "Come with me, we're meeting right now!"
    main "Well whatever..."
    scene boysclub1
    with diss
    jus "Well here we are! Go ahead and talk to everyone."
    cho "Pick a character to learn about."
    menu:
        "Matthew":
            jump choice1_mat
        "Jack":
            jump choice1_jac
    label choice1_mat:
        show matthew smile
        cho "Matthew is a strange man. He loves 9/11 conspiracies, jazz, and being annoying as possible"

    label choice1_jac:
        show jacky
        cho "Jack is a MASTER CODER. He loves getting reddit upvotes and steamed ham memes"
    label choice1_done:






        # ... the game continues here.
    # This ends the game.

    return

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






        # ... the game continues here.
    # This ends the game.

    return

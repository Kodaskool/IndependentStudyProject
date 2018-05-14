# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

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
    main "I'm nervous about this place, I have heard some weird rumors about this place"
    scene bg front
    with diss
    main "So where do I go now?"
    ambi "Oh, you must be the new student right?"
    main "Ah, yes that's me."
    show blanky
    bl "Hey, I'm the principal Mr. Joshua Blankenship, but my friends call me Josh."
    bl "What's your name bud?"
    python:
        name = renpy.input("Pick a name")
        name = name.strip()
        main = Character("[name]")
    main "My name is [name] sir."
    bl "Nice to meet ya, [name], but DON'T CALL ME SIR!"
    main "Oh sorry sir."
    bl "..."
    bl "Well, either way your in Class 1, and also I would implore you to check out clubs after school."
    main " Alright then, thanks for your help Mr. Blankenship"






        # ... the game continues here.

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

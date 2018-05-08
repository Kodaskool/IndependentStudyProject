# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Matthew")


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

    show matthew smile

    # These display lines of dialogue.

    e "Wanna buy a ticket?"
    menu:

        "Sure I guess...":
            jump choice1_yes

        "No I'm good":
            jump choice1_no

    label choice1_yes:

        $ menu_flag = True

        e "$5 then buddy"

        jump choice1_done

    label choice1_no:

        $ menu_flag = False

        e "Are you sure, it's only 5 dollars AND comes with free dessert?"

        jump choice1_done

    label choice1_done:

        # ... the game continues here.

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

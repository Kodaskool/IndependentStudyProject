# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image blanky = "blanky.png"
image matthewsmile = "matthewsmile.jpg"
image greta = "greta.png"
image jackie = "jackie.png"
image robert = "robert.jpg"
image justin = "justin.png"
define main = Character("New Student")
define diss = Dissolve(1.0)
define ambi = Character("Random Voice")
define bl = Character("Mr. Blankenship")
define zach = Character ("Zach")
define jus = Character("Justin")
define mat = Character("Matthew")



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
        yalign 0.1
    bl "{cps=30}I'm the principal Joshua Blankenship. But you can call me Josh.{/cps}"
    bl "{cps=30}What's your name bud?{/cps}"
    python:
        name = renpy.input("Pick a name")
        name = name.strip()
        main = Character("[name]")
    main "{cps=30}I'm [name] sir.{/cps}"
    bl "{cps=30}Nice to meet ya, [name], but try not to call me sir{/cps}"
    main "{cps=30}Oh sorry sir.{/cps}"
    bl "{cps=5}...{/cps}"
    bl "{cps=30}Anyway, you should be on your way to first period, I would also implore you to check out some of the clubs after school.{/cps}"
    main "{cps=30}Alright then, thanks for your help Mr. Blankenship{/cps}"
        # School bell here?
    scene bg classroom
    with diss
    main "{cps=30}Sigh...{/cps}"
    main "{cps=30}New school, still boring I guess...{/cps}"
    main "{cps=30}Well may as well look at some clubs.{/cps}"
    scene hall1
    with diss
    main "{cps=30}Man all these clubs don't feel right to me...{/cps}"
    ambi "{cps=30}Hey bro!{/cps}"
    ambi "{cps=30}Wait up [name]!{/cps}"
    main "{cps=30}?{/cps}"
    show justin
    jus "{cps=30}Hey I'm Justin from your first period class!{/cps}"
    jus "{cps=30}I see your looking for a club to join, right?{/cps}"
    main "{cps=30}I mean, I guess so...{/cps}"
    jus "{cps=30}Well you should join my club, Boy's Club!{/cps}"
    main "{cps=30}Boy's Club? Sounds pretty sus to me...{/cps}"
    jus "{cps=30}Nah it's not like that... well most of the time.{/cps}"
    jus "{cps=30}Anyway, it's really just a bunch of friends that hang out and stuff{/cps}"
    jus "{cps=30}Come with me, we're meeting right now!{/cps}"
    main "{cps=30}Well whatever...{/cps}"
    scene boysclub1
    with diss
    jus "{cps=30}Well here we are! Go ahead and talk to everyone.{/cps}"
    $ matthew = False
    $ jack = False
    $ robert = False
    $ greta = False
    $ brian = False
    $ watashi = False
    menu club_member:
        "Pick a character to learn about"


        "Matthew" if matthew == False:
            show matthewsmile
            "{cps=30}Matthew is a strange man. He loves 7/11 conspiracies, jazz and being as annoying as possible. Don't mention tickets around him.{/cps}"
            $ matthew = True
            hide matthewsmile
        "Jack" if jack == False:
            show jackie
            "{cps=30}Jack is a MASTER CODER. He loves getting reddit upvotes, girls and won an award for being an outstanding band member. Don't mention steamed hams around him.{/cps}"
            $ jack = True
            hide jackie
        "Robert" if robert == False:
            show robert
            #this was i, justin cartier the third
            "{cps=30}Robert is an inspiring navy officer. He loves the south, hats and is fluent in banjo. Don't mention world war II around him.{/cps}"
            $ robert = True
            hide robert
        "Greta" if greta == False:
            show greta
            "{cps=30}Greta is the only girl in the club. She loves anime, Denmark and 'Vote Felippo' stickers. Don't mention a man by the name of Rosenburg.{/cps}"
            $ greta = True
            hide greta
        "Brian" if brian == False:
            show brian
            #put something
            $ brian = True
            hide brian
        "Watashi" if greta == matthew == robert == jack == brian == True:
            show justin
            jus "{cps=30}I am the leader of the club. I love Jojo's Bizzare Adventure, One Piece and History.{/cps}"
            jump after_intro

    label matthew:
        jump club_member
    label jack:
        jump club_member
    label robert:
        jump club_member
    label greta:
        jump club_member
    label brian:
        jump club_member
    label after_intro:
        "After learning about a member of the boys club, I reconsidered my application to the club"
    scene back
    with diss
    "The only route available at the moment is Matthew's."
    scene bg classroom
    with diss
    main "Another boring day, probably cause I don't actually try in class..."
    scene hall1
    with diss
    main "Well guess I'll head home..."
    ambi "Hey [name]."
    show blanky:
        xalign 0.5
        yalign 0.1
    with diss
    main "Oh, hello sir."
    bl "I swear..."
    main "Huh?"
    bl "Nevermind that...How do you like it here so far? Find any clubs yet?"
    main "Yeah I've found one but i'm not sure about it..."
    bl "Which club?"
    main "Boys Club"
    bl "Oh..."
    hide blanky
    with diss
    main "What was that about?"
    show zach
    with diss
    zach "Hey, you should join the comp sci club."
    main "Tempting offer, but I pass."
    zach "Whatever you say, though it's cooler than boys club. You'll see one day"
    hide zach
    with diss
    main "... Don't know what that was, but I need to get home."
    scene road
    "You hear what sounds like a married couple arguing around the corner"
    $ Look = False
    $ DontLook = False
    menu take_a_peek:
        "Take a peek around the corner?"


    "Take a peek":
        show jackie at slightleft
        show matthewsmile at slightright
    ambi "I don't see why you're so hellbent on proving me wrong."
    ambi "I don't see why you think you're right."

    label Take_a_peek:
    "You see two guys arguing over what seems to be something stupid."



        # ... the game continues here.
    # This ends the game.

    return

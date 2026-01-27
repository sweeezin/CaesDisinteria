

#left bar 
screen left_box: 
    fixed:
        frame:
            xsize 365
            ysize 990
            xpos 45
            ypos 45


#right bar 
screen right_bar: 
    frame:
        xsize 365
        ysize 990
        xpos 1500
        ypos 45

#top mid screen 
screen environment_view():

    fixed:
        xpos 0
        ypos 45

        frame:
            xsize 960
            ysize 470
            xalign 0.5

            text "ENVIRONMENT VIEW\n(950 x 470)":
                xalign 0.5
                yalign 0.5
            
            
screen dialogue_box():

    frame:
        xsize 680
        ysize 475
        xpadding 20
        ypadding 20
        background "#111"

        xpos 960
        xanchor 0.5
        xoffset 135

        ypos 1035
        yanchor 1.0

        has viewport:
            draggable True
            mousewheel True
            scrollbars "vertical"

        vbox:
            spacing 10

            text ("Scrollable dialogue text goes here.\n" * 20)

            textbutton "Option 1"
            textbutton "Option 2"
            textbutton "Option 3"


screen map():
    frame:
        xsize 240
        ysize 475

        xpos 480
        xanchor 0.0

        ypos 1035
        yanchor 1.0

        
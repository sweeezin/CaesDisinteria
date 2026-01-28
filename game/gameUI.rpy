

#left bar 
screen left_box: 
    fixed:
        frame:
            xsize 365
            ysize 990
            xpos 45
            ypos 45
            padding (20,20)

            fixed:
                xfill True
                yfill True

                # =============================
                # TOP CONTENT
                # =============================
                vbox:
                    spacing 8
                    xfill True
                    yalign 0.0

                    hbox:
                        xfill True

                        # Day / Time (left)
                        vbox:
                            spacing 4
                            xalign 0.0
                            text "Day: [game_day]" size 27
                            text "Time: [game_time]" size 27

                        # Money (right)
                        text "$[pc_money:.2f]" size 27 xalign 1.0

                    null height 20
                    
                    add RadarChart(size=260) xalign 0.5

                    null height 20

                    use heartbeat_placeholder()
                    null height 15

                    vbox:
                        spacing 8
                        xfill True
                        
                        use stat_bar("Pain", pc_pain)
                        use stat_bar("Stress", pc_stress)
                        use stat_bar("Fatigue", pc_fatigue)
                        use stat_bar("Vitality", pc_vitality)

                vbox:
                    yalign 1.0
                    spacing 6
                    xfill True

                    # Journal / Stats row
                    hbox:
                        spacing 6
                        xfill True

                        frame:
                            xsize 160
                            padding (6,4)

                            textbutton "Journal":
                                background None
                                xalign 0.5
                                action Show("journal_screen")

                        frame:
                            xsize 160
                            padding (6,4)

                            textbutton "Stats":
                                background None
                                xalign 0.5
                                action Show("stats_screen")

                    # Saves (full width)
                    frame:
                        xfill True
                        padding (6,4)

                        textbutton "Saves":
                            background None
                            xalign 0.5
                            action ShowMenu("save")

                    # Options (full width)
                    frame:
                        xfill True
                        padding (6,4)

                        textbutton "Options":
                            background None
                            xalign 0.5
                            action ShowMenu("preferences")




screen journal_screen():

    modal True

    frame:
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 600
        padding (20,20)

        vbox:
            spacing 20

            text "Journal" size 23 xalign 0.5

            text "Journal content placeholder."

            textbutton "Close":
                xalign 0.5
                action Hide("journal_screen")

screen stats_screen():

    modal True

    frame:
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 600
        padding (20,20)

        vbox:
            spacing 20

            text "Stats" size 23 xalign 0.5

            text "Stats screen placeholder."

            textbutton "Close":
                xalign 0.5
                action Hide("stats_screen")


 

screen heartbeat_placeholder():
    frame:
        xalign 0.5
        xsize 300
        ysize 60
        padding (4,4)

        frame:
            xfill True
            yfill True

            text "heart rate gif" xalign 0.5 yalign 0.5 size 23



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

        
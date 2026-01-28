

#left bar 
screen left_box: 
    fixed:
        frame:
            xsize 365
            ysize 990
            xpos 45
            ypos 45

            padding(20,20)

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

                        text "Day: [game_day]" size 24
                        text "Time: [game_time]" size 24

                    # Money (right)
                    text "$[pc_money:.2f]" size 24 xalign 1.0

                null height 20
            
                add RadarChart(size=280) xalign 0.5
                null height 20

                vbox:
                    spacing 8
                    xfill True

                    use stat_bar("Pain", pc_pain)
                    use stat_bar("Stress", pc_stress)
                    use stat_bar("Fatigue", pc_fatigue)
                    use stat_bar("Vitality", pc_vitality)
            
                $ tooltip = GetTooltip()

                if tooltip:
                    frame:
                        xpos 0
                        ypos 900
                        padding (6,4)
                        background Solid("#000")

                        text tooltip size 14 outlines [(2,"#000",0,0)]


 

            


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

        
init python:
    import math
    import pygame

    class RadarChart(renpy.Displayable):
        def __init__(self, size=220, max_value=100, **kwargs):
            super(RadarChart, self).__init__(**kwargs)
            self.size = size
            self.max_value = max_value

            self.labels = [
                "Strength",
                "Agility",
                "Charm",
                "Intellect",
                "Courage",
            ]

        def render(self, width, height, st, at):
            size = self.size
            r = renpy.Render(size, size)

            cx = size / 2
            cy = size / 2
            radius = size / 2 - 20

            values = [
                pc_strength,
                pc_agility,
                pc_charm,
                pc_intelligence,
                pc_courage,
            ]

            points_bg = []
            points_fg = []
            label_points = []

            for i in range(5):
                # Upside-down orientation
                angle = math.pi / 2 + i * (2 * math.pi / 5)

                # Outer pentagon
                x = cx + math.cos(angle) * radius
                y = cy + math.sin(angle) * radius
                points_bg.append((x, y))

                # Label positions (slightly farther out)
                lx = cx + math.cos(angle) * (radius + 14)
                ly = cy + math.sin(angle) * (radius + 14)
                label_points.append((lx, ly))

                # Inner stats
                v = values[i] / float(self.max_value)
                x2 = cx + math.cos(angle) * radius * v
                y2 = cy + math.sin(angle) * radius * v
                points_fg.append((x2, y2))

            surf = pygame.Surface((size, size), pygame.SRCALPHA)

            # Outline pentagon
            pygame.draw.polygon(surf, (180, 180, 180), points_bg, 2)

            # Filled stats
            pygame.draw.polygon(surf, (220, 220, 220, 120), points_fg, 0)
            pygame.draw.polygon(surf, (240, 240, 240), points_fg, 2)

            r.blit(surf, (0, 0))

            # Draw labels
            for i, (lx, ly) in enumerate(label_points):
                txt = renpy.render(
                    renpy.text.text.Text(self.labels[i], size=23, color="#DDD", outlines=[ (2, "#000", 0, 0) ]),
                    100, 40, st, at
                )

                r.blit(txt, (lx - txt.width / 2, ly - txt.height / 2))

            return r

screen stat_bar(label, value, max_value=100):

    vbox:
        spacing 2
        xfill True

        # Label ABOVE bar
        text label size 23 xalign 0.5 outlines [(2,"#000",0,0)]

        frame:
            xfill True
            ysize 16
            padding (2,2)
            background Solid("#222")

            bar:
                value value
                range max_value
                xfill True
                ysize 12
                left_bar Solid("#DDD")
                right_bar Solid("#444")
                tooltip "[value] / [max_value]"


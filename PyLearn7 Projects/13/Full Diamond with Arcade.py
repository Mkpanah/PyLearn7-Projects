# Library imports
import arcade

COLUMN_SPACING = 20
ROW_SPACING = 20
LEFT_MARGIN = 110
BOTTOM_MARGIN = 110


# Open the window and set the background
arcade.open_window(400, 400, "Complex Loops - Full Square Diamonds")

arcade.set_background_color(arcade.color.WHITE)

# Start the render process. This must be done before any drawing commands.
arcade.start_render()

# Loop for each row
for row in range(9):
    # Loop for each column
    # Change the number of columns depending on the row we are in
    for column in range(9):
        if ((row % 2 == 0) and (column % 2 == 0)) or ((row % 2 == 1) and (column % 2 == 1)):
            # Calculate our location
            x = (column * COLUMN_SPACING) + LEFT_MARGIN
            y = (row * ROW_SPACING) + BOTTOM_MARGIN

            # Draw the item
            arcade.draw_rectangle_filled(center_x=x, center_y=y, width=10, height=10, color=arcade.color.BLUE, tilt_angle=45)
        else:
            x = (column * COLUMN_SPACING) + LEFT_MARGIN
            y = (row * ROW_SPACING) + BOTTOM_MARGIN

            # Draw the item
            arcade.draw_rectangle_filled(center_x=x, center_y=y, width=10, height=10, color=arcade.color.RED, tilt_angle=45)

# Finish the render.
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
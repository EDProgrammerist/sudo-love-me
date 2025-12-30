from nicegui import ui
import random

# --- Functions ---
def move_button():
    # Random position (using percentages to keep it on screen)
    new_top = random.randint(10, 80)
    new_left = random.randint(10, 80)
    # Update button style to move it absolute
    no_btn.style(f'position: absolute; top: {new_top}%; left: {new_left}%; transition: all 0.2s ease;')

def accepted():
    ui.notify('I knew you liked me! ❤️', type='positive', close_button=True)
    # Optional: Clear the screen and show a success message
    card.clear()
    with card:
        ui.label("❤️").classes('text-6xl text-red-500 animate-bounce')
        ui.label("It's a date!").classes('text-2xl font-bold')

# --- UI Setup ---
# Set the background color of the main page
ui.query('body').style('background-color: #2C3E50;')

# Create a centered card (Floating "Window")
with ui.card().classes('fixed-center w-96 h-80 items-center justify-center shadow-2xl bg-white') as card:
    
    # Title Label
    ui.label('I like You, Do You Like Me?').classes('text-xl font-bold text-gray-800 mb-10 text-center')

    # Container for buttons
    with ui.row().classes('w-full justify-center gap-4 relative'):
        
        # YES Button
        ui.button('Yes', on_click=accepted).props('color=green glossy push')
        
        # NO Button
        # We start it with relative position, but move_button will make it absolute
        no_btn = ui.button('No', on_click=lambda: ui.notify('How did you click this?!')) \
                   .props('color=red glossy push') \
                   .on('mouseover', move_button) # Moves on hover

# Run the app
# native=True makes it look like a desktop app instead of opening a browser tab
ui.run(title='Proposal', native=True, window_size=(500, 500))
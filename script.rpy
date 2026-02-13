# Define your BL characters
define s = Character("Sarawat", color="#1e90ff") # Thai BL reference
define t = Character("Tine", color="#ff69b4")

label start:
    scene bg university_campus # Add your background image
    
    show sarawat_smiling # Add your character sprite
    
    s "Are you still following me?"
    
    show tine_confused
    
    t "I'm not following you! I'm just... going this way."
    
    menu:
        "Ask him to fake-date you":
            jump fake_dating_route
        "Run away blushing":
            jump shy_route

label fake_dating_route:
    s "Fine. But don't fall in love with me for real."
    return

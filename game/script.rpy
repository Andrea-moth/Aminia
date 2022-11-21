define gap = Character(None, what_xalign=0.5)

define location = "unknown"

define char_name = "Jamie"
define char =  Character("[char_name]")

label splashscreen:
    "Quick trigger warning, this game will contain some pretty heavy stuff if you're not okay with that it's best not to play"
    menu:
        "TW: Slavery, Racism (fantasy) and other such horrible stuff"
        "I can handle it":
            return 
        "I'm actually not okay with that at all":
            "Well thanks for coming, hope you find what you're looking for"
            $ renpy.quit()

label quit:
    return

label start:
    jump prolouge
    
label not_written:
    "Sorry that's not written yet"

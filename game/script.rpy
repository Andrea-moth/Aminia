label start:
    "Hi, welcome to Amina, please do not ask why I called it that"

    "Quick trigger warning, this game will contain some pretty heavy stuff if you're not okay with that it's best not to play"
    menu:
        "If you can't handle the general themes of slavery and a mild bit of violence I could always skip it for you"
        "I can handle it":
            "Let's get to it then"
            jump prolouge
        "I'm actually not okay with that at all":
            "Well thanks for coming, hope you find what you're looking for"
            return

label not_written:
    "Sorry that's not written yet"
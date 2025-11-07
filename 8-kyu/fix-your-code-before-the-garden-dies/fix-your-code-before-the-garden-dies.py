 
def rain_amount(mm):
    if mm < 40:
        mm = 40 - mm
        return f"You need to give your plant {mm}mm of water"
    else:
        return "Your plant has had more than enough water for today!"
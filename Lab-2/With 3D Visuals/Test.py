import keyboard

while True:
    try:
        keyboard.read_key()
        print(keyboard._key_table)
        if keyboard.is_pressed(keyboard.KEY_UP):
            req = [0,1,0]
        if keyboard.is_pressed(keyboard.KEY_DOWN):
            req = [0,-1,0]
        if keyboard.is_pressed(keyboard._key_table):
            req = [0,1,0]
        if keyboard.is_pressed('q'):  # if key 'a' is pressed
            print('You Pressed A Key!')
            break  # finishing the loop
        else:
            pass
    except:
        break
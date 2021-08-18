#Modifying Global Scope

enemies = 1

def increase_enemies():
    '''
    global enemies
    enemies += 1
    '''
    print(f"\tEnemies inside funciton: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

#117. Python Constants and Global Scope
PI = 3.14159
URL = "http://www.google.tw"
TWITTER_HANDLE = "@yu_angela"
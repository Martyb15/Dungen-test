import random, os, time

fileExists = os.path.isfile("load.txt")


# HERO CLASS
class Hero():
    def __init__(self, name, health, strength, defence, magic):
        self.name = name
        self.health = health
        self.strength = strength
        self.defence = defence
        self.magic = magic
        self.wallet = 0
        self.start_health = 0
    
    def reset(self):
      self.health = self.start_health
    
    def get_health(self):
      self.start_health = self.health
      
# ENEMY CLASS
class Enemy():
  def __init__(self, name, health, strength, defence, magic, loot):
    self.name = name
    self.health = health
    self.strength = strength
    self.defence = defence
    self.magic = magic
    self.loot = loot
    self.start_health = 0
    
  def reset(self):
    self.health = self.start_health
    
  def get_health(self):
    if self.name == "ogre":
      self.start_health = 50
    elif self.name == "zombie":
      self.start_health = 60
    elif self.name =="goblin":
      self.start_health = 70
#======================================================      


def heroSelect():
  choice = int(input("welcome to the game, please select your agent \n1) Reyna\n2) Jett\n3) Brimstone\n"))
  if choice==1:
    character = Hero("reyna", 50, 10, 10, 10, )
    character.get_health()
    print("health =", character.health)
    print("strength =", character.strength)
    print("defence =", character.defence)
    print("magic =", character.magic)
    return character
  
  elif choice==2:
    character = Hero("Jett",20,20,5,10,)
    character.get_health()
    print("health =", character.health)
    print("strength =", character.strength)
    print("defence =", character.defence)
    print("magic =", character.magic)
    return character

  elif choice == 3:
    character = Hero("Brimstone",60,5,15,10, )
    character.get_health()
    print("testing character")
    print("health =", character.health)
    print("strength =", character.strength)
    print("defence =", character.defence)
    print("magic =", character.magic)
    return character
  

def enemySelect(zombie, goblin, ogre):
  enemyList = [zombie, goblin, ogre]
  chance = random.randint(0,2)
  enemy = enemyList[chance] 
  return enemy

# Enemy object declaration 

zombie = Enemy("zombie", 60, 10, 10, 0, 10)
ogre = Enemy("ogre",50,20,5,0,10)
goblin = Enemy("goblin", 70,5,10,1,10)

enemy = enemySelect(zombie, goblin, ogre)


def load():
  print( "_____ ")                              
  print("|  __ \ ")                          
  print("| |  | |_   _ _ __   __ _  ___ _ __") 
  print("| |  | | | | | '_ \ / _` |/ _ \ '_ \  ")
  print("| |__| | |_| | | | | (_| |  __/ | | | ")
  print("|_____/ \__,_|_| |_|\__, |\___|_| |_| ")
  print("                     __/ | ")           
  print("                    |___/             ")
  time.sleep(3)
  os.system("clear")
  if fileExists:
    try:
      f = open("load.txt","r")
      loot = int(f.readline())
      f.close()
    except ValueError:
      loot = 0
    return loot

def save(loot):
  if fileExists:
    f = open("load.txt", "w")
    f.write(str(loot))
    f.close()

    

if fileExists:
  loot = load()
else: 
  loot = 0


def battle():
  os.system('clear')
  print('a wild', enemy.name, "has appeared!\n")
  
  while enemy.health > 0 and character.health > 0:
    choice = int(input('you have three options,\n1:sword\n2:magic\n3:RUN\n0:stop program\n'))
    
    if choice == 1:
      print('you swing your sword attacking the', enemy.name)
      hitChance = random.randint(1,3)
      
      if hitChance == 1 :
        enemy.health -= character.strength
        print('the enemys health is now', enemy.health) 
        
        if enemy.health > 1 :
          print("the enemy hits you back and your health is now")
          character.health -= enemy.strength/character.defence
          print(character.health )
          
      else:
        print('you missed and the enemy hit you!\n')
        character.health -= enemy.strength/character.defence
        print('your health is now', character.health)

    elif choice == 2:
      print("you chose to heal yourself using magic")
      
      if character.magic == 10:
        character.magic -=10
        character.health += 15
        print("you sucessfully healed yourself but you cannot use this function anymore")
      
      else:
        print("you dont have any magic left! the enmy hit you while you were trying to heal")
        character.health -=2
        print("your health is now ", character.health)
      
    elif choice == 3:
      print('RUN')
      randomRUN = random.randint(0,10)
      if randomRUN != 7:
        character.health -= 10
        print('the',enemy.name, 'hit you!\nhealth:', character.health )
      elif randomRUN == 7:
        print("you ran away")
        break
        
    elif choice == 0:
      break
    
    
  if enemy.health <= 0:
    character.wallet += enemy.loot
    print("@@@your wallet balance is now ",character.wallet)
# BATTLE Function end
      

character = heroSelect()
battle()
time.sleep(2)


# Replay Loop
while True:
  time.sleep(2)
  os.system("clear") #Clears console
  print("would you like to battle again ? y/n :", end="")
  Choice = input("").upper()
  
  if Choice == "Y":
    enemySelect(zombie, goblin, ogre)
    character.get_health()
    character.reset()
    enemy.get_health()
    enemy.reset()
    print("--hero start Health---", character.health)
    print("--hero Health---", character.health)
    print("--enemy Health---", enemy.health)
    print("---enemy start Health",enemy.start_health)
    
    # reset enemy and character health
    # select an enemy
    
    battle()
  elif Choice == "N":
    save(character.wallet)
    break
  else:
    continue
    



character.health - 10




# Add loot function 

# Creat Hero Class                                                   (DONE)

# Create the reset for object health                                 (DONE)

# Reset the enemy object to a different enemy type at 
# the end of each battle                                             (DONE)



# ---Learn---
# File handling
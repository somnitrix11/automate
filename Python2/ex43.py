from sys import exit
import random

class Engine(object):

    def __init__(self, curr_map):
        self.map = curr_map

    def play(self):
        while True:
            self.map.load_scene()

class Map(object):

    def __init__(self, curr_scene):
        self.scene = curr_scene
        self.dead = False

    def next_scene(self, scene):
        if self.dead:
            self.scene = "Death"
        else:
            self.scene = scene

    def load_scene(self):
        if self.scene is "Central_Corridor":
            scene_object = CentralCorridor()
            if scene_object.fail:
                self.dead = True
            self.next_scene("Laser_Weapon_Armory")
        elif self.scene is "Laser_Weapon_Armory":
            scene_object = LaserWeaponArmory()
            if scene_object.fail:
                self.dead = True
            self.next_scene("The_Bridge")
        elif self.scene is "The_Bridge":
            scene_object = Bridge()
            if scene_object.fail:
                self.dead = True
            self.next_scene("Escape_Pod")
        elif self.scene is "Escape_Pod":
            scene_object = EscapePod()
            if scene_object.fail:
                self.dead = True
            self.next_scene("Death")
        else:
            scene_object = Death()

class Scene(object):
    def enter(self):
        pass

class Death(Scene):

    def __init__(self):
        self.enter()

    def enter(self):
        print("and You die\vMISSION FAILED")
        exit()

class CentralCorridor(Scene):

    def __init__(self):
        self.fail = self.enter()

    def enter(self):
        print("*************************************")
        print("(At NASA)")
        print("*HIGH ALERT*\n*SECURITY BREECH*")
        print("There has been an alien invasion at NASA's spaceship", end='')
        print(" and you have been sent to destroy the ship and escape.")
        print("Aliens should not get any critical information about Homo Sapiens.")
        print("MISSION OBJECTIVE : Destroy Spaceship using Neutron bomb")
        print("\n","..."*10)
        print("You reached the CENTRAL CORRIDOR of the ship.")
        print("WOAH! There stands Gothon (Alien General) infront of you.")
        print("Only way to escape is to distract him.")
        print("Aliens can't control laughter so you think of cracking him up with a joke.")
        self.joke = input("> ")
        if (len(self.joke) < 10):
            print("That joke was seriously bad.\nYou are going to face Gothon's Wrath.\nPrepare for a fight.\nYou had no chance against Gothon.")
            return True
        else:
            print("Good Job! He can't control himself so you slip through his side into another lobby and through a door into a room.")
            return False

class LaserWeaponArmory(Scene):

    def __init__(self):
        self.fail = self.enter()

    def enter(self):
        print("\n","..."*10)
        print("You enter the LASER WEAPON ARMORY and you should find a Neutron Bomb here somewhere.")
        print("You found the Bomb now but NOOO!...")
        print("It has a PASSCODE.")
        print("You search for the code in the room and AHA !")
        print("You found the four digit code but wait it's last digit is blotted.")
        print("Looks like you have to guess the last digit.")
        values = []
        for i in range(0, 10):
            values.append(i)
        self.last_digits = random.sample(values, 5)
        self.digit = int(input("> "))
        if self.digit in self.last_digits:
            print("DIGIT ACCEPTED\nYESSSSSS! *phew* That was a really close one. Good Job!")
            print("Now you take the bomb to the bridge to plant.");
            return False
        else:
            print("DIGIT INCORRECT\n*WARNING*\nABOUT TO EXPLODE in ...")
            print("3\n2\n1\n*BOOOOOOOOOOOOOOOOM*\nYou couldn't escape the radius of the explosion.")
            return True

class Bridge(Scene):

    def __init__(self):
        self.fail = self.enter()

    def enter(self):
        print("\n","..."*10)
        print("You reached the BRIDGE (a perfect place to plant the bomb).")
        print("You have the Neutron bomb and are about to plant and ...")
        print("*pew pew pew* laser shooters ! you duck then peek and see Gothon firing at you.")
        print("you have two options either jump off the bridge or shoot back.")
        print("JUMP[J] or SHOOT[S]")
        self.action = input("> ")
        if self.action is "J":
            print("You jump off the bridge onto a small platform by luck under the bridge and plant the bomb succesfully without being noticed.")
            print("The counter starts and you shoot your way towards the escape pods through the walls.")
            return False
        else:
            print("You shoot Gothon's head, his helmet shatters (NICE SHOT) and you try to take another shot but he takes cover.")
            print("He Throws an EMP and your Laser gun gets jammed and you panic.")
            print("Gothon shoots your head off through your cover")
            print("Your Brain bursts out through your skull and Gothon laughs...")
            return True

class EscapePod(Scene):

    def __init__(self):
        self.fail = self.enter()

    def enter(self):
        print("\n","..."*10)
        print("You reach the ESCAPE PODS STATION but Gothon has succesfully damged 4 out 5 pods.")
        print("You have to take a risk on this one here.")
        print("Choose a pod [1-5]")
        self.pod = int(input("> "))
        self.working_pod = random.randint(1, 5)
        if self.pod is self.working_pod:
            print("Lets hope it works.")
            print("You get into the pod and in time escape the radius of explosion.")
            print("You reach Earth safely\vMISSSION ACCOMPLISHED")
            exit()
        else:
            print("Lets hope it works.")
            print("You get into the pod and detach from the ship just to find that its thrusters are damaged.")
            print("You get caught in the radius of explosion and your body disintegrates.")
            return True

mapObject = Map("Central_Corridor")
gameObject = Engine(mapObject)
gameObject.play()

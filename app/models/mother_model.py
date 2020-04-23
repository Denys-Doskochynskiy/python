from abc import ABC, abstractmethod


class AbstractParent(ABC):
    @abstractmethod
    def hello_friend(self):
        raise NotImplementedError


class Mother:
    def __init__(self, age):
        self.age = age
        print("mother construction")

    def do_work(self):
        print("I'm working")

    def do_house_work(self):
        print("mather do_house_work")

    def do_home_work(self):
        print("child cry(((")


class Father(AbstractParent):
    def __init__(self):
        print("father construction")

    def do_house_work(self):
        print("father do_house_work")

    def play_gitar(self):
        print("play gitar")


class Daughter(Mother, Father):
    def __init__(self, age=0):
        Mother.__init__(self, age=age)
        Father.__init__(self)

    def hello_friend(self):
        print("Hello friend")

    def do_work(self):
        print("I'm working like a horse")


class Friend:
    pass


def greet_mother(mother: Mother):
    print("hello mother!!!!!!!!!")
    mother.do_work()


def greet_father(father: Father):
    print("time to eat")
    father.play_gitar()


if __name__ == "__main__":
    daughter = Daughter()
    #  daughter.__class__ = (Friend,Mother)
    greet_mother(daughter)
    greet_father(daughter)
    daughter.hello_friend()
    daughter.do_house_work()
    daughter.do_home_work()

    for x in [daughter]:
        x.do_house_work()
    # frozen_set
    frozen_set = frozenset(["1_d", "2_s", "3_d"])
    print(frozen_set)

    # tuple
    max = ("18 years old", 12, 3.4, daughter)
    print(max)
    # set
    my_set = {23, 24, 4, 4, 4, "call"}
    print(my_set)
    # list
    produckt_list = ["tomato", "potato", "onion"]
    print(produckt_list)
    # dictionary
    my_dict = {"tomato", "potato", 23, 24, 4, 4, 4, "call"}
    print(my_dict)
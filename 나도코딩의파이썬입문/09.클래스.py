# 클래스

# ===== [ 클래스] =====
# 클래스 : 붕어빵 틀과 같은 개념, 객체를 만들기 위한 설계도, 객체는 클래스에서 만들어진 인스턴스, 클래스는 객체의 속성과 행동을 정의

# 마린 : 공격유닛, 보병, 총을 쏠 수 있음

name = "마린" # 유닛의 이름
hp = 40 # 유닛의 체력
damage = 5 # 유닛의 공격력

print("{0} 유닛이 생성되었습니다.".format(name))
print("유닛 이름 : {0}, 공격력 : {1}\n".format(hp, damage))

# 탱크 : 공격유닛, 탱크, 포를 쏠 수 있음, 일반모드/시즈모드
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("유닛 이름 : {0}, 공격력 : {1}\n".format(tank_hp, tank_damage))

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank2_name))
print("유닛 이름 : {0}, 공격력 : {1}\n".format(tank2_hp, tank2_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)

# 일반유닛
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 : {0}, 공격력 : {1}\n".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank1 = Unit("탱크", 150, 35)

# ===== [ __init__ ] =====
# __init__ : 클래스의 생성자, 객체가 만들어질 때 자동으로 호출되는 함수
# self : 객체 자신을 가리키는 변수, 클래스 내에서 정의된 메소드의 첫 번째 매개변수로 사용, 객체의 속성에 접근하거나 메소드를 호출할 때 사용


# ===== [ 멤버변수 ] =====
# 멤버변수 : 클래스 내에서 정의된 변수, 객체마다 고유한 값을 가질 수 있음, 객체의 상태를 나타내는 데 사용

# 레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않는 능력)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 기술
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True # 객체에 새로운 멤버변수 추가
if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

# ===== [ 메소드 ] =====
# 메소드 : 클래스 내에서 정의된 함수, 객체의 행동을 나타내는 데 사용, 객체의 상태를 변경하거나 다른 객체와 상호작용할 때 사용

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
          self.name = name
          self.hp = hp
          self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
              .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 메딕 : 의무병, 치료 유닛, 공격 불가능


# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격을 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

# ===== [ 상속 ] =====
# 상속 : 기존 클래스의 속성과 메소드를 물려받아 새로운 클래스를 만드는 것, 부모 클래스(상위 클래스)와 자식 클래스(하위 클래스)로 구성, 코드의 재사용성을 높이고 유지보수를 쉽게 함

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
              .format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed) # 부모 클래스의 __init__ 메소드 호출
        self.damage = damage


# ===== [ 다중상속 ] =====
# 다중상속 : 하나의 클래스가 둘 이상의 부모 클래스로부터 상속을 받는 것,
# 자식 클래스는 모든 부모 클래스의 속성과 메소드를 물려받음,
# 다중상속은 코드의 재사용성을 높이지만, 복잡성과 충돌 가능성이 증가할 수 있음


# 드랍쉽 : 공중 유닛, 수송기, 마린/파이어뱃/탱크 등을 수송, 공격 불가능
# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
              .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0으로 설정
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 발키리 : 공중 공격 유닛, 발키리, 미사일 14발을 한 번에 발사
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")


# ===== [ 메소드 오버라이딩 ] =====
# 메소드 오버라이딩 : 부모 클래스에서 정의된 메소드를 자식 클래스에서 재정의하는 것,
# 자식 클래스는 부모 클래스의 메소드를 자신의 방식으로 구현할 수 있음,
# 메소드 오버라이딩은 다형성을 구현하는 데 사용

# 벌쳐 : 지상 유닛, 기동성이 좋은
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중 공격 유닛, 배틀크루저, 체력도 굉장히 좋음, 레이져 광선으로 공격
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")

# ===== [ pass ] =====
# pass : 아무 것도 하지 않는 명령어, 함수나 클래스의 몸체가 비어 있을 때 사용,
# 코드의 구조를 유지하면서 나중에 구현할 부분을 표시하는 데 유용

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass # 나중에 구현할 예정

# 서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()

# ===== [ super ] =====
# super : 부모 클래스의 메소드를 호출하는 데 사용
# 자식 클래스에서 부모 클래스의 메소드를 재정의할 때, 부모 클래스의 메소드를 호출하여 기존 기능을 유지하면서 추가적인 기능을 구현할 수 있음

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        super().__init__(name, hp, 0) # 부모 클래스의 __init__ 메소드 호출, speed 0으로 설정
        self.location = location


class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__() # Unit의 __init__ 메소드 호출
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽 : 공중 유닛, 수송기, 마린/파이어뱃/탱크 등을 수송, 공격 불가능
drop_ship = FlyableUnit()

# ===== [ 스타크래프트 프로젝트 전반전 ] =====

# ===== [ 스타크래프트 프로젝트 후반전 ] =====

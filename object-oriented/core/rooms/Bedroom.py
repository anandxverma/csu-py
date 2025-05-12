import core.Room as rm
import core.House_Constants as constants

class Bedroom(rm.Room):
    def __init__(self, area: float, num_windows: int, num_doors: int, has_balcony: bool, story: int = 1):
        super().__init__(constants.RoomType.BEDROOM, area, num_windows, num_doors, story)
        self.__has_balcony = has_balcony

    @property
    def has_balcony(self) -> bool:
        return self.__has_balcony
    @has_balcony.setter
    def has_balcony(self, has_balcony: bool):
        self.__has_balcony = has_balcony

    def __str__(self) -> str:
        return f"{super().__str__()}, Has Balcony: {self.__has_balcony}"
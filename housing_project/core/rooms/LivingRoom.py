import core.Room as rm
import core.House_Constants as constants

class LivingRoom(rm.Room):
    def __init__(self, area: float, num_windows: int, num_doors: int, has_fireplace: bool, story: int = 1):
        super().__init__(constants.RoomType.LIVING_ROOM, area, num_windows, num_doors, story)
        self.__has_fireplace = has_fireplace

    @property
    def has_fireplace(self) -> bool:
        return self.__has_fireplace
    @has_fireplace.setter
    def has_fireplace(self, has_fireplace: bool):
        self.__has_fireplace = has_fireplace

    def __str__(self) -> str:
        return f"{super().__str__()}, Has Fireplace: {self.__has_fireplace}"
import core.Room as rm
import core.House_Constants as constants

class Bathroom(rm.Room):
    def __init__(self, area: float, num_windows: int, num_doors: int, has_bathtub: bool, has_shower: bool, story: int = 1):
        super().__init__(constants.RoomType.BATHROOM, area, num_windows, num_doors)
        self.__has_bathtub = has_bathtub
        self.__has_shower = has_shower

    @property
    def has_bathtub(self) -> bool:
        return self.__has_bathtub
    @has_bathtub.setter
    def has_bathtub(self, has_bathtub: bool):
        self.__has_bathtub = has_bathtub

    @property
    def has_shower(self) -> bool:
        return self.__has_shower
    @has_shower.setter
    def has_shower(self, has_shower: bool):
        self.__has_shower = has_shower
        
    def __str__(self) -> str:
        return f"{super().__str__()}, Has Bathtub: {self.__has_bathtub}, Has Shower: {self.__has_shower}"

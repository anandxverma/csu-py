from abc import ABC, abstractmethod
import core.House_Constants as constants

class Room(ABC):
    def __init__(self, room_type: constants.RoomType, area: float, num_windows: int, num_doors: int, story: int = 1):
        if not isinstance(room_type, constants.RoomType):
            raise ValueError("Invalid room type. Must be a valid value for Room Type.")
        self.__room_type = room_type
        self.__area = area
        self.__num_windows = num_windows
        self.__num_doors = num_doors
        self.__story = story

    @property
    def room_type(self) -> constants.RoomType:
        return self.__room_type
    @room_type.setter
    def room_type(self, room_type: constants.RoomType):
        self.__room_type = room_type

    @property
    def area(self) -> float:
        return self.__area
    @area.setter
    def area(self, area: float):
        if area <= 0:
            raise ValueError("Area must be greater than 0")
        self.__area = area

    @property
    def num_windows(self) -> int:
        return self.__num_windows
    @num_windows.setter
    def num_windows(self, num_windows: int):
        if num_windows < 0:
            raise ValueError("Number of windows cannot be negative")
        self.__num_windows = num_windows

    @property
    def num_doors(self) -> int:
        return self.__num_doors
    @num_doors.setter
    def num_doors(self, num_doors: int):
        if num_doors < 0:
            raise ValueError("Number of doors cannot be negative")
        self.__num_doors = num_doors
    
    @property
    def story(self) -> int:
        return self.__story
    @story.setter
    def story(self, story: int):
        if story < 1:
            raise ValueError("Story must be greater than or equal to 1")
        self.__story = story

    def __str__(self) -> str:
        return f"Room Type: {self.__room_type.value}, Area: {self.__area}, Windows: {self.__num_windows}, Doors: {self.__num_doors}, Story: {self.__story}"

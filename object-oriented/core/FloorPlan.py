from abc import ABC, abstractmethod
import core.Room as rm
import core.House_Constants as constants

class FloorPlan(ABC):
    def __init__(self, floor_plan_type: str, num_stories: int, area: float):
        self.__floor_plan_type = floor_plan_type
        self.__rooms = list[rm.Room]()
        self.__area = area
        self.__num_stories = num_stories

    @property
    def floor_plan_type(self) -> str:
        return self.__floor_plan_type
    @floor_plan_type.setter
    def layout(self, floor_plan_type: str):
        self.__floor_plan_type = floor_plan_type

    @property
    def area(self) -> float:
        return self.__area
    @area.setter
    def area(self, area: float):
        self.__area = area

    @property
    def rooms(self) -> list[rm.Room]:
        return self.__rooms

    @property
    def num_stories(self) -> int:
        return self.__num_stories
    @num_stories.setter
    def num_stories(self, num_stories: int):
        self.__num_stories = num_stories

    @property
    def num_bathrooms(self) -> int:
        return self.__count_room_type(constants.RoomType.BATHROOM)
    
    @property
    def num_bedrooms(self) -> int:
        return self.__count_room_type(constants.RoomType.BEDROOM)
    
    @property
    def num_kitchens(self) -> int:
        return self.__count_room_type(constants.RoomType.KITCHEN)
    
    @property
    def num_living_rooms(self) -> int:
        return self.__count_room_type(constants.RoomType.LIVING_ROOM)
    
    @property
    def num_dining_rooms(self) -> int:
        return self.__count_room_type(constants.RoomType.DINING_ROOM)
    
    @property
    def num_garages(self) -> int:
        return self.__count_room_type(constants.RoomType.GARAGE)
    
    # Add rooms to the floor plan
    def add_room(self, room: rm.Room):
        self.__rooms.append(room)

    # Function to count a specific room type
    def __count_room_type(self, room_type: str) -> int:
        count = 0
        for room in self.__rooms:
            if room.room_type == room_type:
                count += 1
        return count
    
    # Floor Plan string representation
    def __str__(self) -> str:
        return f"Floor Plan Type: {self.__floor_plan_type}, Area: {self.__area}, Number of Stories: {self.__num_stories}, Bedrooms: {self.num_bedrooms}, Bathrooms: {self.num_bathrooms}, Kitchens: {self.num_kitchens}, Living Rooms: {self.num_living_rooms}, Dining Rooms: {self.num_dining_rooms}, Garages: {self.num_garages}"
    
    # Floors plan room details
    def get_room_details(self) -> str:
        room_details = "\n".join([str(room) for room in self.__rooms])
        return f"{room_details}"
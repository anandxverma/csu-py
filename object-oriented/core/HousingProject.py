from abc import ABC, abstractmethod
import core.House as hs

class HousingProject(ABC):
    def __init__(self, name: str, city: str, county: str, state: str):
        self.__name = name
        self.__city = city
        self.__county = county
        self.__state = state
        self.__houses = dict[str, hs.House]()

    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def city(self) -> str:
        return self.__city
    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def county(self) -> str:
        return self.__county
    @county.setter
    def county(self, county: str):
        self.__county = county

    @property
    def state(self) -> str:
        return self.__state
    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def houses(self) -> dict[str, hs.House]:
        return self.__houses
    
    @property
    def number_of_houses(self) -> int:
        return len(self.__houses)

    # Add a house to the project
    def add_house(self, house: hs.House):
        self.__houses[house.unit_number] = house

    def __str__(self):
        return f"{self.__name}, located in {self.__city}, {self.__county}, {self.__state}"
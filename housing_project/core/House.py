from abc import ABC, abstractmethod
import core.FloorPlan as fp
import core.House_Constants as constants

class House(ABC):
    def __init__(self, unit_number: str, address: str, floor_plan: fp.FloorPlan, price: float, status: constants.HouseStatus):
        self.__unit_number = unit_number
        self.__address = address
        self.__floor_plan = floor_plan
        self.__price = price
        if not isinstance(status, constants.HouseStatus):
            raise ValueError("Invalid status. Must be a valid value for HouseStatus.")
        self.__status = status

    @property
    def unit_number(self) -> str:
        return self.__unit_number
    @unit_number.setter
    def unit_number(self, unit_number: str):
        self.__unit_number = unit_number

    @property
    def address(self) -> str:
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def floor_plan(self) -> fp.FloorPlan:
        return self.__floor_plan
    @floor_plan.setter
    def floor_plan(self, floor_plan: fp.FloorPlan):
        self.__floor_plan = floor_plan

    @property
    def price(self) -> float:
        return self.__price
    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def status(self) -> constants.HouseStatus:
        return self.__status
    @status.setter
    def status(self, status: constants.HouseStatus):
        if not isinstance(status, constants.HouseStatus):
            raise ValueError("Invalid status. Must be a valid value for HouseStatus.")
        self.__status = status

    @abstractmethod
    def calculate_property_tax(self) -> float:
        pass

    def __str__(self):
        return f"Unit Number: {self.__unit_number}, Address: {self.__address}, Floor Plan: {self.__floor_plan.floor_plan_type}, Price: ${self.__price:.0f}, Status: {self.__status.value}"
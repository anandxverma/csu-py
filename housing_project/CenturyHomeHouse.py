import core.House as hs
import core.FloorPlan as fp
import core.House_Constants as constants

class CenturyHomeHouse(hs.House):
    def __init__(self, unit_number: str, address: str, floor_plan: fp.FloorPlan, price: float, status: constants.HouseStatus):
        super().__init__(unit_number, address, floor_plan, price, status)

    # Calculate property tax for Century Home House
    def calculate_property_tax(self) -> float:
        return self.price * 0.0125
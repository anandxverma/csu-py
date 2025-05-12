import core.HousingProject as hp
import core.House_Constants as constants
import CenturyHomeFloorPlan1 as chfp1
import CenturyHomeFloorPlan2 as chfp2
import CenturyHomeHouse as chhs

# Initialize the project
prj1 = hp.HousingProject(
    name="Century Homes Villa Bellissima",
    city="Manteca",
    county="San Joaquin",
    state="California"
)
print(prj1, "\n")

# Create Floor Plan 1
floor_plan1 = chfp1.CenturyHomeFloorPlan1()

# Create House 1 for Floor Plan 1
house1 = chhs.CenturyHomeHouse(
    unit_number="1",
    address="1234 Main St, Manteca, CA 95337",
    floor_plan=floor_plan1,
    price=550000,
    status=constants.HouseStatus.FOR_SALE
)
prj1.add_house(house1)
print(house1, f"and tax: ${house1.calculate_property_tax():.0f}")
print(house1.floor_plan.get_room_details(), "\n")

# Create House 2 for Floor Plan 1
house2 = chhs.CenturyHomeHouse(
    unit_number="2",
    address="2314 Main St, Manteca, CA 95337",
    floor_plan=floor_plan1,
    price=600000,
    status=constants.HouseStatus.FOR_SALE
)
prj1.add_house(house2)
print(house2, f"and tax: ${house2.calculate_property_tax():.0f}")
print(house1.floor_plan.get_room_details(), "\n")

# Create Floor Plan 2
floor_plan2 = chfp2.CenturyHomeFloorPlan2()

# Create House 3 for Floor Plan 2
house3 = chhs.CenturyHomeHouse(
    unit_number="3",
    address="1023 First St, Manteca, CA 95337",
    floor_plan=floor_plan2,
    price=800000,
    status=constants.HouseStatus.AVAILABLE_SOON
)
prj1.add_house(house3)
print(house3, f"and tax: ${house3.calculate_property_tax():.0f}")
print(house3.floor_plan.get_room_details(), "\n")

# Print number of houses in the project
print(f"Number of houses in the project: {prj1.number_of_houses}")
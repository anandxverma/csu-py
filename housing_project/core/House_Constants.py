from enum import Enum

class RoomType(Enum):
    """Enum for room types."""
    BATHROOM = "Bathroom"
    LIVING_ROOM = "Living Room"
    BEDROOM = "Bedroom"
    GUESTROOM = "Guestroom"
    KITCHEN = "Kitchen"
    DINING_ROOM = "Dining Room"
    HALL = "Hall"
    GARAGE = "Garage"
    BASEMENT = "Basement"
    ATTIC = "Attic"
    LAUNDRY = "Laundry"

# Class for House Statuses
class HouseStatus(Enum):
    """Enum for house status."""
    FOR_SALE = "For Sale"
    SOLD = "Sold"
    UNDER_CONTRACT = "Under Contract"
    SALES_PENDING = "Sales Pending"
    UNDER_CONSTRUCTION = "Under Construction"
    AVAILABLE_SOON = "Available Soon"

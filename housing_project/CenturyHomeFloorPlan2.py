import core.FloorPlan as fp
import core.rooms.Bathroom as bth
import core.rooms.Bedroom as bed

class CenturyHomeFloorPlan2(fp.FloorPlan):

    def __init__(self):

        super().__init__(
            floor_plan_type="Century Home Floor Plan 2 - 2 Beds x 1 Bath",
            num_stories=1,
            area=1500
        )

        # Add bedroom to the floor plan
        bed1 = bed.Bedroom(
            area=350,
            num_windows=2,
            num_doors=1,
            has_balcony=False,
            story=1
        )
        self.add_room(bed1)

        # Add bedroom to the floor plan
        bed2 = bed.Bedroom(
            area=250,
            num_windows=2,
            num_doors=1,
            has_balcony=False,
            story=1
        )
        self.add_room(bed2)

        # Add bathroom to the floor plan
        bath1 = bth.Bathroom(
            area=100,
            num_windows=1,
            num_doors=1,
            has_bathtub=True,
            has_shower=True,
            story=1
        )
        self.add_room(bath1)

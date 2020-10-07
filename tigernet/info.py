def get_mtfcc_types():
    """Read in dictionary of MTFCC road type descriptions
    https://www.census.gov/geo/reference/mtfcc.html

    ******* Ranks are subjective *******

    """

    mtfcc_types = {
        "S1100": {
            "FClass": "Primary Road",
            "Desc": "Primary roads are generally divided, "
            + "limited-access highways within the "
            + "interstate highway system or under "
            + "state management, and are "
            + "distinguished by the presence of "
            + "interchanges. These highways are "
            + "accessible by ramps and may include "
            + "some toll highways.",
        },
        "S1200": {
            "FClass": "Secondary Road",
            "Desc": "Secondary roads are main arteries, "
            + "usually in the U.S. Highway, State "
            + "Highway or County Highway system. "
            + "These roads have one or more lanes of "
            + "traffic in each direction, may or may "
            + "not be divided, and usually have "
            + "at-grade intersections with many "
            + "other roads and driveways. They often "
            + "have both a local name and a route "
            + "number.",
        },
        "S1400": {
            "FClass": "Local Neighborhood Road, " + "Rural Road, City Street",
            "Desc": "Generally a paved non-arterial street, "
            + "road, or byway that usually has a "
            + "single lane of traffic in each "
            + "direction. Roads in this feature "
            + "class may be privately or publicly "
            + "maintained. Scenic park roads would "
            + "be included in this feature class, "
            + "as would (depending on the region of "
            + "the country) some unpaved roads.",
        },
        "S1500": {
            "FClass": "Vehicular Trail (4WD)",
            "Desc": "An unpaved dirt trail where a "
            + "four-wheel drive vehicle is required. "
            + "These vehicular trails are found "
            + "almost exclusively in very rural "
            + "areas. Minor, unpaved roads usable by "
            + "ordinary cars and trucks belong in "
            + "the S1400 category.",
        },
        "S1630": {
            "FClass": "Ramp",
            "Desc": "A road that allows controlled access "
            + "from adjacent roads onto a limited "
            + "access highway, often in the form of "
            + "a cloverleaf interchange. These roads "
            + "are unaddressable.",
        },
        "S1640": {
            "FClass": "Service Drive usually along a limited " + "access highway",
            "Desc": "A road, usually paralleling a limited "
            + "access highway, that provides access "
            + "to structures along the highway. "
            + "These roads can be named and may "
            + "intersect with other roads.",
        },
        "S1710": {
            "FClass": "Walkway/Pedestrian Trail",
            "Desc": "A path that is used for walking, being "
            + "either too narrow for or legally "
            + "restricted from vehicular traffic.",
        },
        "S1720": {
            "FClass": "Stairway",
            "Desc": "A pedestrian passageway from one level "
            + "to another by a series of steps.",
        },
        "S1730": {
            "FClass": "Alley",
            "Desc": "A service road that does not generally "
            + "have associated addressed structures "
            + "and is usually unnamed. It is located "
            + "at the rear of buildings and "
            + "properties and is used for "
            + "deliveries.",
        },
        "S1740": {
            "FClass": "Private Road for service vehicles "
            + "(logging, oil fields, ranches, etc.)",
            "Desc": "A road within private property that is "
            + "privately maintained for service, "
            + "extractive, or other purposes. These "
            + "roads are often unnamed.",
        },
        "S1750": {
            "FClass": "Internal U.S. Census Bureau use",
            "Desc": "Internal U.S. Census Bureau use",
        },
        "S1780": {
            "FClass": "Parking Lot Road",
            "Desc": "The main travel route for vehicles "
            + "through a paved parking area.",
        },
        "S1820": {
            "FClass": "Bike Path or Trail",
            "Desc": "A path that is used for manual or "
            + "small, motorized bicycles, being "
            + "either too narrow for or legally "
            + "restricted from vehicular traffic.",
        },
        "S1830": {
            "FClass": "Bridle Path",
            "Desc": "A path that is used for horses, being "
            + "either too narrow for or legally "
            + "restricted from vehicular traffic.",
        },
        "S2000": {
            "FClass": "Road Median",
            "Desc": "The unpaved area or barrier between "
            + "the carriageways of a divided road.",
        },
    }

    return mtfcc_types

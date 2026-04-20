class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error"):
        pass

class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass

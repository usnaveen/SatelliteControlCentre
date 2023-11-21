import logging
from abc import ABC, abstractmethod

# Configure logging to store logs in a file as well as print them
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("satellite_logs.log"), logging.StreamHandler()],
)


# Abstract class for Satellite Actions
class SatelliteAction(ABC):
    @abstractmethod
    def execute(self, satellite):
        pass


# Class for Satellite
class Satellite:
    def __init__(self):
        self.orientation = "North"
        self.solar_panels = "Inactive"
        self.data_collected = 0

    def apply_action(self, action):
        action.execute(self)

    # Method to view the current state of the satellite
    def get_state(self):
        return f"Orientation: {self.orientation}, Solar Panels: {self.solar_panels}, Data Collected: {self.data_collected}"


# Rotate action - Demonstrates SRP
class RotateAction(SatelliteAction):
    def __init__(self, direction):
        self.direction = direction

    def execute(self, satellite):
        satellite.orientation = self.direction
        logging.info(f"Satellite rotated to {self.direction}.")


# Activate Panels action - Demonstrates SRP
class ActivatePanelsAction(SatelliteAction):
    def execute(self, satellite):
        satellite.solar_panels = "Active"
        logging.info("Solar panels activated.")


# Deactivate Panels action - Demonstrates SRP
class DeactivatePanelsAction(SatelliteAction):
    def execute(self, satellite):
        satellite.solar_panels = "Inactive"
        logging.info("Solar panels deactivated.")


# Collect Data action - Demonstrates SRP
class CollectDataAction(SatelliteAction):
    def execute(self, satellite):
        if satellite.solar_panels == "Active":
            satellite.data_collected += 10
            logging.info(
                f"Data collected. Total data: {satellite.data_collected} units."
            )
        else:
            logging.warning("Cannot collect data. Solar panels are inactive.")


def main():
    satellite = Satellite()
    actions = [
        RotateAction("South"),
        ActivatePanelsAction(),
        CollectDataAction(),
        DeactivatePanelsAction(),
    ]

    for action in actions:
        satellite.apply_action(action)

    # Display the state of the satellite before showing logs
    print("\n State of the Satellite :")
    print(satellite.get_state())

    # Displaying logs
    with open("satellite_logs.log", "r") as log_file:
        print("\nLogs logged during the process:")
        print(log_file.read())


if __name__ == "__main__":
    main()

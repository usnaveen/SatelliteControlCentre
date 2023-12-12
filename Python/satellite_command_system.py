import logging
import time

# Configure logging to store logs in a file as well as print them with a tab-separated format
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s\t%(levelname)s\t%(message)s",
    handlers=[logging.FileHandler("satellite_logs.log"), logging.StreamHandler()],
)

# Base class for satellite actions
class SatelliteAction:
    def execute(self, satellite):
        try:
            self._execute(satellite)
        except Exception as e:
            # Log any errors that occur during action execution
            logging.error(f"An error occurred: {e}")

    def _execute(self, satellite):
        pass

# Class representing the state of the satellite
class Satellite:
    def __init__(self):
        self.orientation = "North"
        self.solar_panels = "Inactive"
        self.data_collected = 0

    def apply_action(self, action):
        # Apply the specified action to modify the satellite state
        action.execute(self)

    def get_state(self):
        # Return a formatted string representing the current state of the satellite
        return f"\nOrientation: {self.orientation}, \nSolar Panels: {self.solar_panels}, \nData Collected: {self.data_collected}"

# Action to rotate the satellite
class RotateAction(SatelliteAction):
    def __init__(self, direction):
        self.direction = direction

    def _execute(self, satellite):
        try:
            # Check if the direction is valid
            if self.direction.lower() not in ["north", "south", "east", "west"]:
                raise ValueError(f"Invalid direction: {self.direction}")
            
            # If the direction is valid, rotate the satellite
            satellite.orientation = self.direction.capitalize()
            logging.info(f"Satellite rotated to {self.direction}.")
        except ValueError as ve:
            # Log errors related to invalid direction
            logging.error(f"Error in RotateAction: {ve}")
        except Exception as e:
            # Log unexpected errors during action execution
            logging.error(f"Unexpected error in RotateAction: {e}")

# Action to activate solar panels
class ActivatePanelsAction(SatelliteAction):
    def _execute(self, satellite):
        try:
            # Check if the solar panels are already active
            if satellite.solar_panels == "Active":
                raise RuntimeError("Solar panels are already active.")
            
            # If panels are not active, activate them
            satellite.solar_panels = "Active"
            logging.info("Solar panels activated.")
        except RuntimeError as re:
            # Log errors related to activating already active panels
            logging.error(f"Error in ActivatePanelsAction: {re}")
        except Exception as e:
            # Log unexpected errors during action execution
            logging.error(f"Unexpected error in ActivatePanelsAction: {e}")

# Action to deactivate solar panels
class DeactivatePanelsAction(SatelliteAction):
    def _execute(self, satellite):
        try:
            # Check if the solar panels are already inactive
            if satellite.solar_panels == "Inactive":
                raise RuntimeError("Solar panels are already inactive.")
            
            # If panels are not inactive, deactivate them
            satellite.solar_panels = "Inactive"
            logging.info("Solar panels deactivated.")
        except RuntimeError as re:
            # Log errors related to deactivating already inactive panels
            logging.error(f"Error in DeactivatePanelsAction: {re}")
        except Exception as e:
            # Log unexpected errors during action execution
            logging.error(f"Unexpected error in DeactivatePanelsAction: {e}")

# Action to collect data
class CollectDataAction(SatelliteAction):
    def _execute(self, satellite):
        try:
            # Check if the solar panels are active or inactive
            if satellite.solar_panels not in ["Active", "Inactive"]:
                raise ValueError("Invalid state for solar panels.")
            
            # If panels are active, collect data
            if satellite.solar_panels == "Active":
                satellite.data_collected += 10
                logging.info(
                    f"Data collected. Total data: {satellite.data_collected} units."
                )
            else:
                # Log a warning if trying to collect data with inactive panels
                logging.warning("Cannot collect data. Solar panels are inactive.")
        except ValueError as ve:
            # Log errors related to invalid state for collecting data
            logging.error(f"Error in CollectDataAction: {ve}")

# Custom exception for network-related errors
class NetworkError(Exception):
    pass

# Function to simulate a transient network error
def simulate_transient_error(satellite):
    try:
        # Simulating a transient error, e.g., network timeout
        logging.info("Attempting to perform an operation that may result in a transient error.")
        time.sleep(2)  # Simulating a brief delay
        raise NetworkError("Simulated network error")
    except NetworkError as ne:
        # Log and handle the network-related error
        logging.error(f"Transient error handling: {ne}")

# Main function to demonstrate the satellite actions
def main():
    satellite = Satellite()
    actions = [
        RotateAction("south"),
        ActivatePanelsAction(),
        CollectDataAction(),
        DeactivatePanelsAction(),
    ]

    for action in actions:
        satellite.apply_action(action)

    print("\nState of the Satellite :")
    print(satellite.get_state())

    with open("satellite_logs.log", "r") as log_file:
        print("\nLogs logged during the process:")
        print(log_file.read())

    # Uncomment the line below to simulate a transient network error
    # simulate_transient_error(satellite)

if __name__ == "__main__":
    main()

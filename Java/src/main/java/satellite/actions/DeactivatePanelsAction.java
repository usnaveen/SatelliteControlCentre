public class DeactivatePanelsAction extends SatelliteAction {
    @Override
    public void execute(Satellite satellite) {
        satellite.setSolarPanels("Inactive");
        LOGGER.info("Solar panels deactivated.");
    }
}

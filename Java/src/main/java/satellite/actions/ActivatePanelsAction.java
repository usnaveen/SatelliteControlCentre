public class ActivatePanelsAction extends SatelliteAction {
    @Override
    public void execute(Satellite satellite) {
        satellite.setSolarPanels("Active");
        LOGGER.info("Solar panels activated.");
    }
}

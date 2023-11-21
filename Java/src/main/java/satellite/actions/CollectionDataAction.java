public class CollectDataAction extends SatelliteAction {
    @Override
    public void execute(Satellite satellite) {
        if ("Active".equals(satellite.getSolarPanels())) {
            satellite.setDataCollected(satellite.getDataCollected() + 10);
            LOGGER.info("Data collected. Total data: " + satellite.getDataCollected() + " units.");
        } else {
            LOGGER.warning("Cannot collect data. Solar panels are inactive.");
        }
    }
}

public class RotateAction extends SatelliteAction {
    private final String direction;

    public RotateAction(String direction) {
        this.direction = direction;
    }

    @Override
    public void execute(Satellite satellite) {
        satellite.setOrientation(direction);
        LOGGER.info("Satellite rotated to " + direction + ".");
    }
}

import java.util.logging.Logger;

public class Main {
    private static final Logger LOGGER = Logger.getLogger(Main.class.getName());

    public static void main(String[] args) {
        Satellite satellite = new Satellite();
        LOGGER.info("Initial State: " + satellite.getState());

        satellite.applyAction(new RotateAction("South"));
        satellite.applyAction(new ActivatePanelsAction());
        satellite.applyAction(new CollectDataAction());
        satellite.applyAction(new DeactivatePanelsAction());

        LOGGER.info("Final State: " + satellite.getState());
    }
}

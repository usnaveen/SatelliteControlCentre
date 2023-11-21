import java.util.logging.Logger;

public abstract class SatelliteAction {
    protected static final Logger LOGGER = Logger.getLogger(SatelliteAction.class.getName());

    public abstract void execute(Satellite satellite);
}

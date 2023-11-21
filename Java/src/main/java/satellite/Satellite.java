public class Satellite {
    private String orientation;
    private String solarPanels;
    private int dataCollected;

    public Satellite() {
        this.orientation = "North";
        this.solarPanels = "Inactive";
        this.dataCollected = 0;
    }

    public void applyAction(SatelliteAction action) {
        action.execute(this);
    }

    public String getOrientation() {
        return orientation;
    }

    public void setOrientation(String orientation) {
        this.orientation = orientation;
    }

    public String getSolarPanels() {
        return solarPanels;
    }

    public void setSolarPanels(String solarPanels) {
        this.solarPanels = solarPanels;
    }

    public int getDataCollected() {
        return dataCollected;
    }

    public void setDataCollected(int dataCollected) {
        this.dataCollected = dataCollected;
    }

    public String getState() {
        return "Orientation: " + orientation + ", Solar Panels: " + solarPanels + ", Data Collected: " + dataCollected;
    }
}

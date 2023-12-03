package utilities;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.MutableCapabilities;
import org.openqa.selenium.Platform;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebDriverException;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.firefox.FirefoxOptions;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.safari.SafariDriver;

import java.net.MalformedURLException;
import java.net.URL;

public class Driver {

    private static WebDriver driver;

    public static final String USERNAME = "kjazggul";
    public static final String ACCESS_KEY = "63e40331-66ce-48d0-bc20-5bb6b0470f2b";
    public static final String URL = "http://" + USERNAME + ":" + ACCESS_KEY + "@ondemand.saucelabs.com:80/wd/hub";

    private Driver() {

    }

    public static WebDriver getDriver() {

        if (driver == null) {

            switch (Config.getProperty("browser")) {
                case "chrome":
                    WebDriverManager.chromedriver().setup();
                    driver = new ChromeDriver();
                    break;
                case "firefox":
                    WebDriverManager.firefoxdriver().setup();
                    driver = new FirefoxDriver();
                    break;
                case "safari":
                    if (System.getProperty("os.name").toLowerCase().contains("windows")) {
                        throw new WebDriverException("Windows OS does not support safari");
                    }
                    WebDriverManager.getInstance(SafariDriver.class).setup();
                    driver = new SafariDriver();
                    break;
                case "remotechrome":
                    DesiredCapabilities capabilities = new DesiredCapabilities().chrome();
                    capabilities.setPlatform(Platform.ANY);
                    try {
                        driver = new RemoteWebDriver(new URL("http://localhost:4444/wd/hub"), capabilities);
                    }catch (MalformedURLException e){
                        e.printStackTrace();
                    }
                    break;

                case "saucelabWin":
                    DesiredCapabilities caps = DesiredCapabilities.chrome();
                    MutableCapabilities sauceOptions = new MutableCapabilities();


                    FirefoxOptions browserOptions = new FirefoxOptions();
                    browserOptions.setCapability("platformName", "Windows 7");
                    browserOptions.setCapability("sauce:options", sauceOptions);

                    try {

                        driver = new RemoteWebDriver(new URL(URL), caps);
                    }catch (MalformedURLException e) {
                        e.printStackTrace();
                        System.out.println("MalformedURLException not correct url provided");
                    }
                    break;
            }

            //driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
            driver.manage().window().maximize();

        }

        return driver;

    }

    public static void quitDriver() {
        if (driver != null) {
            driver.quit();
            driver = null;
        }
    }

}

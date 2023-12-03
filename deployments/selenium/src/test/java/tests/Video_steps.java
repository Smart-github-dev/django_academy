package tests;

import org.junit.Test;
import org.openqa.selenium.WebElement;
import pages.Login_page;
import pages.Video_page;
import utilities.Config;
import utilities.Driver;

import java.util.ArrayList;
import java.util.List;

public class Video_steps {

    Video_page video_page = new Video_page();

    Login_page login_page = new Login_page();

    @Test
    public void setUp() {
        Driver.getDriver().get(Config.getProperty("academyURL"));

        login_page.loginButton.click();
        login_page.usernameInputBox.sendKeys("username");
        login_page.passwordInputBox.sendKeys("Admin12345671");
        login_page.loginButton2.click();
    }


    @Test
    public void videoTest() throws Exception {
        Thread.sleep(2000);
        video_page.menuButton.click();
        Thread.sleep(2000);

        video_page.videoButton.click();
        int count = 0;
        Thread.sleep(2000);
        video_page.classes1.click();
        Thread.sleep(2000);
        video_page.videoOption1.click();
        Driver.getDriver().navigate().back();
        video_page.videoOption2.click();
        Driver.getDriver().navigate().back();
        video_page.videoOption3.click();
        Driver.getDriver().navigate().back();
        video_page.videoOption4.click();
        Driver.getDriver().navigate().back();
        Driver.getDriver().navigate().back();
      //  Driver.getDriver().navigate().back();

        video_page.classes2.click();
        // I haven't finished all of them.
        // We have to test all other video sub modules

    }


}

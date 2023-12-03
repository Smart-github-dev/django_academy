package tests;

import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.WebElement;
import pages.Chating_page;
import pages.Login_page;
import utilities.Config;
import utilities.Driver;

public class Chating_test {
    Chating_page chating_page = new Chating_page();
    Login_page login_page = new Login_page();


    @Test
    public void chating() throws Exception {
        Driver.getDriver().get(Config.getProperty("academyURL"));

        login_page.loginButton.click();
        login_page.usernameInputBox.sendKeys("username");
        login_page.passwordInputBox.sendKeys("Admin12345671");
        Thread.sleep(2000);
        login_page.loginButton2.click();
        Thread.sleep(2000);
        chating_page.menuButton.click();
        Thread.sleep(2000);
        chating_page.chatingButton.click();
        Thread.sleep(2000);
        chating_page.messageInputBox.sendKeys("hi everyone ");
        chating_page.sendButton.click();

        String actual = chating_page.message.getText();
        String expected = "hi everyone ";

        //Assert.assertEquals("Is not desplaied", actual,expected);
    }
}

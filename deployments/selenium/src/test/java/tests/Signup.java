package tests;

import com.github.javafaker.Faker;
import org.junit.Test;
import pages.Chating_page;
import pages.SignUp_page;
import utilities.Config;
import utilities.Driver;

public class Signup {
    SignUp_page signUp_page = new SignUp_page();
    Chating_page chating_page = new Chating_page();

    @Test
    public void setUp() throws Exception {
        Faker faker = new Faker();
        Driver.getDriver().get(Config.getProperty("academyURL"));
        signUp_page.signUpTodayButton.click();

        Thread.sleep(1000);
        signUp_page.firstNameInputBox.sendKeys(faker.name().firstName());
        Thread.sleep(1000);
        signUp_page.lastNameInputBox.sendKeys(faker.name().lastName());
        Thread.sleep(1000);
        signUp_page.usernameInputBox.sendKeys("username");
        Thread.sleep(1000);
        signUp_page.emailInputBox.sendKeys("username@gmail.com");
        signUp_page.passwordInputBox.sendKeys("Admin12345671");
        signUp_page.passwordRepeatInputBox.sendKeys("Admin12345671");
        signUp_page.signUpButton.click();

    }



}

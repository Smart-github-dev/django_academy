package pages;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import utilities.Driver;

import java.lang.reflect.Field;

public class Login_page {

    public Login_page() {
        PageFactory.initElements(Driver.getDriver(), this);
    }

    @FindBy(xpath = "(//div[@class='topnav']//a)[1]")
    public WebElement loginButton;

    @FindBy(xpath = "//input[@id='username']")
    public WebElement usernameInputBox;
    @FindBy(xpath = "//input[@id='password']")
    public WebElement passwordInputBox;

    @FindBy(xpath = "//input[@type='submit']")
    public WebElement loginButton2;
}

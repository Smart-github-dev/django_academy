package pages;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import utilities.Driver;

public class SignUp_page {

    public SignUp_page() {
        PageFactory.initElements(Driver.getDriver(), this);
    }

    @FindBy(id = "signup-btn")
    public WebElement signUpTodayButton;

    @FindBy(xpath = "//input[@id='firstname']")
    public WebElement firstNameInputBox;

    @FindBy(xpath = "//input[@id='lastname']")
    public WebElement lastNameInputBox;

    @FindBy(xpath = "//input[@id='username']")
    public WebElement usernameInputBox;
    @FindBy(xpath = "//input[@id='email']")
    public WebElement emailInputBox;
    @FindBy(xpath = "//input[@id='password']")
    public WebElement passwordInputBox;
    @FindBy(xpath = "//input[@id='confirm']")
    public WebElement passwordRepeatInputBox;
    @FindBy(xpath = "//button[@type='submit']")
    public WebElement signUpButton;


    @FindBy(xpath = "//input[@id='username']")
    public WebElement loginUsernameInput;

    @FindBy(xpath = "//input[@id='password']")
    public WebElement loginPasswordInputBox;


}

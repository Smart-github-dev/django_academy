package pages;

import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import utilities.Driver;

import java.util.List;

public class Video_page {

    public Video_page(){
        PageFactory.initElements(Driver.getDriver(), this);
    }
    @FindBy(xpath = "//span[@style='font-size:30px;cursor:pointer']")
    public WebElement menuButton;

    @FindBy(xpath = "(//div[@id='mySidenav']//a)[4]")
    public WebElement videoButton;

    @FindBy(xpath = "(//div[@class='vertical-menu'])[1]")
    public WebElement classes1;
    @FindBy(xpath = "(//div[@class='vertical-menu'])[1]")
    public WebElement classes2;
    @FindBy(xpath = "(//div[@class='vertical-menu'])[1]")
    public WebElement classes3;
    @FindBy(xpath = "(//div[@class='vertical-menu'])[1]")
    public WebElement classes4;
    @FindBy(xpath = "(//div[@class='vertical-menu'])[1]")
    public WebElement classes5;
    @FindBy(xpath = "(//div[@class='vertical-menu'])[1]")
    public WebElement classes6;


    @FindBy(xpath = "(//div[@class='vertical-menu'])[1]")
    public WebElement videoOption1;
    @FindBy(xpath = "(//div[@class='vertical-menu'])[2]")
    public WebElement videoOption2;
    @FindBy(xpath = "(//div[@class='vertical-menu'])[3]")
    public WebElement videoOption3;
    @FindBy(xpath = "(//div[@class='vertical-menu'])[4]")
    public WebElement videoOption4;
    @FindBy(xpath = "(//div[@class='vertical-menu'])[5]")
    public WebElement videoOption5;

}

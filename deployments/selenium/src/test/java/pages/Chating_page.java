package pages;

import org.apache.poi.hssf.record.chart.DatRecord;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import utilities.Driver;

public class Chating_page {
    public Chating_page(){
        PageFactory.initElements(Driver.getDriver(),this);

    }

    @FindBy(xpath = "//span[@style='font-size:30px;cursor:pointer']")
    public WebElement menuButton;

    @FindBy(xpath = "//div[@id='mySidenav']//a[3]")
    public WebElement chatingButton;
    @FindBy(xpath = "//input[@id='chat_text']")
    public WebElement messageInputBox;
    @FindBy(xpath = "//a[@id='chat_btn']")
    public WebElement sendButton;
    @FindBy(xpath = "(//div[@class='content']//p//br)[3]")
    public WebElement message;
}

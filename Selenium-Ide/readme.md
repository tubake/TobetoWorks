Selenium IDE Komutları(Commands)
Selenium IDE komutları, web tarayıcılarını otomatikleştirmek için kullanılır. Bu komutlar, web sayfalarında gezinmenizi, formları doldurmanızı ve diğer eylemleri gerçekleştirmenizi sağlar.

Selenium IDE, Selenium WebDriver'ın bir test otomasyon aracıdır ve bir tarayıcıda yapılan etkileşimleri kaydederek ve oynatarak test senaryoları oluşturmanıza olanak sağlar. İşte Selenium IDE'de kullanabileceğiniz temel komutlar:

open: Bir URL'yi ziyaret etmek için kullanılır.
Örnek: open | https://www.example.com

click: Belirtilen bir elemente tıklamak için kullanılır.
Örnek: click | id=buttonId

type: Bir input alanına metin girmek için kullanılır.
Örnek: type | id=inputField | Example Text

select: Bir dropdown menüden bir seçenek seçmek için kullanılır.
Örnek: select | id=dropdownId | label=Option

verifyText: Bir elementin metninin belirli bir metinle eşleşip eşleşmediğini doğrulamak için kullanılır.
Örnek: verifyText | id=elementId | Expected Text

verifyElementPresent: Bir elementin varlığını doğrulamak için kullanılır.
Örnek: verifyElementPresent | id=elementId

waitForElementPresent: Bir elementin belirli bir süre içinde görünmesini beklemek için kullanılır.
Örnek: waitForElementPresent | id=elementId | 5000 (5 saniye bekler)

store: Bir değeri depolamak için kullanılır.
Örnek: store | Example | variableName

echo: Bir mesajı konsola yazdırmak için kullanılır.
Örnek: echo | This is a message

pause: Belirli bir süre beklemek için kullanılır.
Örnek: pause | 3000 (3 saniye bekler)


Tabii, işte başka yaygın olarak kullanılan Selenium IDE komutları:

storeText: Bir elementin metnini almak ve depolamak için kullanılır.
Örnek: storeText | id=elementId | variableName

assertText: Bir elementin metninin belirli bir metinle eşleşip eşleşmediğini doğrulamak için kullanılır. Ancak, bu komut testin başarısız olmasına neden olur.
Örnek: assertText | id=elementId | Expected Text

waitForText: Bir elementin belirli bir metni içermesini beklemek için kullanılır.
Örnek: waitForText | id=elementId | Expected Text

assertElementPresent: Bir elementin var olup olmadığını doğrulamak için kullanılır. Ancak, bu komut testin başarısız olmasına neden olur.
Örnek: assertElementPresent | id=elementId

storeAttribute: Bir elementin belirli bir özniteliğini almak ve depolamak için kullanılır.
Örnek: storeAttribute | id=elementId@attributeName | variableName

mouseOver: Bir elementin üzerine fareyi getirmek için kullanılır.
Örnek: mouseOver | id=elementId

keyPress: Bir tuşa basmak için kullanılır.
Örnek: keyPress | id=elementId | \\13 (Enter tuşuna basar)

submit: Bir formu göndermek için kullanılır.
Örnek: submit | id=formId

runScript: JavaScript kodunu çalıştırmak için kullanılır.
Örnek: runScript | window.scrollBy(0, 100)

waitForPageToLoad: Sayfanın yüklenmesini beklemek için kullanılır.
Örnek: waitForPageToLoad | 5000 (5 saniye bekler)
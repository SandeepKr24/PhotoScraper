# PhotoScraper

This script creates a directory named 'images'.
Then subdirectories are created with the keyword they entered followed by the serial number of the images as its name, and the photos are downloaded into the respective subdirectories.

Requirements- 
You will need to have Selenium and a Chrome web driver installed on your computer/laptop for this.

1) Selenium-
The pip command is- 'pip install selenium'. I recommend you to visit the official documentation as well, you can try cool stuff with this magical module.

2) Chrome Web Driver-
https://chromedriver.chromium.org/downloads
You should first check your Chrome version.
You can do that by following the steps here-
  a) Launch Chrome.
  b) Click on the 3 Vertical Dots Image of 3 vertical dots in the upper right corner of the browser.
  c) Scroll down to and Hover over the Help option, then click on About Google Chrome in the new menu that opens.
  d) A new window appears that provides information about the browser. The version is located below the browser name.

#### NOTE: In line 71, the path of the output directory is set to my accordance. If you wish to use this code, you will have to change the first part of the path to the name of the directory you are storing this script. Eg- If you are naming your main directory as 'scraper' then the path should be 'scraper/images/{keyword}'.

Here's a short video showcasing this scraper-

https://github.com/SandeepKr24/PhotoScraper/assets/94790806/09884a47-17da-4dcb-bebd-739a88b9c4f5

Thank You for visiting. See you soon!

# Click-Go-Lotto

![A rounded triangle containing four lottery balls with numbers on each. At the bottom of the triangle is the phrase "Click-Go-Lotto."](static/images/click_go_lotto_gemini_generated.jpeg)

Get lottery numbers for Cash3, Cash4, Cash4Life, Fantasy Five, Mega Millions, Pick3, Pick4, Pick5, and Powerball with a
click of a button.

## About The Program

This web applications uses the Bootstrap on the Front-End and Python/Flask on the Back-End to display the website and
provide the random lottery numbers. Visitors can get a new set of numbers for a specific game by clicking on the button.

## Program Dependencies

A modern web browser (like Google Chrome) with JavaScript enabled.

## Website

[clickgolotto.com](https://clickgolotto.com/)

## Found A Bug? Need Help?

Please file a new issue using the Issues tab on the repo.

## Version History

* Latest release notes as of November 2025:
    - Refactored web scraping functions for Cash4Life, Mega Millions, and Powerball for improved reliability and efficiency.
    - Switched Cash4Life data source to Virginia Lottery API for more stable winning number retrieval.
    - Implemented user-agent headers and increased timeouts for web requests to mitigate blocking.
* Latest release notes as of April May:
    - Replaced some CSS rules with various Bootstrap ultilities.
    - Created main.js to contain the event handlers.
    - Added a spinner to the three National games that appears when the visitor generates a new set of numbers.
    - Added additional screen sizes of the mobile media queries.
* Latest release notes as of April 2025:
    - Removed the inline onclick event handler from all the HTML files.
* Latest release notes as of March 2025:
    - Created a base.html template
    - Extended the base.html template to all the html files in the project.
    - Added the latest winning lottery numbers for Cash4Life, Mega Millions, and Powerball.
* Latest release notes as of February 2025:
    - Updated the README.
* Latest release notes as of January 2025:
    - Updated the footer on all pages to display all my social media links.
* Latest release notes as of late December 2024:
    - Consolidated all the individual modules for each game into one module.
    - Added type annotations to all the functions and variables.
    - Added a gitignore file.
    - Updated the social media links in the index.html footer.
    - Fixed typos.
    - Removed unnecessary files from the repo.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

[Dominique Pizzie](https://gist.github.com/DomPizzie) for the simple README template.
# Instagram Engagement Rate Calculator

A complete open-source web scrapper for autonomous calculation of one's account's engagement rate.

## Technical Details

### Engagement Rate Formal Definition

Engagement rate is defined as the following:

$$
R=\frac{T+C}{F}
$$

where $T$ is the thumbs-up number, $C$ is the number of total comments and $F$ is the follower count.

### Backend

The website is powered with BeautifulSoup, Selenium and Flask.
Selenium serves as the core driver and utility for our web scrapper, whereas
BeautifulSoup comes in handy with analyzing the DOM. Finally, Flask is the
backend we use to display a practical user interface.

# Contributors

- raylee030: techlead, developer, SVN maintainer
- noobist-saiko: software architecture designer

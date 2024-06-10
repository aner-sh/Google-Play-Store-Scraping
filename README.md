# Google-Play-Store-Scraping
Google Play Store app scraping and how to bypass data restrictions legally + READY DATASET

--------------------------------------------------------------------------------------------------------------------------------

> [!IMPORTANT]
> `google-play-scraper` limits the number of apps returned per search to a of maximum 30 (as of 2024). Additionally, not all searches are guaranteed to yield this full amount. As a result of my need of a larger dataset than the ones available, I have come up with a solution that will bypass Google’s restrictions by utilizing the same features as other projects with google-play-scraper, but using a combination of different keywords and regions in order to enlarge the final volume of data. This iterative approach is easy to implement and adapt to your specific needs, and avoids the frustration in helplessly attempting to increase the data limit and receiving an exceeding error. The key benefit of this method is the ability to personalize your data collection and to extract a substantial amount for your projects without limitations. The purpose of sharing this approach is to promote knowledge exchange for educational purposes, not for financial gain or strategic advantage.

--------------------------------------------------------------------------------------------------------------------------------

##Installation
> [!NOTE]
> Exclamation mark might not be needed in some coding workspaces. I used Google Colab and an error was returned when absent.
```
!pip install google-play-scraper
```
##Code
> [!TIP]
> `google-play-scraper` is implemented in this code by using its `search()` feature and altering its aims to match mine. This specific code was used to extract data for classification and regression projects in Machine Learning, and so I naturally droped several attributes that didn't avail to me before forming a dataset. You are welcome to adjust this code to your project to match your academic needs. 

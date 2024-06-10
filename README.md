# Google-Play-Store-Scraping
Google Play Store app scraping and how to bypass data restrictions legally + READY DATASET

--------------------------------------------------------------------------------------------------------------------------------

> [!IMPORTANT]
> `google-play-scraper` limits the number of apps returned per search to a of maximum 30 (as of 2024). Additionally, not all searches are guaranteed to yield this full amount. As a result of my need of a larger dataset than the ones available, I have come up with a solution that will bypass Google’s restrictions by utilizing the same features as other projects with google-play-scraper, but using a combination of different keywords and regions in order to enlarge the final volume of data. This iterative approach is easy to implement and adapt to your specific needs, and avoids the frustration in helplessly attempting to increase the data limit and receiving an exceeding error. The key benefit of this method is the ability to personalize your data collection and to extract a substantial amount for your projects without limitations. The purpose of sharing this approach is to promote knowledge exchange for educational purposes, not for financial gain or strategic advantage.

--------------------------------------------------------------------------------------------------------------------------------

## Installation

> [!NOTE]
> Exclamation mark might not be needed in some coding workspaces. I used Google Colab and an error was returned when absent.
```
!pip install google-play-scraper
```
## [Code](google-play-scraper.py)

> [!TIP]
> `google-play-scraper` is implemented in this code by using its `search()` feature and altering its aims to match mine. This specific code was used to extract data for classification and regression projects in Machine Learning, and so I naturally droped several attributes that didn't avail to me before forming a dataset. You are welcome to adjust this code to your project to match your academic needs. 


### Imports
```
import pandas as pd
from google_play_scraper import app, search
```

### Main
```
def keywords():
    all_app_data = []
    unique_app_ids = set()
```

A variety of categories self chosen to make the search of apps for, feel free to change them according to your needs:
```
    words_list = ['books', 'pi digits', 'editors choice', 'memory', 'art', 'movie maker', 'photos', 'backup', 'adobe', 'music', 'finance', 'food', 'wellbeing', 'lifestyle', 'health', 'news', 'animals', 'productivity', 'travel', 'medical', 'shopping', 'streaming', 'social', 'design', 'kids', 'languages', 'education', 'sports', 'training', 'professional', 'beauty', 'utility', 'entertainment', 'lifestyle', 'taxi', 'messages', 'mobile', 'typing', 'coding', 'bakery', 'mission', 'farm', 'house', 'family', 'restaurant', 'money', 'managing', 'flight', 'train', 'car', 'race', 'website']
```
Two ending words to add to the category words, in order to enlarge the amount of outputs:
```
    endings = [" games", " apps", " new", " trending"]
```
United States, United Kingdom, Israel, Canada, Egypt, China. Any other country that is added will search all of the combinations in question and return the local leading apps in the region:
```
    countries = ["us", "uk", "il", "ca", "eg", "cn"]
```
> [!NOTE]
>Every search combination of categories in `words_list` combined with words in `endings` is ran for every single country in `countries`, so the leading apps returned after the search are most likely to differ and by this stragedy, we can surpass Google's scraping restrictions and extract more data!

### Rest Of The Function
```
    for a in words_list:
        for b in countries:
            for c in endings:
                keyword = a + c
                try:
                    result = search(keyword, lang="en", country=b, n_hits=30)
                    for app_info in result:
                        app_id = app_info['appId']
                        if app_id not in unique_app_ids:
                            app_data = app(app_id, lang="en", country=b)
                            all_app_data.append(app_data)
                            unique_app_ids.add(app_id)
                except Exception as e:
                    print(f"An error occurred while processing the keyword '{keyword}': {e}")

    return all_app_data
```

### Forming The Dataset

Call the keywords() function to start processing your list of keywords:
```
df_list = keywords()
```
Convert list of dictionaries to pandas DataFrame:
```
df = pd.DataFrame(df_list)
```
Drop unnecessary columns (**for a classification or regression project in Machine Learning I believe you won't need these attributes, but otherwise - feel free to delete this block of code)**:
```
df.drop(['minInstalls', 'sale', 'summary', 'privacyPolicy', 'saleTime', 'originalPrice', 'saleText', 'inAppProductPrice', 'developer', 'developerId', 'developer', 'developerEmail', 'developerWebsite', 'adSupported', 'developerAddress', 'genreId', 'headerImage', 'screenshots', 'video', 'videoImage', 'contentRatingDescription', 'updated', 'version', 'icon', 'categories', 'histogram', 'description', 'descriptionHTML', 'comments', 'appId', 'url'], axis=1, inplace=True)
```
Reset index and call the dataframe:
```
df.reset_index(drop=True, inplace=True)  
df
```

## Ready Dataset After Scraping 
The results of my `keywords()` combinations stored as a `CSV file` can be found [here](GooglePlayData.csv).



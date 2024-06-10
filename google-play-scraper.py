!pip install google-play-scraper

import pandas as pd
from google_play_scraper import app, search

def keywords():
    all_app_data = []
    unique_app_ids = set()

    # A variety of categories self chosen to make the search of apps for, feel free to change them according to your needs
    words_list = ['books', 'pi digits', 'editors choice', 'memory', 'art', 'movie maker', 'photos', 'backup', 'adobe', 'music', 'finance', 'food', 'wellbeing', 'lifestyle', 'health', 'news', 'animals', 'productivity', 'travel', 'medical', 'shopping', 'streaming', 'social', 'design', 'kids', 'languages', 'education', 'sports', 'training', 'professional', 'beauty', 'utility', 'entertainment', 'lifestyle', 'taxi', 'messages', 'mobile', 'typing', 'coding', 'bakery', 'mission', 'farm', 'house', 'family', 'restaurant', 'money', 'managing', 'flight', 'train', 'car', 'race', 'website']
    endings = [" games", " apps", " new", " trending"] # Two ending words to add to the category words, in order to enlarge the amount of outputs
    countries = ["us", "uk", "il", "ca", "eg", "cn"] # United States, United Kingdom, Israel, Canada, Egypt, China. Any other country that is added will search all of the combinations in question and return the local leading apps in the region
    # Every search combination of categories in {words_list} combined with words in {endings} is ran for every single country in {countries}, so the leading apps returned after the search are most likely to differ and by this stragedy, we can surpass Google's scraping restrictions and extract more data!

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

# Call the keywords() function to start processing your list of keywords
df_list = keywords()

# Convert list of dictionaries to pandas DataFrame
df = pd.DataFrame(df_list)

# Drop unnecessary columns (for a classification project I believe you won't need these attributes, but otherwise - feel free to delete this block of code)
df.drop(['minInstalls', 'sale', 'summary', 'privacyPolicy', 'saleTime', 'originalPrice', 'saleText', 'inAppProductPrice', 'developer', 'developerId', 'developer', 'developerEmail', 'developerWebsite', 'adSupported', 'developerAddress', 'genreId', 'headerImage', 'screenshots', 'video', 'videoImage', 'contentRatingDescription', 'updated', 'version', 'icon', 'categories', 'histogram', 'description', 'descriptionHTML', 'comments', 'appId', 'url'], axis=1, inplace=True)

# Reset index
df.reset_index(drop=True, inplace=True)  

df

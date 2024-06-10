!pip install google-play-scraper

import pandas as pd
from google_play_scraper import app, search

def keywords():
    all_app_data = []
    unique_app_ids = set()
    words_list = ['books', 'pi digits', 'editors choice', 'memory', 'art', 'movie maker', 'photos', 'backup', 'adobe', 'music', 'finance', 'food', 'wellbeing', 'lifestyle', 'health', 'news', 'animals', 'productivity', 'travel', 'medical', 'shopping', 'streaming', 'social', 'design', 'kids', 'languages', 'education', 'sports', 'training', 'professional', 'beauty', 'utility', 'entertainment', 'lifestyle', 'taxi', 'messages', 'mobile', 'typing', 'coding', 'bakery', 'mission', 'farm', 'house', 'family', 'restaurant', 'money', 'managing', 'flight', 'train', 'car', 'race', 'website']
    endings = [" games", " apps", " new", " trending"] 
    countries = ["us", "uk", "il", "ca", "eg", "cn"]

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

df_list = keywords()
df = pd.DataFrame(df_list)
df.drop(['minInstalls', 'sale', 'summary', 'privacyPolicy', 'saleTime', 'originalPrice', 'saleText', 'inAppProductPrice', 'developer', 'developerId', 'developer', 'developerEmail', 'developerWebsite', 'adSupported', 'developerAddress', 'genreId', 'headerImage', 'screenshots', 'video', 'videoImage', 'contentRatingDescription', 'updated', 'version', 'icon', 'categories', 'histogram', 'description', 'descriptionHTML', 'comments', 'appId', 'url'], axis=1, inplace=True)
df.reset_index(drop=True, inplace=True)  
df

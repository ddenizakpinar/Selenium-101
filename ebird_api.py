import os
from ebird.api import get_taxonomy, get_taxonomy_forms, get_taxonomy_versions
from dotenv import load_dotenv


def get_bird_name():

    load_dotenv()
    API_KEY = os.getenv('API_KEY')
    taxonomy = get_taxonomy(API_KEY)

    prev_name = ''
    bird_list = []

    for bird in taxonomy:
        name = ''
        try:
            name = bird['familyComName']
            try:
                name = name.split(' ')[-1]
            except:
                pass
            try:
                name = name.split('-')[-1]
            except:
                pass
            try:
                name = name.split(',')[-1]
            except:
                pass
            if name[-1] == 's':
                name = name[:-1]
            if prev_name != name:
                prev_name = name
                bird_list.append(name)
        except:
            pass

    return bird_list


import pyyoutube as yt
def get_yt_link(autor, utwor):
    api = yt.Api(api_key='W tym miejscu jest potrzebny klucz wygenerowany z google')
    r = api.search_by_keywords(q=f"{autor} {utwor}", search_type=['video'], count=1, limit=1)
    if not r.items: return 'https://youtu.be/dQw4w9WgXcQ'
    r=r.to_dict().get('items')[0].get('id').get('videoId')
    return f'https://youtu.be/{r}'
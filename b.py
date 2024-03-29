import requests

# url = 'https://codeforces.com/contest/1950/submission/253744351'

    
def check(url):
    response = requests.get(url)
    # print(response.text)
    task = 'E - Nearly Shortest Repeating Substring'
    programminglang = 'c++'
    nooo = '#ifndef'
    noooooo = '#ifdef'
    if programminglang in response.text.lower() and nooo not in response.text.lower() and noooooo not in response.text.lower():
        return True
    return False 



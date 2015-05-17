import mechanize
import cookielib
import pandas as pd
import matplotlib.pyplot as plt

class gtrends:
    front_daily_url = "http://www.google.com/trends/trendsReport?hl=en-US&tz=&q="
    back_daily_url = "&date=today%203-m&cmpt=q&export=1"

    front_weekly_url = "http://www.google.com/trends/trendsReport?q="
    back_weekly_url = "&export=1"

    def __init__(self, username, password):
        self.br = mechanize.Browser()

        self.br.set_handle_robots(False)

        self.cj = cookielib.LWPCookieJar()
        self.br.set_cookiejar(self.cj)
        self.br.addheaders = [('User-agent', "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36")]
        response = self.br.open('https://accounts.google.com/ServiceLogin?hl=en&continue=https://www.google.com/')
        forms = mechanize.ParseResponse(response)
        form = forms[0]
        form['Email'] = username
        form['Passwd'] = password
        response = self.br.open(form.click())

    def build_query(self, terms = [], daily = True):
        if daily == True:
            front_url = gtrends.front_daily_url
            back_url = gtrends.back_daily_url
        else:
            front_url = gtrends.front_weekly_url
            back_url = gtrends.back_weekly_url

        query = ""
        for term in terms:
            term = term.replace(" ", "+")
            query += term + ","
            url = front_url + query + back_url
        return url

    def build_result(self, url):
        Result = self.br.open(url)
        xs = Result.read().split('\n')
        proto = []
        i = 4
        while xs[i] != "":
            line = xs[i].split(",")
            if line[1] != "":
                proto.append(line)
            i += 1
        df = pd.DataFrame(proto[1:])
        df.columns = proto[0]
        df.inex = df.ix[:,0]
        del df[df.columns[0]]
        df = df.convert_objects(convert_numeric=True)
        return df

    def get_volume(self, terms=[], daily=True):
        url = self.build_query(terms, daily = daily)
        df = self.build_result(url)
        return df


# Collect data thusly:
# gt = gtrends(<username>, <password>)
vol = gt.get_volume(terms = ["iphone", "ipad"])
print vol
# vol2 = gt.get_volume(terms = ["iphone", "ipad"], daily = False)
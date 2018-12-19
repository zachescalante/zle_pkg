import re


class DateToken():

    def __init__(self):

        self.months = "january|february|march|april|may|june|july|august"\
                      "|september|october|november|december|jan|feb|mar|may"\
                      "|jun|jul|aug|sep|sept|oct|nov|dec"

    def us_month(self, date_string):

        date_string = date_string.lower()

        month_backslash = re.compile(r'\s+\d{1,2}/', re.IGNORECASE)
        month_dash = re.compile(r'\s+\d{1,2}-', re.IGNORECASE)
        month_name = re.compile(self.months)

        if re.search(r'\d{1,2}/\d{1,2}/\d{2,4}', date_string):
            date_string = month_backslash.sub(' <month> ', date_string)

        if re.search(r'\d{1,2}-\d{1,2}-\d{2,4}', date_string):
            date_string = month_dash.sub(' <month> ', date_string)

        if re.search('(' + self.months + ')', date_string):
            date_string = month_name.sub(' <month> ', date_string)

        return date_string
    
    def us_day(self, date_string):

        date_string = date_string.lower()

        day_backslash = re.compile(r'/\d{1,2}/', re.IGNORECASE)
        day_dash = re.compile(r'-\d{1,2}-', re.IGNORECASE)
        day_name = re.compile(r'\s*\d+(st|nd|rd|th)')

        if re.search(r'\d{1,2}/\d{1,2}/\d{2,4}', date_string):
            date_string = day_backslash.sub(' <day> ', date_string)

        if re.search(r'\d{1,2}-\d{1,2}-\d{2,4}', date_string):
            date_string = day_dash.sub(' <day> ', date_string)

        if re.search('(' + self.months + ')' + '\s*\d+(st|nd|rd|th)', date_string):
            date_string = day_name.sub(' <day> ', date_string)

        return date_string

    def us_year(self, date_string):

        date_string = date_string.lower()

        year_backslash = re.compile(r'/\d{2,4}(?!\/)', re.IGNORECASE)
        year_dash = re.compile(r'-\d{2,4}(?!-)', re.IGNORECASE)
        year_name = re.compile(r'\d{2,4}')

        if re.search(r'\d{1,2}/\d{1,2}/\d{2,4}', date_string):
            date_string = year_backslash.sub(' <year> ', date_string)

        if re.search(r'\d{1,2}-\d{1,2}-\d{2,4}', date_string):
            date_string = year_dash.sub(' <year> ', date_string)

        if re.search('(' + self.months + ')' + '\s*\d+(st|nd|rd|th)(,|.)\s*\d{2,4}', date_string):
            date_string = year_name.sub(' <year> ', date_string)

        return date_string

    def us_date(self, date_string):

        date_string = date_string.lower()

        date_backslash = re.compile(r'\d{1,2}/\d{1,2}/\d{2,4}', re.IGNORECASE)
        date_dash = re.compile(r'\d{1,2}-\d{1,2}-\d{2,4}', re.IGNORECASE)
        date_name = re.compile(r'(' + self.months + ')' + '\s*\d+(st|nd|rd|th)(,|.)\s*\d{2,4}')

        if re.search(r'\d{1,2}/\d{1,2}/\d{2,4}', date_string):
            date_string = date_backslash.sub(' <date> ', date_string)

        if re.search(r'\d{1,2}-\d{1,2}-\d{2,4}', date_string):
            date_string = date_dash.sub(' <date> ', date_string)

        if re.search('(' + self.months + ')' + '\s*\d+(st|nd|rd|th)(,|.)\s*\d{2,4}', date_string):
            date_string = date_name.sub(' <date> ', date_string)

        return date_string


if __name__ == '__main__':
    main()
    
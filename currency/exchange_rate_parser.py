import html.parser


class ExchangeRateParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_result_span = False
        self.exchange_rate = None

    def handle_starttag(self, tag, attrs):
        if tag == 'span' and attrs and ('class', 'uccResultAmount') in attrs:
            self.in_result_span = True

    def handle_data(self, data):
        if self.in_result_span:
            self.exchange_rate = data.strip()
            self.in_result_span = False
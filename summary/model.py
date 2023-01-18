# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = Model_YahooFinQuery1_from_dict(json.loads(json_string))

from typing import Optional, Any, List, TypeVar, Callable, Type, cast

T = TypeVar("T")


def from_str(x: Any) -> str:
    # assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    if x is None:
        return 0.0
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_int(x: Any) -> int:
    # assert isinstance(x, (int, float))  # and not isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Result:
    language: str
    region: str
    quote_type: str
    type_disp: str
    quote_source_name: str
    triggerable: bool
    custom_price_alert_confidence: str
    currency: str
    market_state: str
    exchange: str
    short_name: str
    exchange_timezone_name: str
    exchange_timezone_short_name: str
    regular_market_change_percent: float
    regular_market_price: float
    esg_populated: bool
    long_name: str
    gmt_off_set_milliseconds: int
    message_board_id: str
    market: str
    first_trade_date_milliseconds: int
    price_hint: int
    regular_market_change: float
    regular_market_time: int
    regular_market_day_high: float
    regular_market_day_range: str
    regular_market_day_low: float
    regular_market_volume: int
    regular_market_previous_close: float
    bid: int
    ask: int
    bid_size: int
    ask_size: int
    full_exchange_name: str
    financial_currency: str
    regular_market_open: float
    average_daily_volume3_month: int
    average_daily_volume10_day: int
    fifty_two_week_low_change: float
    fifty_two_week_low_change_percent: float
    fifty_two_week_range: str
    fifty_two_week_high_change: float
    fifty_two_week_high_change_percent: float
    fifty_two_week_low: float
    fifty_two_week_high: float
    earnings_timestamp: int
    earnings_timestamp_start: int
    earnings_timestamp_end: int
    trailing_annual_dividend_rate: int
    trailing_annual_dividend_yield: int
    eps_trailing_twelve_months: float
    shares_outstanding: int
    book_value: float
    fifty_day_average: float
    fifty_day_average_change: float
    fifty_day_average_change_percent: float
    two_hundred_day_average: float
    two_hundred_day_average_change: float
    two_hundred_day_average_change_percent: float
    market_cap: int
    price_to_book: float
    source_interval: int
    exchange_data_delayed_by: int
    tradeable: bool
    crypto_tradeable: bool
    symbol: str
    trailing_pe: Optional[float]
    eps_forward: Optional[float]
    eps_current_year: Optional[float]
    price_eps_current_year: Optional[float]
    forward_pe: Optional[float]
    average_analyst_rating: Optional[str]

    def __init__(self, language: str, region: str, quote_type: str, type_disp: str, quote_source_name: str,
                 triggerable: bool, custom_price_alert_confidence: str, currency: str, market_state: str, exchange: str,
                 short_name: str, exchange_timezone_name: str, exchange_timezone_short_name: str,
                 regular_market_change_percent: float, regular_market_price: float, esg_populated: bool, long_name: str,
                 gmt_off_set_milliseconds: int, message_board_id: str, market: str, first_trade_date_milliseconds: int,
                 price_hint: int, regular_market_change: float, regular_market_time: int,
                 regular_market_day_high: float, regular_market_day_range: str, regular_market_day_low: float,
                 regular_market_volume: int, regular_market_previous_close: float, bid: int, ask: int, bid_size: int,
                 ask_size: int, full_exchange_name: str, financial_currency: str, regular_market_open: float,
                 average_daily_volume3_month: int, average_daily_volume10_day: int, fifty_two_week_low_change: float,
                 fifty_two_week_low_change_percent: float, fifty_two_week_range: str, fifty_two_week_high_change: float,
                 fifty_two_week_high_change_percent: float, fifty_two_week_low: float, fifty_two_week_high: float,
                 earnings_timestamp: int, earnings_timestamp_start: int, earnings_timestamp_end: int,
                 trailing_annual_dividend_rate: int, trailing_annual_dividend_yield: int,
                 eps_trailing_twelve_months: float, shares_outstanding: int, book_value: float,
                 fifty_day_average: float, fifty_day_average_change: float, fifty_day_average_change_percent: float,
                 two_hundred_day_average: float, two_hundred_day_average_change: float,
                 two_hundred_day_average_change_percent: float, market_cap: int, price_to_book: float,
                 source_interval: int, exchange_data_delayed_by: int, tradeable: bool, crypto_tradeable: bool,
                 symbol: str, trailing_pe: Optional[float], eps_forward: Optional[float],
                 eps_current_year: Optional[float], price_eps_current_year: Optional[float],
                 forward_pe: Optional[float], average_analyst_rating: Optional[str]) -> None:
        self.language = language
        self.region = region
        self.quote_type = quote_type
        self.type_disp = type_disp
        self.quote_source_name = quote_source_name
        self.triggerable = triggerable
        self.custom_price_alert_confidence = custom_price_alert_confidence
        self.currency = currency
        self.market_state = market_state
        self.exchange = exchange
        self.short_name = short_name
        self.exchange_timezone_name = exchange_timezone_name
        self.exchange_timezone_short_name = exchange_timezone_short_name
        self.regular_market_change_percent = regular_market_change_percent
        self.regular_market_price = regular_market_price
        self.esg_populated = esg_populated
        self.long_name = long_name
        self.gmt_off_set_milliseconds = gmt_off_set_milliseconds
        self.message_board_id = message_board_id
        self.market = market
        self.first_trade_date_milliseconds = first_trade_date_milliseconds
        self.price_hint = price_hint
        self.regular_market_change = regular_market_change
        self.regular_market_time = regular_market_time
        self.regular_market_day_high = regular_market_day_high
        self.regular_market_day_range = regular_market_day_range
        self.regular_market_day_low = regular_market_day_low
        self.regular_market_volume = regular_market_volume
        self.regular_market_previous_close = regular_market_previous_close
        self.bid = bid
        self.ask = ask
        self.bid_size = bid_size
        self.ask_size = ask_size
        self.full_exchange_name = full_exchange_name
        self.financial_currency = financial_currency
        self.regular_market_open = regular_market_open
        self.average_daily_volume3_month = average_daily_volume3_month
        self.average_daily_volume10_day = average_daily_volume10_day
        self.fifty_two_week_low_change = fifty_two_week_low_change
        self.fifty_two_week_low_change_percent = fifty_two_week_low_change_percent
        self.fifty_two_week_range = fifty_two_week_range
        self.fifty_two_week_high_change = fifty_two_week_high_change
        self.fifty_two_week_high_change_percent = fifty_two_week_high_change_percent
        self.fifty_two_week_low = fifty_two_week_low
        self.fifty_two_week_high = fifty_two_week_high
        self.earnings_timestamp = earnings_timestamp
        self.earnings_timestamp_start = earnings_timestamp_start
        self.earnings_timestamp_end = earnings_timestamp_end
        self.trailing_annual_dividend_rate = trailing_annual_dividend_rate
        self.trailing_annual_dividend_yield = trailing_annual_dividend_yield
        self.eps_trailing_twelve_months = eps_trailing_twelve_months
        self.shares_outstanding = shares_outstanding
        self.book_value = book_value
        self.fifty_day_average = fifty_day_average
        self.fifty_day_average_change = fifty_day_average_change
        self.fifty_day_average_change_percent = fifty_day_average_change_percent
        self.two_hundred_day_average = two_hundred_day_average
        self.two_hundred_day_average_change = two_hundred_day_average_change
        self.two_hundred_day_average_change_percent = two_hundred_day_average_change_percent
        self.market_cap = market_cap
        self.price_to_book = price_to_book
        self.source_interval = source_interval
        self.exchange_data_delayed_by = exchange_data_delayed_by
        self.tradeable = tradeable
        self.crypto_tradeable = crypto_tradeable
        self.symbol = symbol
        self.trailing_pe = trailing_pe
        self.eps_forward = eps_forward
        self.eps_current_year = eps_current_year
        self.price_eps_current_year = price_eps_current_year
        self.forward_pe = forward_pe
        self.average_analyst_rating = average_analyst_rating

    @staticmethod
    def from_dict(obj: Any) -> 'Result':
        assert isinstance(obj, dict)
        language = from_str(obj.get("language"))
        region = from_str(obj.get("region"))
        quote_type = from_str(obj.get("quoteType"))
        type_disp = from_str(obj.get("typeDisp"))
        quote_source_name = from_str(obj.get("quoteSourceName"))
        triggerable = from_bool(obj.get("triggerable"))
        custom_price_alert_confidence = from_str(obj.get("customPriceAlertConfidence"))
        currency = from_str(obj.get("currency"))
        market_state = from_str(obj.get("marketState"))
        exchange = from_str(obj.get("exchange"))
        short_name = from_str(obj.get("shortName"))
        exchange_timezone_name = from_str(obj.get("exchangeTimezoneName"))
        exchange_timezone_short_name = from_str(obj.get("exchangeTimezoneShortName"))
        regular_market_change_percent = from_float(obj.get("regularMarketChangePercent"))
        regular_market_price = from_float(obj.get("regularMarketPrice"))
        esg_populated = from_bool(obj.get("esgPopulated"))
        long_name = from_str(obj.get("longName"))
        gmt_off_set_milliseconds = from_int(obj.get("gmtOffSetMilliseconds"))
        message_board_id = obj.get("messageBoardId")
        market = from_str(obj.get("market"))
        first_trade_date_milliseconds = from_int(obj.get("firstTradeDateMilliseconds"))
        price_hint = from_int(obj.get("priceHint"))
        regular_market_change = from_float(obj.get("regularMarketChange"))
        regular_market_time = from_int(obj.get("regularMarketTime"))
        regular_market_day_high = from_float(obj.get("regularMarketDayHigh"))
        regular_market_day_range = from_str(obj.get("regularMarketDayRange"))
        regular_market_day_low = from_float(obj.get("regularMarketDayLow"))
        regular_market_volume = from_int(obj.get("regularMarketVolume"))
        regular_market_previous_close = from_float(obj.get("regularMarketPreviousClose"))
        bid = from_int(obj.get("bid"))
        ask = from_int(obj.get("ask"))
        bid_size = from_int(obj.get("bidSize"))
        ask_size = from_int(obj.get("askSize"))
        full_exchange_name = from_str(obj.get("fullExchangeName"))
        financial_currency = from_str(obj.get("financialCurrency"))
        regular_market_open = from_float(obj.get("regularMarketOpen"))
        average_daily_volume3_month = from_int(obj.get("averageDailyVolume3Month"))
        average_daily_volume10_day = from_int(obj.get("averageDailyVolume10Day"))
        fifty_two_week_low_change = from_float(obj.get("fiftyTwoWeekLowChange"))
        fifty_two_week_low_change_percent = from_float(obj.get("fiftyTwoWeekLowChangePercent"))
        fifty_two_week_range = from_str(obj.get("fiftyTwoWeekRange"))
        fifty_two_week_high_change = from_float(obj.get("fiftyTwoWeekHighChange"))
        fifty_two_week_high_change_percent = from_float(obj.get("fiftyTwoWeekHighChangePercent"))
        fifty_two_week_low = from_float(obj.get("fiftyTwoWeekLow"))
        fifty_two_week_high = from_float(obj.get("fiftyTwoWeekHigh"))
        earnings_timestamp = from_int(obj.get("earningsTimestamp"))
        earnings_timestamp_start = from_int(obj.get("earningsTimestampStart"))
        earnings_timestamp_end = from_int(obj.get("earningsTimestampEnd"))
        trailing_annual_dividend_rate = from_int(obj.get("trailingAnnualDividendRate"))
        trailing_annual_dividend_yield = from_int(obj.get("trailingAnnualDividendYield"))
        eps_trailing_twelve_months = (obj.get("epsTrailingTwelveMonths"))
        shares_outstanding = from_int(obj.get("sharesOutstanding"))
        book_value = from_float(obj.get("bookValue")) if obj.get("bookValue") is not None else 0
        fifty_day_average = from_float(obj.get("fiftyDayAverage"))  # if obj.get("fiftyDayAverage") is not None else 0
        fifty_day_average_change = from_float(obj.get("fiftyDayAverageChange"))
        fifty_day_average_change_percent = from_float(obj.get("fiftyDayAverageChangePercent"))
        two_hundred_day_average = from_float(obj.get("twoHundredDayAverage"))
        two_hundred_day_average_change = from_float(obj.get("twoHundredDayAverageChange"))
        two_hundred_day_average_change_percent = from_float(obj.get("twoHundredDayAverageChangePercent"))
        market_cap = from_int(obj.get("marketCap"))
        price_to_book = from_float(obj.get("priceToBook")) if obj.get("priceToBook") is not None else 0
        source_interval = from_int(obj.get("sourceInterval"))
        exchange_data_delayed_by = from_int(obj.get("exchangeDataDelayedBy"))
        tradeable = from_bool(obj.get("tradeable"))
        crypto_tradeable = from_bool(obj.get("cryptoTradeable"))
        symbol = from_str(obj.get("symbol"))
        trailing_pe = from_union([from_float, from_none], obj.get("trailingPE"))
        eps_forward = from_union([from_float, from_none], obj.get("epsForward"))
        eps_current_year = from_union([from_float, from_none], obj.get("epsCurrentYear"))
        price_eps_current_year = from_union([from_float, from_none], obj.get("priceEpsCurrentYear"))
        forward_pe = from_union([from_float, from_none], obj.get("forwardPE"))
        average_analyst_rating = from_union([from_str, from_none], obj.get("averageAnalystRating"))
        return Result(language, region, quote_type, type_disp, quote_source_name, triggerable,
                      custom_price_alert_confidence, currency, market_state, exchange, short_name,
                      exchange_timezone_name, exchange_timezone_short_name, regular_market_change_percent,
                      regular_market_price, esg_populated, long_name, gmt_off_set_milliseconds, message_board_id,
                      market, first_trade_date_milliseconds, price_hint, regular_market_change, regular_market_time,
                      regular_market_day_high, regular_market_day_range, regular_market_day_low, regular_market_volume,
                      regular_market_previous_close, bid, ask, bid_size, ask_size, full_exchange_name,
                      financial_currency, regular_market_open, average_daily_volume3_month, average_daily_volume10_day,
                      fifty_two_week_low_change, fifty_two_week_low_change_percent, fifty_two_week_range,
                      fifty_two_week_high_change, fifty_two_week_high_change_percent, fifty_two_week_low,
                      fifty_two_week_high, earnings_timestamp, earnings_timestamp_start, earnings_timestamp_end,
                      trailing_annual_dividend_rate, trailing_annual_dividend_yield, eps_trailing_twelve_months,
                      shares_outstanding, book_value, fifty_day_average, fifty_day_average_change,
                      fifty_day_average_change_percent, two_hundred_day_average, two_hundred_day_average_change,
                      two_hundred_day_average_change_percent, market_cap, price_to_book, source_interval,
                      exchange_data_delayed_by, tradeable, crypto_tradeable, symbol, trailing_pe, eps_forward,
                      eps_current_year, price_eps_current_year, forward_pe, average_analyst_rating)

    def to_dict(self) -> dict:
        result: dict = {}
        result["language"] = from_str(self.language)
        result["region"] = from_str(self.region)
        result["quoteType"] = from_str(self.quote_type)
        result["typeDisp"] = from_str(self.type_disp)
        result["quoteSourceName"] = from_str(self.quote_source_name)
        result["triggerable"] = from_bool(self.triggerable)
        result["customPriceAlertConfidence"] = from_str(self.custom_price_alert_confidence)
        result["currency"] = from_str(self.currency)
        result["marketState"] = from_str(self.market_state)
        result["exchange"] = from_str(self.exchange)
        result["shortName"] = from_str(self.short_name)
        result["exchangeTimezoneName"] = from_str(self.exchange_timezone_name)
        result["exchangeTimezoneShortName"] = from_str(self.exchange_timezone_short_name)
        result["regularMarketChangePercent"] = to_float(self.regular_market_change_percent)
        result["regularMarketPrice"] = to_float(self.regular_market_price)
        result["esgPopulated"] = from_bool(self.esg_populated)
        result["longName"] = from_str(self.long_name)
        result["gmtOffSetMilliseconds"] = from_int(self.gmt_off_set_milliseconds)
        result["messageBoardId"] = from_str(self.message_board_id)
        result["market"] = from_str(self.market)
        result["firstTradeDateMilliseconds"] = from_int(self.first_trade_date_milliseconds)
        result["priceHint"] = from_int(self.price_hint)
        result["regularMarketChange"] = to_float(self.regular_market_change)
        result["regularMarketTime"] = from_int(self.regular_market_time)
        result["regularMarketDayHigh"] = to_float(self.regular_market_day_high)
        result["regularMarketDayRange"] = from_str(self.regular_market_day_range)
        result["regularMarketDayLow"] = to_float(self.regular_market_day_low)
        result["regularMarketVolume"] = from_int(self.regular_market_volume)
        result["regularMarketPreviousClose"] = to_float(self.regular_market_previous_close)
        result["bid"] = from_int(self.bid)
        result["ask"] = from_int(self.ask)
        result["bidSize"] = from_int(self.bid_size)
        result["askSize"] = from_int(self.ask_size)
        result["fullExchangeName"] = from_str(self.full_exchange_name)
        result["financialCurrency"] = from_str(self.financial_currency)
        result["regularMarketOpen"] = to_float(self.regular_market_open)
        result["averageDailyVolume3Month"] = from_int(self.average_daily_volume3_month)
        result["averageDailyVolume10Day"] = from_int(self.average_daily_volume10_day)
        result["fiftyTwoWeekLowChange"] = to_float(self.fifty_two_week_low_change)
        result["fiftyTwoWeekLowChangePercent"] = to_float(self.fifty_two_week_low_change_percent)
        result["fiftyTwoWeekRange"] = from_str(self.fifty_two_week_range)
        result["fiftyTwoWeekHighChange"] = to_float(self.fifty_two_week_high_change)
        result["fiftyTwoWeekHighChangePercent"] = to_float(self.fifty_two_week_high_change_percent)
        result["fiftyTwoWeekLow"] = to_float(self.fifty_two_week_low)
        result["fiftyTwoWeekHigh"] = to_float(self.fifty_two_week_high)
        result["earningsTimestamp"] = from_int(self.earnings_timestamp)
        result["earningsTimestampStart"] = from_int(self.earnings_timestamp_start)
        result["earningsTimestampEnd"] = from_int(self.earnings_timestamp_end)
        result["trailingAnnualDividendRate"] = from_int(self.trailing_annual_dividend_rate)
        result["trailingAnnualDividendYield"] = from_int(self.trailing_annual_dividend_yield)
        result["epsTrailingTwelveMonths"] = to_float(self.eps_trailing_twelve_months)
        result["sharesOutstanding"] = from_int(self.shares_outstanding)
        result["bookValue"] = to_float(self.book_value)
        result["fiftyDayAverage"] = to_float(self.fifty_day_average)
        result["fiftyDayAverageChange"] = to_float(self.fifty_day_average_change)
        result["fiftyDayAverageChangePercent"] = to_float(self.fifty_day_average_change_percent)
        result["twoHundredDayAverage"] = to_float(self.two_hundred_day_average)
        result["twoHundredDayAverageChange"] = to_float(self.two_hundred_day_average_change)
        result["twoHundredDayAverageChangePercent"] = to_float(self.two_hundred_day_average_change_percent)
        result["marketCap"] = from_int(self.market_cap)
        result["priceToBook"] = to_float(self.price_to_book)
        result["sourceInterval"] = from_int(self.source_interval)
        result["exchangeDataDelayedBy"] = from_int(self.exchange_data_delayed_by)
        result["tradeable"] = from_bool(self.tradeable)
        result["cryptoTradeable"] = from_bool(self.crypto_tradeable)
        result["symbol"] = from_str(self.symbol)
        result["trailingPE"] = from_union([to_float, from_none], self.trailing_pe)
        result["epsForward"] = from_union([to_float, from_none], self.eps_forward)
        result["epsCurrentYear"] = from_union([to_float, from_none], self.eps_current_year)
        result["priceEpsCurrentYear"] = from_union([to_float, from_none], self.price_eps_current_year)
        result["forwardPE"] = from_union([to_float, from_none], self.forward_pe)
        result["averageAnalystRating"] = from_union([from_str, from_none], self.average_analyst_rating)
        return result


class QuoteResponse:
    result: List[Result]
    error: None

    def __init__(self, result: List[Result], error: None) -> None:
        self.result = result
        self.error = error

    @staticmethod
    def from_dict(obj: Any) -> 'QuoteResponse':
        assert isinstance(obj, dict)
        result = from_list(Result.from_dict, obj.get("result"))
        error = from_none(obj.get("error"))
        return QuoteResponse(result, error)

    def to_dict(self) -> dict:
        result: dict = {}
        result["result"] = from_list(lambda x: to_class(Result, x), self.result)
        result["error"] = from_none(self.error)
        return result


class Model_YahooFinQuery1:
    quote_response: QuoteResponse

    def __init__(self, quote_response: QuoteResponse) -> None:
        self.quote_response = quote_response

    @staticmethod
    def from_dict(obj: Any) -> 'Model_YahooFinQuery1':
        assert isinstance(obj, dict)
        quote_response = QuoteResponse.from_dict(obj.get("quoteResponse"))
        return Model_YahooFinQuery1(quote_response)

    def to_dict(self) -> dict:
        result: dict = {"quoteResponse": to_class(QuoteResponse, self.quote_response)}
        return result


def Model_YahooFinQuery1_from_dict(s: Any) -> Model_YahooFinQuery1:
    return Model_YahooFinQuery1.from_dict(s)


def Model_YahooFinQuery1_to_dict(x: Model_YahooFinQuery1) -> Any:
    return to_class(Model_YahooFinQuery1, x)

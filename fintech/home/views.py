import json
import string
import os
from django.shortcuts import render
from yahoo_finance import Share

def index(request):
    template_name = "home/index.html"
    ticker = request.GET.get('ticker', None)
    method = request.GET.get('method', None)
    start_date = request.GET.get('start', None)
    end_date = request.GET.get('end', None)
    share = Share('ticker')
    context = {}
    if ticker and method:
        if method == "price":
            context["price"] = share.get_price()
        elif method == "change":
            context["change"] = share.get_change()
        elif method == "percent_change":
            context["percent_change"] = share.get_percent_change()
        elif method == "volume":
            context["volume"] = share.get_volume()
        elif method == "pre_close":
            context["pre_close"] = share.get_pre_close()
        elif method == "open":
            context["open"] = share.get_open()
        elif method == "avg_daily_volume":
            context["avg_daily_volume"] = share.get_avg_daily_volume()
        elif method == "stock_exchange":
            context["stock_exchange"] = share.get_stock_exchange()
        elif method == "market_cap":
            context["market_cap"] = share.get_market_cap()
        elif method == "book_value":
            context["book_value"] = share.get_book_value()
        elif method == "ebitda":
            context["ebitda"] = share.get_ebitda()
        elif method == "dividend_share":
            context["dividend_share"] = share.get_dividend_share()
        elif method == "dividend_yield":
            context["dividend_yield"] = share.get_dividend_yield()
        elif method == "earnings_share":
            context["earnings_share"] = share.get_earnings_share()
        elif method == "days_high":
            context["days_high"] = share.get_days_high()
        elif method == "days_low":
            context["days_low"] = share.get_days_low()
        elif method == "year_high":
            context["year_high"] = share.get_year_high()
        elif method == "year_low":
            context["year_low"] = share.get_year_low()
        elif method == "50day_moving_avg":
            context["50day_moving_avg"] = share.get_50day_moving_avg()
        elif method == "200day_moving_avg":
            context["200day_moving_avg"] = share.get_200day_moving_avg()
        elif method == "price_earnings_ratio":
            context["price_earnings_ratio"] = share.get_price_earnings_ratio()
        elif method == "price_earnings_growth_ratio":
            context["price_earnings_growth_ratio"] = share.get_price_earnings_growth_ratio()
        elif method == "price_sales":
            context["price_sales"] = share.get_price_sales()
        elif method == "price_book":
            context["price_book"] = share.get_price_book()
        elif method == "short_ratio":
            context["short_ratio"] = share.get_short_ratio()
        elif method == "trade_datetime":
            context["trade_datetime"] = share.get_trade_datetime()
        elif method == "historical":
            context["historical"] = share.get_historical()
        elif method == "info":
            context["info"] = share.get_info()
        elif method == "name":
            context["name"] = share.get_name()

        return render(request, template_name, context)
    else:
        return render(request, template_name)

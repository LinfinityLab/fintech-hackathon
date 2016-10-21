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
    share = Share(ticker)
    context = {}
    if ticker and method:
        if method == "price":
            context["result"] = share.get_price()
        elif method == "change":
            context["result"] = share.get_change()
        elif method == "percent_change":
            context["result"] = share.get_percent_change()
        elif method == "volume":
            context["result"] = share.get_volume()
        elif method == "pre_close":
            context["result"] = share.get_pre_close()
        elif method == "open":
            context["result"] = share.get_open()
        elif method == "avg_daily_volume":
            context["result"] = share.get_avg_daily_volume()
        elif method == "stock_exchange":
            context["result"] = share.get_stock_exchange()
        elif method == "market_cap":
            context["result"] = share.get_market_cap()
        elif method == "book_value":
            context["result"] = share.get_book_value()
        elif method == "ebitda":
            context["result"] = share.get_ebitda()
        elif method == "dividend_share":
            context["result"] = share.get_dividend_share()
        elif method == "dividend_yield":
            context["result"] = share.get_dividend_yield()
        elif method == "earnings_share":
            context["result"] = share.get_earnings_share()
        elif method == "days_high":
            context["result"] = share.get_days_high()
        elif method == "days_low":
            context["result"] = share.get_days_low()
        elif method == "year_high":
            context["result"] = share.get_year_high()
        elif method == "year_low":
            context["result"] = share.get_year_low()
        elif method == "50day_moving_avg":
            context["result"] = share.get_50day_moving_avg()
        elif method == "200day_moving_avg":
            context["result"] = share.get_200day_moving_avg()
        elif method == "price_earnings_ratio":
            context["result"] = share.get_price_earnings_ratio()
        elif method == "price_earnings_growth_ratio":
            context["result"] = share.get_price_earnings_growth_ratio()
        elif method == "price_sales":
            context["result"] = share.get_price_sales()
        elif method == "price_book":
            context["result"] = share.get_price_book()
        elif method == "short_ratio":
            context["result"] = share.get_short_ratio()
        elif method == "trade_datetime":
            context["result"] = share.get_trade_datetime()
        elif method == "historical":
            context["result"] = share.get_historical()
        elif method == "info":
            context["result"] = share.get_info()
        elif method == "name":
            context["result"] = share.get_name()

        return render(request, template_name, context)
    else:
        return render(request, template_name)

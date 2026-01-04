from django.http import HttpResponse
import time

def convert(request):
    from_currency = request.GET.get('from').lower()
    to_currency = request.GET.get('to').lower()

    return HttpResponse(convert_currency_io_bound(from_currency, to_currency))

def convert_currency_io_bound(from_currency, to_currency):
    
    time.sleep(5) # DB uses 5 sec to respond

    if (from_currency == "usd" and to_currency == "gbp"):
        return 0.75
    elif (from_currency == "gbp" and to_currency == "usd"):
        return 1.33
    elif (from_currency == "usd" and to_currency == "eur"):
        return 0.86
    elif (from_currency == "eur" and to_currency == "usd"):
        return  1.16

def convert_currency_cpu_bound(from_currency, to_currency):
    
    # Do CPU-intensive work (finding primes up to a large number)
    limit = 1_000_000
    primes = []
    for x in range(limit):
        if is_prime(x):
            primes.append(x)

    if (from_currency == "usd" and to_currency == "gbp"):
        return 0.75
    elif (from_currency == "gbp" and to_currency == "usd"):
        return 1.33
    elif (from_currency == "usd" and to_currency == "eur"):
        return 0.86
    elif (from_currency == "eur" and to_currency == "usd"):
        return  1.16

def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
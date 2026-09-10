tea_price_inr={
    "masala chai":40,
    "lemon tea":50,
    "green tea":70,    
}
tea_prices_usd={tea:price/80 for tea,price in tea_price_inr.items()}
print(tea_prices_usd)
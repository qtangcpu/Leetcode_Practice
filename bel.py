import sys


def calculate_rolling_average(trades, window_quantity, window_trade_count):
    trade_history = []

    window_limit = window_quantity
    quantity_limit = window_trade_count
    n = len(trades)
    t = 0
    t_l = 0
    total_quantity = 0
    while t <len(trades):
        quantity_l = trades[t_l][1]
        total_quantity += trades[t][1]
        if t - t_l + 1 > window_limit:
            total_quantity -= trades[t_l][1]
            t_l +=1
        while total_quantity > quantity_limit:
            if (total_quantity-quantity_limit) >trades[t_l][1]:
                total_quantity -= trades[t_l][1]
                t_l +=1
            else:
                total_quantity -= (total_quantity-quantity_limit)
                quantity_l = trades[t_l][1] - (total_quantity-quantity_limit)
        #calculate average
        avg = 0
        avg_cnt = 0
        for i in range(t_l+1,t+1):
            avg += (trades[i][1]*trades[i][0])
            avg_cnt +=(trades[i][1])
        avg += (quantity_l*trades[t_l][0])
        #trade_history.append(avg/(avg_cnt+quantity_l))
        print("{:.2f}".format(avg/(avg_cnt+quantity_l)))



    # for price, quantity in trades:
    #     trade_history.append((price, quantity))
    #
    #     while sum(q for _, q in trade_history) > window_quantity or len(trade_history) > window_trade_count:
    #         trade_history.pop(0)
    #
    #     total_quantity = sum(q for _, q in trade_history)
    #     total_weighted_price = sum(price * q for price, q in trade_history)
    #
    #     average_price = total_weighted_price / total_quantity
    #     print("{:.2f}".format(average_price))


# Input parsing
input_str = input()
params, *trade_data = input_str.split(';')
window_quantity, window_trade_count = map(int, params.split(','))
trades = [(float(price), int(quantity)) for price, quantity in (data.split(',') for data in trade_data)]

# Calculate and print rolling averages
calculate_rolling_average(trades, window_quantity, window_trade_count)
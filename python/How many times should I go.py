# https://www.codewars.com/kata/57efcb78e77282f4790003d8
def how_many_times(annual_price, individual_price):
    times = annual_price // individual_price
    if annual_price % individual_price > 0: times += 1

    return times
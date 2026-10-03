from ast import literal_eval

OFFER_WRAPPERS = 3
wallet, cost = literal_eval(input())
chocolates_in_hand = wallet // cost
chocolates_by_offer = chocolates_in_hand // OFFER_WRAPPERS
remaining_chocolates = chocolates_by_offer + (chocolates_in_hand % OFFER_WRAPPERS)
chocolates = chocolates_in_hand + chocolates_by_offer

while remaining_chocolates > 2:
    chocolates_in_hand = remaining_chocolates
    chocolates_by_offer = remaining_chocolates // OFFER_WRAPPERS
    remaining_chocolates = chocolates_by_offer + (chocolates_in_hand % OFFER_WRAPPERS)
    chocolates += chocolates_by_offer

print(chocolates)

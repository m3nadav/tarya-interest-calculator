#!/usr/bin/env python

TAX = 15
SUCCESS_COMMISSION_PCT = 10
INVEST_YEARLY_COMMISSION_PCT = 0.5
INTEREST_PCT_OVER_2YR = 6.5/12
INTEREST_PCT_OVER_1YR = 5.5/12
INTEREST_PCT_FLUID = 5/12

def calc_success_commission_pct(invested, interest_pct):
    return invested * interest_pct / 100 * SUCCESS_COMMISSION_PCT / 100

def calc_monthly_interest(invested, interest_pct):
    return invested * interest_pct / 100

def calc_invest_commission(invested):
    monthly_commission = INVEST_YEARLY_COMMISSION_PCT / 100 / 12
    return invested * monthly_commission

def calc_commission(invested, interest_pct):
   return min(calc_success_commission_pct(invested, interest_pct), calc_invest_commission(invested))

def calc_tax(invested, interest_pct):
    bruto_for_fortune_tax = (calc_monthly_interest(invested, interest_pct) - calc_commission(invested, interest_pct))
    return TAX / 100 * bruto_for_fortune_tax

def calc_tara(invested, interest_pct):
    return calc_commission(invested, interest_pct) + calc_tax(invested, interest_pct)

def calc_neto(invested, interest_pct):
    return calc_monthly_interest(invested, interest_pct) - calc_tara(invested, interest_pct)

def sum_netos(invested_2yr, invested_1yr, invested_fluid):
    monthly_interest_2yr = calc_neto(invested_2yr, INTEREST_PCT_OVER_2YR)
    monthly_interest_1yr = calc_neto(invested_1yr, INTEREST_PCT_OVER_1YR)
    monthly_interest_fluid = calc_neto(invested_fluid, INTEREST_PCT_FLUID)

    return monthly_interest_2yr + monthly_interest_1yr + monthly_interest_fluid

if __name__ == "__main__":
    import sys

    args = sys.argv + [0] * (4 - len(sys.argv))

    invested_2yr = int(args[1])
    invested_1yr = int(args[2])
    invested_fluid = int(args[3])

    monthly_interest_2yr = calc_neto(invested_2yr, INTEREST_PCT_OVER_2YR)
    monthly_interest_1yr = calc_neto(invested_1yr, INTEREST_PCT_OVER_1YR)
    monthly_interest_fluid = calc_neto(invested_fluid, INTEREST_PCT_FLUID)
    print(f"Interest while closing {invested_2yr} for 2 years: {monthly_interest_2yr}")
    print(f"Interest while closing {invested_1yr} for 12 months: {monthly_interest_1yr}")
    print(f"Interest while closing {invested_fluid} in fluid investment: {monthly_interest_fluid}")
    print()
    print(f"Total interest will be: {monthly_interest_2yr + monthly_interest_1yr + monthly_interest_fluid}")

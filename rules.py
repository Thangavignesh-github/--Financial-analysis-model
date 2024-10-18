import datetime


class FLAGS:
    GREEN = 1
    AMBER = 2
    RED = 0
    MEDIUM_RISK = 3  # display purpose only
    WHITE = 4  # data is missing for this field


def latest_financial_index(data: dict):
    """
    Determine the index of the latest standalone financial entry in the data.
    """
    for index, financial in enumerate(data.get("financials", [])):
        if financial.get("nature") == "STANDALONE":
            return index
    return 0


def total_revenue(data: dict, financial_index):
    """
    Calculate the total revenue from the financial data at the given index.
    """
    try:
        financials = data["financials"][financial_index]
        pnl = financials["pnl"]["lineItems"]
        # Using "net_revenue" as per your data structure
        total_revenue = pnl.get("net_revenue", 0)  # Changed to match your JSON structure
        return total_revenue
    except (IndexError, KeyError):
        return 0  # Return 0 if data is missing or incorrect


def total_borrowing(data: dict, financial_index):
    """
    Calculate the ratio of total borrowings to total revenue for the financial data at the given index.
    """
    try:
        financials = data["financials"][financial_index]
        balance_sheet = financials["bs"]["lineItems"]
        long_term_borrowings = balance_sheet.get("Long Term Borrowings", 0)
        short_term_borrowings = balance_sheet.get("Short Term Borrowings", 0)
        total_borrowings = long_term_borrowings + short_term_borrowings

        revenue = total_revenue(data, financial_index)
        if revenue > 0:
            return total_borrowings / revenue
        return 0
    except (IndexError, KeyError):
        return 0


def iscr_flag(data: dict, financial_index):
    """
    Determine the flag color based on the ISCR value.
    """
    iscr_value = iscr(data, financial_index)

    if iscr_value >= 2:
        return FLAGS.GREEN
    return FLAGS.RED


def total_revenue_5cr_flag(data: dict, financial_index):
    """
    Determine the flag color based on whether the total revenue exceeds 50 million.
    """
    revenue = total_revenue(data, financial_index)

    if revenue >= 50000000:  # 5 crore
        return FLAGS.GREEN
    return FLAGS.RED


def iscr(data: dict, financial_index):
    """
    Calculate the Interest Service Coverage Ratio (ISCR) for the financial data at the given index.
    """
    try:
        financials = data["financials"][financial_index]
        pnl = financials["pnl"]["lineItems"]

        profit_before_interest_and_tax = pnl.get("profit_before_interest_and_tax", 0)  # Updated key
        depreciation = pnl.get("depreciation", 0)  # Updated key
        interest_expenses = pnl.get("interest", 0)  # Updated key

        iscr_value = (profit_before_interest_and_tax + depreciation + 1) / (
            interest_expenses + 1
        )
        return iscr_value
    except (IndexError, KeyError):
        return 0


def borrowing_to_revenue_flag(data: dict, financial_index):
    """
    Determine the flag color based on the ratio of total borrowings to total revenue.
    """
    borrowing_ratio = total_borrowing(data, financial_index)

    if borrowing_ratio <= 0.25:
        return FLAGS.GREEN
    return FLAGS.AMBER

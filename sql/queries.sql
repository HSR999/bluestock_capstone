-- 1. Top 5 Funds by AUM
SELECT
    scheme_name,
    fund_house,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- 2. Average NAV per Month
SELECT
    strftime('%Y-%m', date) AS month,
    AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;


-- 3. Total SIP Investment Amount
SELECT
    SUM(amount_inr) AS total_sip_amount
FROM fact_transactions
WHERE transaction_type = 'SIP';


-- 4. Transactions by State
SELECT
    state,
    COUNT(*) AS transaction_count,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;


-- 5. Funds with Expense Ratio Below 1%
SELECT
    scheme_name,
    fund_house,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


-- 6. Top 10 Funds by 5-Year Return
SELECT
    scheme_name,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;


-- 7. Average Return by Fund Category
SELECT
    category,
    AVG(return_3yr_pct) AS avg_3yr_return
FROM fact_performance
GROUP BY category
ORDER BY avg_3yr_return DESC;


-- 8. Transaction Count by Payment Mode
SELECT
    payment_mode,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY payment_mode
ORDER BY total_transactions DESC;


-- 9. Average Investment Amount by City Tier
SELECT
    city_tier,
    AVG(amount_inr) AS avg_investment
FROM fact_transactions
GROUP BY city_tier
ORDER BY avg_investment DESC;


-- 10. Top Categories by Average AUM
SELECT
    category,
    AVG(aum_crore) AS avg_aum
FROM fact_performance
GROUP BY category
ORDER BY avg_aum DESC;
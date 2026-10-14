in some ways related to [[AI-related projects]]

- Options pricing and greeks engine (black scholes, binomial trees, monte carlo; calculate the greeks and build the volatility surface from real market data)
- Pairs trading backtester (cointegration to find stocks that move together, spread calculator when it breaks, adding transactions costs, testing on out-of-sample-data)
- Limit order book market-making simulator
- ML alpha signal (predicts return but validate it with walk forward testing and no data leakage, in order to not overfit)

- Reverse DCF model
- Three statement model from primary filings
- Systematic strategy backtest

- end-to-end data pipeline
    1. data source through API
    2. kafka (for event streaming)
    3. spark (to clean and transform)
    4. snowflake (data warehouse)
    5. looker (data visualization)
- real time data pipeline
    1. event source (json)
    2. kafka
    3. spark
    4. snowflakes
    5. analytics
- data warehouse on the cloud 
    1. raw data (csv or json)
    2. snowflake (data warehouse)
    3. dbt (to transform and model)
    4. Analitycs (BI ready tables)
- data lakehouse
    1. raw data
    2. snowflake
    3. dbt
    4. data marts
    5. BI tool

- analyze a company
    ![[Screenshot 2026-10-14 alle 19.14.36.png]]
- other classics: Three-statement model; DCF model; Forecasting model; M&A model; LBO model

# a useful python toolkit
"GS Quant" on github (but it may be a sort of scam)
## Objectives

The purpose of this project is to build a forecasting model *(forecasting)* that can predict sales quantity in the next period. To create this forecasting model, I will use historical sales data from the `ParagonCorp` dataset that has been provided to identify product sales patterns and trends, and make predictions based on these patterns. Of course, this will help businesses to plan *inventory* and *staffing levels* to be more effective and can ensure that they are ready for changes in demand. To achieve this goal, the steps taken are as follows:<br>
1. Collect historical sales data.<br>
In this project, I will use historical sales data from the period `2021-52` to `2023-14` which can be used to train a forecasting model.<br>
2. Explore data.<br>
I will analyze the data to identify any trends or patterns that might be useful in predicting future sales. This can include `trend`, `seasonality` and `noise` over time.<br>
3. Select a forecasting model.<br>
I will choose the appropriate forecasting model based on the characteristics of the data and the nature of the sales process.<br>
4. Training model.<br>
I will use historical data to train my forecasting model, adjusting model parameters as necessary to optimize performance.<br>
5. Evaluate the model.<br>
I will use the data set to evaluate the performance of the model and make any necessary adjustments.<br>
6. Prediction of sales.<br>
I will use the model that has been trained to estimate sales for the next 1 period.

## Data description `sample_dataset_timeseries_noarea.csv`

* Field Description: <br>

Feature | Description
---|---
`week_number`| contained information about week of specific product sold, (2021-52 to 2023-14)
`week_start_date`| contained information about week start date of specific product sold
`week_end_date`| contained information about week end date of specific product sold
`product_item`| contained information about product item/product code (Variabel Bebas)
`quantity`| contained information about quantity of product in respective week

Dataset source: `ParagonCorp`.

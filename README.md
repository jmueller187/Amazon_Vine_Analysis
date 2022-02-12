# Amazon_Vine_Analysis
Amazon Vine review analysis using PySpark, Amazon RDS &amp; S3 and pgAdmin

## Overview of the analysis:
The purpose of this project was to analyze Amazon reviews written by members of the Amazon Vine program, which is a service that allows merchants selling on Amazon to receive reviews for their products. We started by selecting a musical instrument dataset, and then loaded this dataset into PySpark to perform our Extract, Transform, Load process. After extracting the appropriate data and transforming it into four dataframes, we connected to our Amazon RDS instance and loaded the data into our pgAdmin database. Once the database had been populated, our final task was to determine if any bias towards favorable reviews from the Vine reviewers was present in our dataset.

## Results:
The following tables show the data used for our analysis. Table 1 shows a portion of the data where a review was written as part of the Vine program (paid), and Table 2 shown a portion of the data where the review was not part of the Vine program (unpaid).<br>
Table 1:<br>
![Paid Vine Reviews](https://github.com/jmueller187/Amazon_Vine_Analysis/blob/main/Resources/VineReviewsDataFrame.png)

Table 2:<br>
![Unpaid Vine Reviews](https://github.com/jmueller187/Amazon_Vine_Analysis/blob/main/Resources/NonVineReviewsDataFrame.png)

We uses this data to address the following questions:
- How many Vine reviews and non-Vine reviews were there?<br>
Our analysis identified a total of 60 paid Vine reviews (see Image 1), and 14,477 unpaid Vine reviews (see Image 2).<br>
Image 1:<br>
![Total Paid Reviews](https://github.com/jmueller187/Amazon_Vine_Analysis/blob/main/Resources/TotalPaidReviews.png)

Image 2:<br>
![Total Unpaid Reviews](https://github.com/jmueller187/Amazon_Vine_Analysis/blob/main/Resources/TotalUnpaidReviews.png)

- How many Vine reviews were 5 stars? How many non-Vine reviews were 5 stars?<br>
Our analysis identified a total of 34 paid 5-star reviews (see Image 3), and 8,212 unpaid 5-star reviews (see Image 4).<br>
Image 3:<br>
![Paid 5-star reviews](https://github.com/jmueller187/Amazon_Vine_Analysis/blob/main/Resources/TotalPaid5StarReviews.png)

Image 4:<br>
![Unpaid 5-star reviews](https://github.com/jmueller187/Amazon_Vine_Analysis/blob/main/Resources/TotalUnpaid5StarReviews.png)

- What percentage of Vine reviews were 5 stars? What percentage of non-Vine reviews were 5 stars?<br>
Our analysis revealed that 56.67% of the paid reviews were 5-star reviews (see Image 5), and 56.72% of the unpaid reviews were 5-star reviews (see Image 6).<br>
Image 5:<br>
![Paid 5-star reviews percentage](https://github.com/jmueller187/Amazon_Vine_Analysis/blob/main/Resources/PercentPaid5StarReviews.png)

Image 6:<br>
![Unpaid 5-star reviews percentage](https://github.com/jmueller187/Amazon_Vine_Analysis/blob/main/Resources/PercentPaid5StarReviews.png)

## Summary:
In your summary, state if there is any positivity bias for reviews in the Vine program. Use the results of your analysis to support your statement. Then, provide one additional analysis that you could do with the dataset to support your statement.

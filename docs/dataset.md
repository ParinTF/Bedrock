# Dataset Documentation

## Dataset Overview

- **Name:** eCommerce Behavior Data from Multi-Category Store
- **Provider:** REES46 Marketing Platform
- **Data Type:** Customer behavior events
- **Time Period:** October 2019 – April 2020
- **Full Dataset Size:** Approximately 285 million events, as reported by the dataset description.
- **Source Format:** CSV / GZIP
- **Official Source:** https://data.rees46.com/
- **Kaggle:** https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store

## Initial Dataset

| Property | Value |
|---|---|
| Source partition | October 2019 |
| Source file | 2019-Oct.csv.gz |
| Expected source records | Approximately 42.4 million |
| Development sample target | 10,000 records |
| Sampling method | First-N records |
| Source storage | data/raw/ |
| Sample storage | data/samples/ |

## Data Dictionary

| Column | Target Data Type | Description |
|---|---|---|
| event_time | TIMESTAMP | Event timestamp in UTC |
| event_type | VARCHAR | Customer interaction type |
| product_id | BIGINT | Product identifier |
| category_id | BIGINT | Product category identifier |
| category_code | VARCHAR | Product category hierarchy |
| brand | VARCHAR | Product brand |
| price | DECIMAL | Product price |
| user_id | BIGINT | User identifier |
| user_session | VARCHAR | Session identifier |

## Event Types

- view
- cart
- remove_from_cart
- purchase

Actual event types will be validated for each monthly partition.

## Data Limitations

- The dataset contains historical customer interaction events.
- One record represents an event, not necessarily an order.
- Missing values may exist in some fields.
- Product prices do not necessarily represent net revenue.
- The development sample is not statistically representative of the full dataset.

## Data Governance

- Preserve original source files.
- Do not commit raw or generated datasets to Git.
- Record dataset provenance.
- Verify usage terms before commercial use or redistribution.
- Keep synthetic benchmark data separate from real-world data.

## Attribution

Thanks to REES46 Marketing Platform for providing the dataset.
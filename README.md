# Python Libraries Collection

A collection of custom Python utility functions and libraries for data analysis and development.

## Contents

- `pandas_utils.py` - Custom utilities for pandas DataFrame analysis

## pandas_utils.py

### Functions

- `custom_info(df)` - Enhanced DataFrame information display with completeness analysis
  - Shows total rows and columns
  - Displays column-wise data types and completeness percentages
  - Highlights columns with missing values using bullet markers
  - Shows memory usage information

## Usage

```python
import pandas as pd
from pandas_utils import custom_info

# Load your DataFrame
df = pd.read_csv('your_data.csv')

# Get enhanced info with completeness analysis
custom_info(df)
```

## Requirements

- pandas

## Installation

Clone this repository and import the utilities as needed in your Python projects.
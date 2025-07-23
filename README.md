# Python Libraries Collection

A collection of custom Python utility functions and libraries for data analysis and development.

## Contents

- `pandas_utils.py` - Advanced utilities for pandas DataFrame analysis and exploration

## pandas_utils.py

### Functions

#### `custom_info(df)`
Enhanced DataFrame information display with completeness analysis
- Shows total rows and columns count
- Displays column-wise data types and completeness percentages
- Highlights columns with missing values using bullet markers (•)
- Shows memory usage information in KB

#### `custom_describe(df)`
Enhanced describe function for numeric columns with extended statistical measures
- Comprehensive statistics: count, mean, median, mode
- Variability measures: standard deviation, variance
- Distribution shape: skewness, kurtosis
- Range information: min, quartiles (25%, 50%, 75%), max, range
- Organized output with proper statistical ordering

#### `full_analysis(df, save_to=None)` 
Complete integrated DataFrame analysis combining overview and detailed statistics
- **Overview**: Total rows/columns, data types summary, memory usage
- **Integrated Statistics**: All statistical measures in a single comprehensive table
- **Data Quality**: Completeness percentages and data types for each column
- **Advanced Metrics**: Includes all measures from custom_describe plus data completeness
- **Export Capability**: Save analysis to CSV or Excel files with `save_to` parameter
- Visual formatting with emojis and clear section separation

## Usage Examples

### Basic Information Analysis
```python
import pandas as pd
from pandas_utils import custom_info

# Load your DataFrame
df = pd.read_csv('your_data.csv')

# Get enhanced info with completeness analysis
custom_info(df)
```

### Enhanced Statistical Description
```python
from pandas_utils import custom_describe

# Get comprehensive statistical summary for numeric columns
custom_describe(df)
```

### Complete DataFrame Analysis
```python
from pandas_utils import full_analysis

# Get complete integrated analysis (recommended for thorough exploration)
full_analysis(df)

# Save analysis to CSV file
full_analysis(df, save_to='dataset_analysis.csv')

# Save analysis to Excel file (with separate sheets for overview and statistics)
full_analysis(df, save_to='dataset_report.xlsx')
```

### Import All Functions
```python
from pandas_utils import custom_info, custom_describe, full_analysis

# Use any function as needed
custom_info(df)          # Quick overview with completeness
custom_describe(df)      # Detailed numeric statistics  
full_analysis(df)        # Complete integrated analysis
```

## Export Functionality

The `full_analysis()` function supports exporting results to files for reporting and documentation:

### Supported Formats
- **CSV files** (`.csv`): Single file with dataset overview and statistics table
- **Excel files** (`.xlsx`): Multi-sheet workbook with separate tabs for:
  - **Dataset_Overview**: General information about the dataset
  - **Statistics**: Complete statistical analysis table

### Export Examples
```python
# Export to CSV - all information in one file
full_analysis(df, save_to='my_analysis.csv')

# Export to Excel - organized in separate sheets
full_analysis(df, save_to='my_report.xlsx')

# The function will display the analysis on screen AND save to file
```

### What Gets Exported
- Dataset overview (rows, columns, data types, memory usage)
- Complete statistical analysis for all numeric columns
- Data completeness information
- All statistical measures (mean, median, mode, std, variance, quartiles, skewness, kurtosis, etc.)

## Features

- 🔍 **Enhanced Data Exploration**: Go beyond pandas' basic info() and describe()
- 📊 **Statistical Completeness**: Includes advanced metrics like skewness, kurtosis, mode, variance
- 🎯 **Data Quality Focus**: Highlights missing values and data completeness issues
- 📈 **Integrated Analysis**: Combines overview, quality check, and statistics in one view
- 💾 **Export Functionality**: Save complete analysis to CSV or Excel files
- 🎨 **Visual Formatting**: Clean, organized output with emojis and clear sections
- ⚡ **Easy to Use**: Simple function calls with comprehensive results

## Requirements

- pandas
- numpy

## Installation

Clone this repository and import the utilities as needed in your Python projects:

```bash
git clone https://github.com/marcelosilva2604/mylibs.git
cd mylibs
```

Then import in your Python scripts:
```python
from pandas_utils import custom_info, custom_describe, full_analysis
```
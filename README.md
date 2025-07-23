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

#### `full_analysis(df)` 
Complete integrated DataFrame analysis combining overview and detailed statistics
- **Overview**: Total rows/columns, data types summary, memory usage
- **Integrated Statistics**: All statistical measures in a single comprehensive table
- **Data Quality**: Completeness percentages and data types for each column
- **Advanced Metrics**: Includes all measures from custom_describe plus data completeness
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
```

### Import All Functions
```python
from pandas_utils import custom_info, custom_describe, full_analysis

# Use any function as needed
custom_info(df)          # Quick overview with completeness
custom_describe(df)      # Detailed numeric statistics  
full_analysis(df)        # Complete integrated analysis
```

## Features

- 🔍 **Enhanced Data Exploration**: Go beyond pandas' basic info() and describe()
- 📊 **Statistical Completeness**: Includes advanced metrics like skewness, kurtosis, mode, variance
- 🎯 **Data Quality Focus**: Highlights missing values and data completeness issues
- 📈 **Integrated Analysis**: Combines overview, quality check, and statistics in one view
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
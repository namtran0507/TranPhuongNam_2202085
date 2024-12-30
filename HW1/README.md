
# Data Visualization Name Sorting and Transformation

This repository contains a Python script designed to perform data visualization and manipulation tasks using the `datascience` library. The tasks include creating a dataset, formatting numerical data, sorting names, and abbreviating names. The script is structured to showcase fundamental data processing techniques.

## Features

### 1. **Create Dataset**
- A table is created with three columns:
  - `Ho va Ten` (Full Name): A list of sample Vietnamese names.
  - `Tuoi` (Age): Corresponding ages of individuals.
  - `So Du (VND)` (Balance): Financial balances in Vietnamese Dong.

### 2. **Format Balances**
- Converts the numerical data in the `So Du (VND)` column to a formatted string representation with commas and two decimal places for better readability.

### 3. **Sort by Last Name**
- Splits full names to extract last names.
- Adds a temporary column for sorting.
- Sorts the table by the extracted last names in ascending order and removes the temporary column.

### 4. **Abbreviate Names**
- Implements a function to abbreviate full names, keeping the last name in full while reducing other parts to initials.
  - Example: "Nguyen Thi Binh" becomes "N.T.Binh".

## Prerequisites

Ensure you have the following installed:
- Python 3.x
- Libraries:
  - `datascience`
  - `numpy`
  - `matplotlib`

You can install the required libraries using pip:
```bash
pip install datascience numpy matplotlib
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Script Overview

The script contains:
1. **Dataset Creation**: Defines a sample table with names, ages, and balances.
2. **Balance Formatting**: Formats monetary values for improved clarity.
3. **Name Sorting**: Extracts and sorts by last names.
4. **Name Abbreviation**: Shortens names by initials, keeping the last name intact.

## Output

The final table showcases:
- Abbreviated full names.
- Sorted order based on last names.
- Formatted financial data.

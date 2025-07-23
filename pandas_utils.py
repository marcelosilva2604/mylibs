"""
Utilitários personalizados para pandas
"""
import pandas as pd

def custom_info(df):
    """
    Exibe informações customizadas do DataFrame com análise de completude
    """
    total_rows = len(df)
    print(f"DataFrame Info with Completeness Analysis:")
    print("-" * 75)
    print(f"Total Rows: {total_rows}")
    print(f"Total Columns: {len(df.columns)}")
    print("\nColumn Details:")
    print("-" * 75)
    
    for col in df.columns:
        non_null = df[col].count()
        dtype = str(df[col].dtype)
        completeness = (non_null / total_rows * 100).round(2)
        
        # Add red dot (•) for columns with missing values
        marker = " •" if completeness < 100 else ""
        print(f"{col:<20} {non_null:>8} non-null {dtype:<10} ({completeness}% complete){marker}")
    
    print(f"\nMemory Usage: {df.memory_usage().sum() / 1024:.1f}+ KB")
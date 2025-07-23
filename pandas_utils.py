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

def custom_describe(df):
    """
    Describe melhorado para colunas numéricas com estatísticas adicionais
    Ordem: count → mean/median/mode → std/variance → min/quartis/max → range → skew/kurtosis
    """
    import numpy as np
    
    # Seleciona apenas colunas numéricas
    numeric_df = df.select_dtypes(include=[np.number])
    
    if numeric_df.empty:
        print("Nenhuma coluna numérica encontrada!")
        return
    
    print("Enhanced DataFrame Description (Numeric Columns Only):")
    print("=" * 80)
    
    results = {}
    
    for col in numeric_df.columns:
        series = numeric_df[col]
        
        # Estatísticas básicas
        count = series.count()
        mean_val = series.mean()
        median_val = series.median()
        mode_val = series.mode().iloc[0] if not series.mode().empty else np.nan
        std_val = series.std()
        var_val = series.var()
        
        # Quartis e extremos
        min_val = series.min()
        q25 = series.quantile(0.25)
        q50 = series.quantile(0.50)  # mediana
        q75 = series.quantile(0.75)
        max_val = series.max()
        
        # Métricas adicionais
        range_val = max_val - min_val
        skew_val = series.skew()
        kurt_val = series.kurtosis()
        
        results[col] = {
            'count': count,
            'mean': mean_val,
            'median': median_val,
            'mode': mode_val,
            'std': std_val,
            'variance': var_val,
            'min': min_val,
            '25%': q25,
            '50%': q50,
            '75%': q75,
            'max': max_val,
            'range': range_val,
            'skewness': skew_val,
            'kurtosis': kurt_val
        }
    
    # Converte para DataFrame para exibição organizada
    result_df = pd.DataFrame(results)
    
    # Reordena as linhas (estatísticas) na ordem desejada
    row_order = ['count', 'mean', 'median', 'mode', 'std', 'variance', 
                'min', '25%', '50%', '75%', 'max', 'range', 'skewness', 'kurtosis']
    
    result_df = result_df.loc[row_order]
    
    print(result_df.round(4))
    print("=" * 80)

def full_analysis(df):
    """
    Análise completa do DataFrame: informações gerais + estatísticas detalhadas
    """
    import numpy as np
    
    print("🔍 FULL DATAFRAME ANALYSIS")
    print("=" * 80)
    
    # === SEÇÃO 1: INFORMAÇÕES GERAIS ===
    total_rows = len(df)
    total_cols = len(df.columns)
    
    print(f"📊 OVERVIEW:")
    print(f"   Total Rows: {total_rows:,}")
    print(f"   Total Columns: {total_cols}")
    print(f"   Memory Usage: {df.memory_usage(deep=True).sum() / 1024 / 1024:.2f} MB")
    print()
    
    # Tipos de dados
    type_counts = df.dtypes.value_counts()
    print(f"📋 DATA TYPES:")
    for dtype, count in type_counts.items():
        print(f"   {dtype}: {count} columns")
    print()
    
    # === SEÇÃO 2: COMPLETUDE POR COLUNA ===
    print(f"📊 COLUMN COMPLETENESS:")
    print("-" * 75)
    print(f"{'Column':<25} {'Non-Null':<12} {'Type':<15} {'Complete %':<12} {'Status'}")
    print("-" * 75)
    
    missing_cols = []
    
    for col in df.columns:
        non_null = df[col].count()
        dtype = str(df[col].dtype)
        completeness = (non_null / total_rows * 100)
        
        # Status visual
        if completeness == 100:
            status = "✅"
        elif completeness >= 95:
            status = "⚠️"
        else:
            status = "🔴"
            
        if completeness < 100:
            missing_cols.append((col, total_rows - non_null, completeness))
        
        print(f"{col:<25} {non_null:>8,} {dtype:<15} {completeness:>7.1f}% {status}")
    
    print("-" * 75)
    
    # Resumo de problemas
    if missing_cols:
        print(f"\n⚠️  MISSING VALUES SUMMARY:")
        for col, missing, completeness in missing_cols:
            print(f"   {col}: {missing:,} missing ({100-completeness:.1f}%)")
    else:
        print(f"\n✅ No missing values found!")
    
    print()
    
    # === SEÇÃO 3: ESTATÍSTICAS NUMÉRICAS ===
    numeric_df = df.select_dtypes(include=[np.number])
    
    if not numeric_df.empty:
        print("📊 NUMERIC COLUMNS STATISTICS:")
        print("=" * 80)
        
        results = {}
        
        for col in numeric_df.columns:
            series = numeric_df[col]
            
            # Estatísticas básicas
            count = series.count()
            mean_val = series.mean()
            median_val = series.median()
            mode_val = series.mode().iloc[0] if not series.mode().empty else np.nan
            std_val = series.std()
            var_val = series.var()
            
            # Quartis e extremos
            min_val = series.min()
            q25 = series.quantile(0.25)
            q50 = series.quantile(0.50)
            q75 = series.quantile(0.75)
            max_val = series.max()
            
            # Métricas adicionais
            range_val = max_val - min_val
            skew_val = series.skew()
            kurt_val = series.kurtosis()
            
            results[col] = {
                'count': count,
                'mean': mean_val,
                'median': median_val,
                'mode': mode_val,
                'std': std_val,
                'variance': var_val,
                'min': min_val,
                '25%': q25,
                '50%': q50,
                '75%': q75,
                'max': max_val,
                'range': range_val,
                'skewness': skew_val,
                'kurtosis': kurt_val
            }
        
        # Exibe tabela de estatísticas
        result_df = pd.DataFrame(results)
        row_order = ['count', 'mean', 'median', 'mode', 'std', 'variance', 
                    'min', '25%', '50%', '75%', 'max', 'range', 'skewness', 'kurtosis']
        result_df = result_df.loc[row_order]
        
        print(result_df.round(4))
    else:
        print("📊 No numeric columns found for statistical analysis.")
    
    print("=" * 80)
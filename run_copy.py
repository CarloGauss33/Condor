import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def read_and_clean_data(file_path):
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)

        # Clean the data
        df = df.dropna()  # remove rows with missing values
        df.columns = df.columns.str.strip()  # remove leading/trailing spaces from column names

        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print(f"No data in file: {file_path}")
        return None
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

def create_bar_plot(df, x_col, y_col):
    # Set the style
    sns.set(style="whitegrid")

    # Create the bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=x_col, y=y_col, data=df, ax=ax, palette="Blues_d")

    # Customize the plot
    ax.set_title('Bar Plot', fontsize=15)
    ax.set_xlabel(x_col, fontsize=12)
    ax.set_ylabel(y_col, fontsize=12)

    # Show the plot
    plt.show()

# Use the functions
data = read_and_clean_data('your_file.csv')
if data is not None:
    create_bar_plot(data, 'column1', 'column2')

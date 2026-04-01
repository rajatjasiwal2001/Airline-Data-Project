import pandas as pd

# 1. Load data
df = pd.read_csv("data.csv")

print("✅ Data Loaded Successfully")
print("Shape:", df.shape)

# 2. Clean column names
df.columns = df.columns.str.lower().str.strip()

# 3. Show columns
print("\nColumns:", df.columns)

# 4. Remove missing values
df = df.dropna()

print("After cleaning:", df.shape)

# 5. Detect delay column automatically
delay_col = None
for col in df.columns:
    if "delay" in col:
        delay_col = col
        break

print("Delay column:", delay_col)

# 6. Create delay_status column
if delay_col:
    df["delay_status"] = df[delay_col].apply(lambda x: "Late" if x > 15 else "On Time")
else:
    print("⚠️ No delay column found")

# 7. Airline wise delay analysis
if "airline" in df.columns and delay_col:
    print("\n📊 Airline Wise Avg Delay:")
    print(df.groupby("airline")[delay_col].mean())

# 8. Delay status count
if "delay_status" in df.columns:
    print("\n📊 Delay Status Count:")
    print(df["delay_status"].value_counts())

# 9. Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("\n✅ cleaned_data.csv saved successfully")
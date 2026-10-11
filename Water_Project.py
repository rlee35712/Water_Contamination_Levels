import pandas as pd
import matplotlib.pyplot as plt

choice = input("Enter a key: ")

if choice == "a":
    df = pd.read_csv("water_pollution_disease.csv")
    
    source_counts = df["Water Source Type"].value_counts()
    
    plt.figure(figsize=(8, 8))
    plt.pie(
        source_counts, 
        labels=source_counts.index, 
        autopct="%1.1f%%", 
        startangle=140, 
        colors=["#32ffeb", "#87db34", "#b256a7", "#ecba31", "#aeb2f1", "#ae0193"]
    )
    
    plt.title("Distribution of Water Source Types", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.show()

elif choice == "b":
    df = pd.read_csv("water_pollution_disease.csv")
    
    disease_cols = [
        "Diarrheal Cases per 100,000 people",
        "Cholera Cases per 100,000 people",
        "Typhoid Cases per 100,000 people",
        "Infant Mortality Rate (per 1,000 live births)"
    ]
    
    country_averages = df.groupby("Country")[disease_cols].mean()
    
    country_averages.plot(
        kind="bar", 
        figsize=(12, 7), 
        color=["#32ffeb", "#87db34", "#b256a7", "#ecba31"]
    )
    
    plt.title("Disease Burden Comparison across Countries", fontsize=14, fontweight="bold")
    plt.xlabel("Country", fontsize=12)
    plt.ylabel("Rates / Cases", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.legend(title="Diseases / Rates")
    
    plt.tight_layout()
    plt.show()

else:
    print("Invalid key pressed.")

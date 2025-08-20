import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic customer data
n = 150
acquisition_cost = np.random.uniform(50, 500, n)  # Acquisition cost between $50 and $500
lifetime_value = acquisition_cost * np.random.uniform(2, 8, n) + np.random.normal(0, 200, n)  # CLV related to cost

# Create DataFrame
df = pd.DataFrame({
    "Acquisition_Cost": acquisition_cost,
    "Lifetime_Value": lifetime_value
})

# Apply Seaborn professional style
sns.set_style("whitegrid")
sns.set_context("talk")

# Create scatterplot
plt.figure(figsize=(8, 8))  # ensures 512x512 at dpi=64
sns.scatterplot(
    data=df,
    x="Acquisition_Cost",
    y="Lifetime_Value",
    hue="Acquisition_Cost",
    palette="viridis",
    size="Lifetime_Value",
    sizes=(40, 200),
    alpha=0.8
)

# Add titles and labels
plt.title("Customer Lifetime Value vs. Acquisition Cost", fontsize=16, weight="bold")
plt.xlabel("Customer Acquisition Cost ($)", fontsize=12)
plt.ylabel("Customer Lifetime Value ($)", fontsize=12)

# Save figure as PNG (512x512 pixels)
plt.savefig("chart.png", dpi=64, bbox_inches="tight")

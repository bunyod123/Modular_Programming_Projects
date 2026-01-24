import matplotlib.pyplot as plt
import seaborn as sns


        
def visualize_data(df):
    print("\n--- 2. Vizualizatsiya jarayoni ---")
    
    # Target (Price Range) taqsimoti
    plt.figure(figsize=(8, 5))
    sns.countplot(x='price_range', data=df)
    plt.title('Narx oralig\'i taqsimoti (Target Variable)')
    plt.show()
    
    # Korrelyatsiya matritsasi
    plt.figure(figsize=(20, 15))
    sns.heatmap(df.corr(), annot=True, fmt='.2f', cmap='coolwarm')
    plt.title('Xususiyatlar orasidagi korrelyatsiya')
    plt.show()
    
    # RAM va Narx o'rtasidagi bog'liqlik
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='price_range', y='ram', data=df)
    plt.title('Narx oralig\'i va RAM bog\'liqligi')
    plt.show()


import shap
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class ShapAnalyzer:
    def __init__(self, model, X_train):
       
        self.model = model
        self.X_train = X_train
        self.explainer = None
        self.shap_values = None
        
        # Analizni boshlash
        self.calculate_shap_values()

    def calculate_shap_values(self):
        
        try:
            
            self.explainer = shap.Explainer(self.model, self.X_train)
            self.shap_values = self.explainer(self.X_train)
            
        except Exception:
            sample_data = shap.sample(self.X_train, 100)
            self.explainer = shap.KernelExplainer(self.model.predict, sample_data)
            self.shap_values = self.explainer.shap_values(sample_data)

    def plot_summary(self):
        
        plt.figure(figsize=(10, 6))
        shap.summary_plot(self.shap_values, self.X_train, show=False)
        plt.title("Model uchun eng muhim faktorlar", fontsize=14)
        plt.tight_layout()
        plt.show()

    def plot_bar(self):
        
        plt.figure()
        shap.plots.bar(self.shap_values, show=False)
        plt.title("Faktorlarning ta'sir kuchi", fontsize=14)
        plt.show()

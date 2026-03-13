from sklearn.ensemble import (
    RandomForestClassifier, GradientBoostingClassifier, VotingClassifier,
    RandomForestRegressor, GradientBoostingRegressor, VotingRegressor
)
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error, r2_score, mean_absolute_error

def train_voting_model(X_train, X_test, y_train, y_test, task_type='classification'):
 
    
    if task_type == 'classification':
        
        rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
        gb_model = GradientBoostingClassifier(n_estimators=100, random_state=42)
        lr_model = LogisticRegression(max_iter=1000, random_state=42)
        
        model = VotingClassifier(
            estimators=[
                ('Random_Forest', rf_model),
                ('Gradient_Boosting', gb_model),
                ('Logistic_Regression', lr_model)
            ],
            voting='soft'
        )
        
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        print("\nCLASSIFICATION")
        print(f"Accuracy (Aniqlik): {accuracy_score(y_test, y_pred):.4f}")
        print("\nClassification Report:\n", classification_report(y_test, y_pred))

    elif task_type == 'regression':

        rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
        gb_model = GradientBoostingRegressor(n_estimators=100, random_state=42)
        lr_model = LinearRegression()
        
        model = VotingRegressor(
            estimators=[
                ('Random_Forest', rf_model),
                ('Gradient_Boosting', gb_model),
                ('Linear_Regression', lr_model)
            ]
        )
        
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        print("\nREGRESSION")
        print(f"R2 Score: {r2_score(y_test, y_pred):.4f}")
        print(f"MAE (Ortacha absolyut xato): {mean_absolute_error(y_test, y_pred):.4f}")
        print(f"MSE (Ortacha kvadratik xato): {mean_squared_error(y_test, y_pred):.4f}")
        
    else:
        raise ValueError("classification yoki regression bo'lishi kerak")

    return model
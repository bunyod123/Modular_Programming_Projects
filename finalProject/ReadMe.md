# ⚡ Elektromobillar Narxini Bashorat Qilish (EV Price Prediction)

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Pandas](https://img.shields.io/badge/Data_Processing-Pandas-green.svg)
![Scikit-Learn](https://img.shields.io/badge/Machine_Learning-Scikit_Learn-orange.svg)

Bu loyiha bozordagi turli zamonaviy elektromobillarning texnik ko'rsatkichlariga (batareya sig'imi, tezlanish, energiya sarfi va h.k.) asoslanib, ularning **bozor narxini** bashorat qilish uchun mo'ljallangan Machine Learning modelini o'z ichiga oladi.

## 📊 Ma'lumotlar To'plami (Dataset)

Modelni o'qitish uchun ishlatilgan `car_data.csv` fayli o'zida quyidagi muhim xususiyatlarni (features) jamlagan:

* **Name:** Avtomobil rusumi (masalan, *Tesla Model Y, BMW iX3*)
* **Range_km:** Bir to'la zaryad bilan yurish masofasi (km)
* **Efficiency:** Energiya samaradorligi (Wh/km)
* **Weight:** Avtomobil og'irligi (kg)
* **Acceleration(0-100):** 0 dan 100 km/soat gacha tezlanish vaqti (sekund)
* **Battery_kWh:** Batareya sig'imi (kVt/soat)
* **Fast_charger(kW):** Maksimal tez zaryadlash quvvati
* **Towing_kg / Cargo_volume:** Tortish qobiliyati va yukxona hajmi
* **Price:** Avtomobil narxi (Target variable - bashorat qilinadigan o'zgaruvchi)

## 🛠️ Ma'lumotlarni Qayta Ishlash (Feature Engineering)

Modelni qurishdan oldin ma'lumotlar ustida quyidagi tozalash ishlari amalga oshirildi:
1. `Price` ustunidagi Yevro belgisi (`€`) va vergullar (`,`) olib tashlanib, qatorlar sonli (numeric) turga o'tkazildi.
2. Yetishmayotgan qiymatlar (Missing values) to'ldirildi.
3. Model uchun muhim bo'lmagan matnli ustunlar kodlandi (Encoding).

## 🧠 Model Arxitekturasi

Loyihada **Regressiya** algoritmlaridan foydalanildi. Agar loyiha ham narxni, ham zaryad masofasini bashorat qilsa, **Multi-Output Regression** yondashuvi qo'llaniladi.

* **Algoritm:** [Masalan: Random Forest Regressor / XGBoost]
* **Metrikalar:** * Mean Absolute Error (MAE): `Kiritilishi kerak`
  * R-squared ($R^2$): `Kiritilishi kerak`

## 🚀 O'rnatish va Ishga Tushirish

Loyihani o'z kompyuteringizda ishga tushirish uchun quyidagi qadamlarni bajaring:

1. Repozitoriyni yuklab oling:
```bash
git clone [https://github.com/username/ev-price-prediction.git](https://github.com/username/ev-price-prediction.git)
cd ev-price-prediction
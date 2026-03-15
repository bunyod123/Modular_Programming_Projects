# 🚗 EV Price and Range Predictor (Multi-Output Classification)

Ushbu loyiha elektromobillarning (EV) texnik xususiyatlariga asoslanib, ularning **narx toifasi (`Price_level`)** va **yurish masofasi toifasini (`Range_km_level`)** bir vaqtning o'zida bashorat qiluvchi mashinali o'rganish (Machine Learning) modelini o'z ichiga oladi. 

Loyiha ma'lumotlarni yig'ish, modelni ko'p maqsadli (multi-output) o'qitish, giperparametrlarni aqlli optimizatsiya qilish va natijalarni interpretatsiya qilish qadamlaridan iborat.

## 📊 Ma'lumotlar bazasi (Dataset)
Ma'lumotlar dastlab maxsus web scraping skriptlari (Playwright kutubxonasi yordamida) orqali elektromobillar haqidagi ochiq ma'lumotlar bazalaridan (masalan, ev-database) yig'ilgan. 

Asosiy fayl: `sampled_data.csv`
Model uchun ishlatilgan asosiy xususiyatlar (Features):
* `Efficiency` (Samaradorlik)
* `Battery_kWh` (Batareya sig'imi)
* `Acceleration(0-100)` (Tezlanish)
* `Weight_kg` (Og'irlik)
* `Fast_charger(kW)` (Tez quvvatlash imkoniyati)
* va boshqa muhim texnik parametrlar...

**Maqsadli o'zgaruvchilar (Targets):**
1. `Range_km_level` - Bir marta quvvatlash orqali bosib o'tiladigan masofa toifasi (Masalan: 0, 1, 2)
2. `Price_level` - Elektromobilning narx toifasi (Masalan: 0, 1, 2)

## 🛠️ Loyiha arxitekturasi va texnologiyalar

Loyiha quyidagi zamonaviy Python kutubxonalari asosida qurilgan:
* **Pandas & NumPy:** Ma'lumotlarni tozalash va qayta ishlash.
* **Scikit-Learn:** Modelni qurish (`MultiOutputClassifier`), ma'lumotlarni qismlarga ajratish va baholash.
* **XGBoost:** Asosiy tasniflash (classification) algoritmi sifatida.
* **Optuna:** Giperparametrlarni Bayes optimizatsiyasi orqali tez va samarali tuning qilish.
* **SHAP (SHapley Additive exPlanations):** Model qarorlarini tushuntirib berish va vizualizatsiya qilish.

* `plotly express linki` https://0ec73db1-58d3-4a8b-a266-e871cc327dbd.plotly.app
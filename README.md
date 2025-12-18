# Weather Data Analyzer

A command-line based Python project for analyzing historical weather data. This project demonstrates data cleaning, exploratory data analysis (EDA), filtering, statistical analysis, and basic data visualization using **pandas** and **matplotlib**.

---

## 📌 Features

* Load and clean real-world weather data
* Handle missing values safely
* Convert and process date-time data
* Filter data by **year** or **month**
* Perform statistical analysis (mean, median, std, min, max)
* Visualize trends and distributions
* Modular and reusable code structure

---

## 🗂 Project Structure

```
WeatherDataAnalyzer/
│
├── weatherMain.py        # Main program (menu-driven)
├── utils.py              # Utility functions (analysis, filtering, visualization)
├── clipData.py           # Dataset preprocessing and clipping script
├── data/
│   └── weatherData2012.csv
└── README.md
```

---

## 📊 Dataset

* Original dataset: **Madrid Daily Weather (1997–2015)**
* Processed subset: **Weather data for year 2012**

### Columns used:

* `date`
* `max_temperature`
* `min_temperature`
* `max_humidity`
* `min_humidity`
* `precipitation`

---

## ⚙️ Requirements

Install the required Python libraries:

```bash
pip install pandas matplotlib
```

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/YugalThapa/WeatherDataAnalyzer.git
cd WeatherDataAnalyzer
```

2. Run the main program:

```bash
python weatherMain.py
```

3. Use the interactive menu to:

* View data overview
* Filter data (yearly / monthly)
* Perform statistical analysis
* Visualize weather trends

---

## 📈 Data Visualization

The project includes:

* Line plots (trend over observations)
* Histograms (distribution)
* Boxplots (outlier detection)

Visualization is implemented using **matplotlib**.

---

## 🧠 Learning Outcomes

This project helps in understanding:

* Practical pandas data manipulation
* Handling missing values correctly
* Writing modular Python code
* Separating logic into reusable functions
* Preparing datasets for future ML workflows

---

## 🚀 Future Improvements

* Time-based plots using `date` on x-axis
* Advanced aggregation (weekly / monthly averages)
* Export analysis reports
* Integrate basic Machine Learning models

---

## 👤 Author

**Yugal Thapa**
Undergraduate – Electronics, Communication & Information Engineering

---

## 📄 License

This project is for learning and educational purposes.

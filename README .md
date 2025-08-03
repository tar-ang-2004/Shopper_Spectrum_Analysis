# 🛍️ Shopper Spectrum - Customer Analytics Dashboard

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📋 Overview

**Shopper Spectrum** is a comprehensive customer segmentation and retail analytics platform that leverages machine learning to provide actionable insights for retail businesses. The project combines advanced data analysis, customer segmentation using K-means clustering, and interactive visualizations to help businesses understand their customer base and optimize their strategies.

### 🎯 Key Features

- **Customer Segmentation**: RFM (Recency, Frequency, Monetary) analysis with K-means clustering
- **Interactive Dashboard**: Streamlit-powered web application with dark/light mode
- **Product Recommendations**: Collaborative filtering recommendation system
- **Geographic Analysis**: Country-wise performance analytics
- **Time Pattern Analysis**: Temporal trends and seasonal insights
- **Customer Explorer**: Advanced filtering and search capabilities
- **Statistical Testing**: Hypothesis testing for business insights

## 🏗️ Project Structure

```
📦 Shopper Spectrum
├── 📊 shopper_spectrum_analysis.ipynb   # Main analysis notebook
├── 🖥️ streamlit_app.py                 # Interactive dashboard
├── 📄 online_retail.csv                # Source dataset
├── 📁 Generated CSV files/             # Processed data files
│   ├── customer_segments.csv
│   ├── cluster_characteristics.csv
│   ├── product_analysis.csv
│   ├── geographical_analysis.csv
│   ├── time_analysis.csv
│   └── retail_data_sample.csv
├── 📁 Charts/                          # Generated visualizations
├── 📁 Streamlit App Screenshots/       # App screenshots
├── 📊 summary_stats.json              # Key metrics summary
├── 🔧 requirements.txt                # Dependencies
├── 📚 Shopper Spectrum.pdf            # Project documentation
└── 📖 README.md                       # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd shopper-spectrum
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the analysis notebook** (if data files don't exist)
   ```bash
   jupyter notebook shopper_spectrum_analysis.ipynb
   ```
   Execute all cells to generate the required CSV files and analysis.

5. **Launch the Streamlit dashboard**
   ```bash
   streamlit run streamlit_app.py
   ```

6. **Open your browser** and navigate to `http://localhost:8501`

## 📊 Dashboard Features

### 🌙 Dark Mode Support
Toggle between light and dark themes for comfortable viewing in any environment.

### 📈 Overview Dashboard
- **Key Metrics**: Revenue, customers, orders, and segmentation overview
- **Revenue Distribution**: Interactive pie charts by customer segments
- **Time Trends**: Daily revenue patterns and growth analysis
- **Business Insights**: Automated key findings and recommendations

### 👥 Customer Segments
- **RFM Analysis**: Recency, Frequency, Monetary value segmentation
- **Cluster Characteristics**: Detailed segment profiles and statistics
- **Customer Lifetime Value**: CLV estimation and distribution analysis
- **Interactive Exploration**: Drill-down capabilities for each segment

### 🛒 Product Analysis
- **Performance Matrix**: Star products, premium products, volume products
- **Revenue Leaders**: Top-performing products by various metrics
- **Category Analysis**: Product categorization and performance insights

### 🌍 Geographic Analysis
- **Country Performance**: Revenue and customer distribution by geography
- **Market Insights**: Average order value and customer behavior by region
- **Growth Opportunities**: Identification of high-potential markets

### ⏰ Time Patterns
- **Temporal Trends**: Daily, hourly, and seasonal patterns
- **Sales Heatmaps**: Visual representation of peak selling times
- **Forecasting Insights**: Historical trends for strategic planning

### 🔍 Customer Explorer
- **Advanced Filtering**: Multi-criteria customer search and analysis
- **Customer Profiles**: Detailed individual customer insights
- **Behavioral Analysis**: Purchase patterns and preferences

### 🎯 Product Recommendations
- **Collaborative Filtering**: AI-powered product recommendation engine
- **Similarity Analysis**: Find products based on customer behavior
- **Cross-selling Opportunities**: Identify bundling possibilities

## 🔬 Technical Implementation

### Machine Learning Models
- **K-means Clustering**: Customer segmentation with optimal cluster selection
- **RFM Scoring**: Quantitative customer value assessment
- **Cosine Similarity**: Product recommendation algorithm
- **Statistical Testing**: Hypothesis validation for business decisions

### Data Processing Pipeline
1. **Data Cleaning**: Handling missing values, outliers, and data quality issues
2. **Feature Engineering**: Creating derived metrics and temporal features
3. **Normalization**: Scaling features for machine learning algorithms
4. **Dimensionality Reduction**: PCA for visualization and analysis

### Technologies Used
- **Backend**: Python, Pandas, NumPy, Scikit-learn
- **Visualization**: Plotly, Matplotlib, Seaborn
- **Web Framework**: Streamlit
- **Statistics**: SciPy for hypothesis testing
- **Data Storage**: CSV files for processed data

## 📈 Business Insights

The analysis provides actionable insights including:

- **Customer Segmentation**: Identify high-value, at-risk, and potential customers
- **Product Performance**: Understand star products vs. underperformers
- **Geographic Opportunities**: Optimize market expansion strategies
- **Temporal Patterns**: Optimize inventory and marketing timing
- **Cross-selling**: Increase average order value through recommendations

## 🔧 Configuration

### Environment Variables
No environment variables required for basic setup.

### Customization Options
- **Clustering Parameters**: Modify K-means settings in the notebook
- **Recommendation Engine**: Adjust similarity thresholds and recommendation count
- **Visualization Themes**: Customize color schemes and chart types
- **Data Filters**: Modify date ranges and customer criteria

## 📱 Screenshots

| Dashboard View | Customer Segments | Product Recommendations |
|:--------------:|:-----------------:|:----------------------:|
| ![Overview](Streamlit%20App%20Screenshots/overview.png) | ![Segments](Streamlit%20App%20Screenshots/segments.png) | ![Recommendations](Streamlit%20App%20Screenshots/recommendations.png) |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Dataset**: Online Retail Dataset from UCI Machine Learning Repository
- **Streamlit**: For the amazing web framework
- **Plotly**: For interactive visualizations
- **Scikit-learn**: For machine learning capabilities

## 📞 Contact

For questions, suggestions, or collaboration opportunities, please reach out:

- **Email**: tarangkishor704@gmail.com
---

⭐ **Star this repository if you find it helpful!** ⭐

*Built with ❤️ for data-driven retail insights*
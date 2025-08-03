# 🛍️ Shopper Spectrum - Customer Analytics Dashboard

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/tar-ang-2004/Shopper_Spectrum_Analysis.svg)](https://github.com/tar-ang-2004/Shopper_Spectrum_Analysis/stargazers)

## 🎯 Overview

**Shopper Spectrum** is a comprehensive customer segmentation and retail analytics platform that leverages machine learning to provide actionable insights for retail businesses. This project combines advanced data analysis, customer segmentation using K-means clustering, RFM analysis, and interactive visualizations to help businesses understand their customer base and optimize their strategies.

### ✨ Key Features

- 🎯 **Customer Segmentation**: Advanced RFM (Recency, Frequency, Monetary) analysis with K-means clustering
- 📊 **Interactive Dashboard**: Streamlit-powered web application with dark/light mode toggle
- 🤖 **Product Recommendations**: AI-powered collaborative filtering recommendation system
- 🌍 **Geographic Analysis**: Country-wise performance analytics and market insights
- ⏰ **Time Pattern Analysis**: Temporal trends, seasonal patterns, and sales forecasting
- 🔍 **Customer Explorer**: Advanced filtering, search capabilities, and customer profiling
- 📈 **Statistical Testing**: Hypothesis testing for data-driven business insights
- 📱 **Responsive Design**: Mobile-friendly interface with professional styling

## 🏗️ Project Structure

```
📦 Shopper_Spectrum_Analysis/
├── 📊 Charts/                          # Generated visualizations
│   ├── 3D RFM Analysis.png             # 3D customer segmentation plot
│   ├── Correlation Matrix.png          # Feature correlation heatmap
│   ├── Distributions.png               # Data distribution analysis
│   ├── Geographical Analysis.png       # Geographic performance maps
│   ├── K-Mean Clustering.png           # Clustering visualization
│   └── Product Analysis.png            # Product performance charts
├── 📁 Generated CSV files/             # Processed datasets
│   ├── cluster_characteristics.csv     # Segment profiles and statistics
│   ├── customer_segments.csv           # Customer segmentation results
│   ├── geographical_analysis.csv       # Country-wise performance data
│   ├── product_analysis.csv            # Product performance metrics
│   ├── retail_data_sample.csv          # Cleaned and processed dataset
│   ├── time_analysis.csv               # Temporal analysis results
│   └── transaction_summary.csv         # Transaction-level insights
├── 📱 Streamlit App Screenshots/       # Dashboard demonstration
│   ├── Screenshot 2025-08-01 185339.png
│   ├── Screenshot 2025-08-01 185348.png
│   ├── Screenshot 2025-08-03 143755.png
│   ├── Screenshot 2025-08-03 143806.png
│   └── Screenshot 2025-08-03 143817.png
├── 🤖 model_info.pkl                   # Machine learning model metadata
├── 🔧 scaler.pkl                       # Feature scaling transformer
├── 📊 summary_stats.json               # Key business metrics summary
├── 📄 Shopper Spectrum.pdf             # Comprehensive project documentation
├── 🖥️ streamlit_app.py                 # Main dashboard application
├── 📓 shopper_spectrum_analysis.ipynb  # Complete data analysis notebook
├── 📋 requirements.txt                 # Python dependencies
├── 📖 README.md                        # This documentation file
├── 📜 LICENSE                          # MIT license
└── 🚫 .gitignore                       # Git ignore configuration
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager
- 8GB+ RAM recommended for large dataset processing

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/tar-ang-2004/Shopper_Spectrum_Analysis.git
   cd Shopper_Spectrum_Analysis
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

4. **Launch the Streamlit dashboard**
   ```bash
   streamlit run streamlit_app.py
   ```

5. **Open your browser** and navigate to `http://localhost:8501`

### Running the Complete Analysis

If you want to run the full analysis from scratch:

1. **Download the dataset** from [UCI ML Repository - Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/online+retail)
2. **Place it as `online_retail.csv`** in the project root
3. **Open and run the Jupyter notebook**:
   ```bash
   jupyter notebook shopper_spectrum_analysis.ipynb
   ```
4. **Execute all cells** to regenerate all analysis files and visualizations

## 📊 Dashboard Features

### 🌙 Dark Mode Support
Toggle between light and dark themes for comfortable viewing in any environment with the moon/sun button in the top-right corner.

### 📈 Overview Dashboard
- **Key Business Metrics**: Total revenue, customers, orders, and segment overview
- **Revenue Distribution**: Interactive pie charts showing revenue by customer segments
- **Time Trends**: Daily revenue patterns and growth analysis
- **Automated Insights**: AI-generated key findings and business recommendations

### 👥 Customer Segments
- **RFM Analysis**: Comprehensive Recency, Frequency, Monetary value segmentation
- **Cluster Characteristics**: Detailed profiles for each customer segment
- **Customer Lifetime Value**: CLV estimation and distribution analysis
- **Interactive Exploration**: Drill-down capabilities with radar charts and scatter plots

### 🛒 Product Analysis
- **Performance Matrix**: Categorization into Star Products, Premium Products, Volume Products
- **Revenue Leaders**: Top-performing products by various metrics
- **Category Analysis**: Product categorization and cross-category insights
- **BCG-style Matrix**: Strategic product portfolio analysis

### 🌍 Geographic Analysis
- **Global Performance**: Revenue and customer distribution by country
- **Market Insights**: Average order value and customer behavior by region
- **Growth Opportunities**: Identification of high-potential markets
- **Interactive Maps**: Geographic visualization of business performance

### ⏰ Time Patterns
- **Temporal Trends**: Daily, hourly, monthly, and seasonal patterns
- **Sales Heatmaps**: Visual representation of peak selling times
- **Forecasting Insights**: Historical trends for strategic planning
- **Customer Acquisition**: Timeline analysis of customer growth

### 🔍 Customer Explorer
- **Advanced Filtering**: Multi-criteria customer search and analysis
- **Customer Profiles**: Detailed individual customer insights and purchase history
- **Behavioral Analysis**: Purchase patterns, preferences, and lifecycle stages
- **Custom Segments**: Create and analyze custom customer groups

### 🎯 Product Recommendations
- **Collaborative Filtering**: AI-powered product recommendation engine using cosine similarity
- **Similarity Analysis**: Find products based on customer purchase behavior
- **Cross-selling Opportunities**: Identify product bundling possibilities
- **Performance Metrics**: Recommendation accuracy and similarity scores

## 🔬 Technical Implementation

### Machine Learning Models
- **K-means Clustering**: Customer segmentation with optimal cluster selection using elbow method and silhouette analysis
- **RFM Scoring**: Quantitative customer value assessment with quintile-based scoring
- **Cosine Similarity**: Product recommendation algorithm based on user-item interactions
- **Statistical Testing**: Hypothesis validation using t-tests and ANOVA for business decisions

### Data Processing Pipeline
1. **Data Cleaning**: Handling missing values, duplicates, and outlier detection using IQR method
2. **Feature Engineering**: Creating derived metrics, temporal features, and behavioral indicators
3. **Normalization**: StandardScaler for clustering algorithms and similarity calculations
4. **Dimensionality Reduction**: PCA for visualization and noise reduction

### Technologies Used
- **Backend**: Python, Pandas, NumPy, Scikit-learn
- **Visualization**: Plotly (interactive), Matplotlib, Seaborn
- **Web Framework**: Streamlit with custom CSS styling
- **Statistics**: SciPy for hypothesis testing and statistical analysis
- **Data Storage**: CSV files for processed data, Pickle for model persistence

## 📈 Business Insights & Impact

The analysis provides actionable insights including:

- **Customer Segmentation**: Identify high-value customers (20% generate 80% revenue), at-risk customers for retention campaigns
- **Product Performance**: Discover star products vs. underperformers, optimize inventory management
- **Geographic Opportunities**: Market expansion strategies, regional customization opportunities
- **Temporal Patterns**: Optimize marketing timing, inventory planning, and resource allocation
- **Cross-selling**: Increase average order value through AI-powered recommendations (average 15-25% uplift)

### Key Findings from Analysis
- 🎯 **Top 20% of customers** generate **80% of total revenue**
- 💎 **High-value segment** shows **3x higher CLV** than average customers
- 🌍 **UK market dominates** with **85%+ of total revenue**
- 🛒 **Peak sales hours**: **10 AM - 3 PM GMT**
- 📦 **Top product categories** account for **60% of sales volume**

## 🎨 Screenshots

| Overview Dashboard | Customer Segmentation | Product Recommendations |
|:-----------------:|:---------------------:|:-----------------------:|
| ![Overview](Streamlit%20App%20Screenshots/Screenshot%202025-08-03%20143755.png) | ![Segments](Streamlit%20App%20Screenshots/Screenshot%202025-08-03%20143806.png) | ![Recommendations](Streamlit%20App%20Screenshots/Screenshot%202025-08-03%20143817.png) |

## 🔧 Configuration & Customization

### Environment Variables
No environment variables required for basic setup. All configuration is handled through the Streamlit interface.

### Customization Options
- **Clustering Parameters**: Modify K-means settings in the notebook (n_clusters, random_state)
- **RFM Scoring**: Adjust quintile thresholds for different business contexts
- **Recommendation Engine**: Tune similarity thresholds and recommendation count
- **Visualization Themes**: Customize color schemes and chart types in the app
- **Data Filters**: Modify date ranges, customer criteria, and business rules

### Performance Optimization
- **Data Caching**: Streamlit @st.cache_data for faster loading
- **Lazy Loading**: Charts generated on-demand to reduce initial load time
- **Memory Management**: Optimized data structures for large datasets

## 📊 Data Schema

### Customer Segments Schema
```python
{
    'CustomerID': 'Unique customer identifier',
    'Recency': 'Days since last purchase',
    'Frequency': 'Number of transactions',
    'Monetary': 'Total amount spent',
    'R_Score': 'Recency score (1-5)',
    'F_Score': 'Frequency score (1-5)',
    'M_Score': 'Monetary score (1-5)',
    'RFM_Score': 'Combined RFM score',
    'Cluster': 'Customer segment (0-4)',
    'CLV_Estimate': 'Customer Lifetime Value prediction'
}
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add comments for complex algorithms
- Update documentation for new features
- Test all functionality before submitting

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Dataset**: Online Retail Dataset from UCI Machine Learning Repository
- **Streamlit**: For the amazing web framework enabling rapid dashboard development
- **Plotly**: For interactive and beautiful data visualizations
- **Scikit-learn**: For machine learning capabilities and clustering algorithms
- **Pandas & NumPy**: For efficient data manipulation and analysis

## 📞 Contact & Support

For questions, suggestions, or collaboration opportunities:

- **GitHub**: [tar-ang-2004](https://github.com/tar-ang-2004)
- **Repository**: [Shopper_Spectrum_Analysis](https://github.com/tar-ang-2004/Shopper_Spectrum_Analysis)
- **Issues**: [Report Bug / Request Feature](https://github.com/tar-ang-2004/Shopper_Spectrum_Analysis/issues)

## 🎯 Future Enhancements

- [ ] **Real-time Analytics**: Integration with live data streams
- [ ] **Advanced ML Models**: Deep learning for customer behavior prediction
- [ ] **API Development**: REST API for programmatic access
- [ ] **Database Integration**: PostgreSQL/MongoDB support
- [ ] **A/B Testing Framework**: Built-in experimentation platform
- [ ] **Mobile App**: React Native companion app
- [ ] **Cloud Deployment**: AWS/Azure containerized deployment

---

⭐ **Star this repository if you find it helpful!** ⭐

*Built with ❤️ for data-driven retail insights and customer analytics*

## 📚 Additional Resources

- [Jupyter Notebook with Complete Analysis](shopper_spectrum_analysis.ipynb)
- [Project Documentation PDF](Shopper%20Spectrum.pdf)
- [Generated Visualizations](Charts/)
- [Processed Datasets](Generated%20CSV%20files/)
- [Dashboard Screenshots](Streamlit%20App%20Screenshots/)

**Last Updated**: August 3, 2025

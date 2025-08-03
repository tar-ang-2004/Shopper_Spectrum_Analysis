import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib.pyplot as plt
import json
import pickle
from datetime import datetime, timedelta
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

# Configure Streamlit page
st.set_page_config(
    page_title="Shopper Spectrum - Customer Analytics",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state for dark mode
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

# Dark mode toggle function
def toggle_dark_mode():
    st.session_state.dark_mode = not st.session_state.dark_mode

# Get theme colors based on mode
def get_theme_colors():
    if st.session_state.dark_mode:
        return {
            'bg_color': '#0e1117',
            'secondary_bg': '#262730',
            'text_color': '#fafafa',
            'accent_color': '#ff6b6b',
            'card_bg': '#1e2124',
            'border_color': '#404040',
            'metric_bg': '#2d3436'
        }
    else:
        return {
            'bg_color': '#ffffff',
            'secondary_bg': '#f0f2f6',
            'text_color': '#262730',
            'accent_color': '#1f77b4',
            'card_bg': '#f8f9fa',
            'border_color': '#e0e0e0',
            'metric_bg': '#f0f2f6'
        }

# Get current theme
theme = get_theme_colors()

# Function to update chart layout for dark mode
def update_chart_layout(fig):
    """Update chart layout for current theme"""
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color=theme['text_color'],
        title_font_color=theme['text_color']
    )
    return fig

# Custom CSS for better styling with dark mode support
st.markdown(f"""
<style>
    .main-header {{
        font-size: 3rem;
        font-weight: bold;
        color: {theme['accent_color']};
        text-align: center;
        margin-bottom: 2rem;
    }}
    .metric-card {{
        background-color: {theme['metric_bg']};
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid {theme['accent_color']};
    }}
    .insight-box {{
        background-color: {theme['card_bg']};
        color: {theme['text_color']};
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #17a2b8;
        margin: 1rem 0;
        border: 1px solid {theme['border_color']};
    }}
    .recommendation-card {{
        border: 1px solid {theme['border_color']}; 
        border-radius: 8px; 
        padding: 15px; 
        margin: 10px 0;
        background-color: {theme['card_bg']};
        border-left: 4px solid {theme['accent_color']};
        color: {theme['text_color']};
    }}
    .recommendation-card h4 {{
        color: {theme['accent_color']}; 
        margin: 0 0 10px 0;
    }}
    .dark-mode-toggle {{
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 999;
        background-color: {theme['accent_color']};
        color: white;
        border: none;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        font-size: 20px;
        cursor: pointer;
        box-shadow: 0 2px 10px rgba(0,0,0,0.2);
    }}
    .stApp {{
        background-color: {theme['bg_color']};
        color: {theme['text_color']};
    }}
</style>
""", unsafe_allow_html=True)

# Title and Header
st.markdown('<div class="main-header">🛍️ Shopper Spectrum</div>', unsafe_allow_html=True)
st.markdown("### Customer Segmentation & Retail Analytics Dashboard")

# Dark mode toggle in top-right corner
col1, col2 = st.columns([6, 1])
with col2:
    if st.button("🌙" if not st.session_state.dark_mode else "☀️", 
                help="Toggle dark/light mode",
                on_click=toggle_dark_mode,
                key="dark_mode_toggle"):
        st.rerun()

st.markdown("---")

# Sidebar Navigation
st.sidebar.title("📊 Navigation")
page = st.sidebar.selectbox(
    "Choose Analysis View",
    ["📈 Overview Dashboard", "👥 Customer Segments", "🛒 Product Analysis", 
     "🌍 Geographic Analysis", "⏰ Time Patterns", "🔍 Customer Explorer", "🎯 Product Recommendations"]
)

# Load data function
@st.cache_data
def load_data():
    """Load all necessary data files"""
    try:
        # Load summary stats
        with open('summary_stats.json', 'r') as f:
            summary_stats = json.load(f)
        
        # Load main datasets from Generated CSV files folder
        customer_segments = pd.read_csv('Generated CSV files/customer_segments.csv')
        cluster_characteristics = pd.read_csv('Generated CSV files/cluster_characteristics.csv')
        product_analysis = pd.read_csv('Generated CSV files/product_analysis.csv')
        geographical_analysis = pd.read_csv('Generated CSV files/geographical_analysis.csv')
        time_analysis = pd.read_csv('Generated CSV files/time_analysis.csv')
        retail_sample = pd.read_csv('Generated CSV files/retail_data_sample.csv')
        
        # Convert date columns
        retail_sample['InvoiceDate'] = pd.to_datetime(retail_sample['InvoiceDate'])
        time_analysis['Date'] = pd.to_datetime(time_analysis['Date'])
        
        return {
            'summary_stats': summary_stats,
            'customer_segments': customer_segments,
            'cluster_characteristics': cluster_characteristics,
            'product_analysis': product_analysis,
            'geographical_analysis': geographical_analysis,
            'time_analysis': time_analysis,
            'retail_sample': retail_sample
        }
    except FileNotFoundError as e:
        st.error(f"Data file not found: {e}")
        st.error("Please run the Jupyter notebook first to generate the required data files.")
        return None

# Load all data
data = load_data()

if data is None:
    st.stop()

# Extract data
summary_stats = data['summary_stats']
customer_segments = data['customer_segments']
cluster_characteristics = data['cluster_characteristics']
product_analysis = data['product_analysis']
geographical_analysis = data['geographical_analysis']
time_analysis = data['time_analysis']
retail_sample = data['retail_sample']

# Overview Dashboard
if page == "📈 Overview Dashboard":
    st.header("📈 Business Overview")
    
    # Key Metrics Row
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Total Revenue", f"${summary_stats['total_revenue']:,.0f}")
    with col2:
        st.metric("Total Customers", f"{summary_stats['total_customers']:,}")
    with col3:
        st.metric("Total Orders", f"{summary_stats['total_orders']:,}")
    with col4:
        st.metric("Avg Order Value", f"${summary_stats['avg_order_value']:.2f}")
    with col5:
        st.metric("Customer Segments", f"{summary_stats['cluster_info']['n_clusters']}")
    
    st.markdown("---")
    
    # Revenue Trends and Customer Distribution
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Revenue by Customer Segment")
        cluster_revenue = customer_segments.groupby('Cluster')['Monetary'].sum().reset_index()
        cluster_revenue['Percentage'] = (cluster_revenue['Monetary'] / cluster_revenue['Monetary'].sum()) * 100
        
        fig_pie = px.pie(
            cluster_revenue, 
            values='Monetary', 
            names='Cluster',
            title="Revenue Distribution by Segment",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig_pie.update_traces(textposition='inside', textinfo='percent+label')
        fig_pie = update_chart_layout(fig_pie)
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        st.subheader("👥 Customer Distribution")
        cluster_counts = customer_segments['Cluster'].value_counts().reset_index()
        cluster_counts.columns = ['Cluster', 'Count']
        
        fig_bar = px.bar(
            cluster_counts, 
            x='Cluster', 
            y='Count',
            title="Number of Customers by Segment",
            color='Cluster',
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig_bar = update_chart_layout(fig_bar)
        st.plotly_chart(fig_bar, use_container_width=True)
    
    # Daily Revenue Trend
    st.subheader("📈 Daily Revenue Trend")
    daily_revenue = time_analysis.groupby('Date')['Revenue'].sum().reset_index()
    
    fig_line = px.line(
        daily_revenue, 
        x='Date', 
        y='Revenue',
        title="Daily Revenue Over Time",
        line_shape='spline'
    )
    fig_line.update_layout(xaxis_title="Date", yaxis_title="Revenue ($)")
    fig_line = update_chart_layout(fig_line)
    st.plotly_chart(fig_line, use_container_width=True)
    
    # Top Insights
    st.subheader("🔍 Key Insights")
    
    # Calculate insights
    top_cluster = customer_segments.groupby('Cluster')['Monetary'].sum().idxmax()
    top_cluster_revenue_pct = (customer_segments[customer_segments['Cluster'] == top_cluster]['Monetary'].sum() / 
                              customer_segments['Monetary'].sum()) * 100
    
    avg_clv = customer_segments['CLV_Estimate'].mean()
    high_value_customers = len(customer_segments[customer_segments['CLV_Estimate'] > avg_clv * 2])
    
    insights = [
        f"🎯 Cluster {top_cluster} generates {top_cluster_revenue_pct:.1f}% of total revenue",
        f"💎 {high_value_customers} customers have CLV 2x above average",
        f"🌍 Business operates in {summary_stats['unique_countries']} countries",
        f"🛒 Average customer makes {customer_segments['Frequency'].mean():.1f} orders",
        f"⏱️ Analysis covers {summary_stats['analysis_period_days']} days of data"
    ]
    
    for insight in insights:
        st.markdown(f'<div class="insight-box">{insight}</div>', unsafe_allow_html=True)

# Customer Segments Page
elif page == "👥 Customer Segments":
    st.header("👥 Customer Segmentation Analysis")
    
    # Segment Overview
    st.subheader("📊 Segment Characteristics")
    
    # Display cluster characteristics table
    st.dataframe(
        cluster_characteristics.style.format({
            'Recency_mean': '{:.1f}',
            'Frequency_mean': '{:.1f}',
            'Monetary_mean': '${:.2f}',
            'CustomerID_count': '{:.0f}'
        }),
        use_container_width=True
    )
    
    # RFM Analysis Visualization
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 RFM Distribution by Segment")
        
        # Create RFM radar chart
        fig_radar = go.Figure()
        
        for cluster in sorted(customer_segments['Cluster'].unique()):
            cluster_data = customer_segments[customer_segments['Cluster'] == cluster]
            
            # Normalize RFM scores for radar chart
            r_score = cluster_data['R_Score'].mean()
            f_score = cluster_data['F_Score'].mean()
            m_score = cluster_data['M_Score'].mean()
            
            fig_radar.add_trace(go.Scatterpolar(
                r=[r_score, f_score, m_score, r_score],
                theta=['Recency', 'Frequency', 'Monetary', 'Recency'],
                fill='toself',
                name=f'Cluster {cluster}'
            ))
        
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 5]
                )),
            showlegend=True,
            title="RFM Scores by Segment"
        )
        
        st.plotly_chart(fig_radar, use_container_width=True)
    
    with col2:
        st.subheader("💰 Customer Lifetime Value")
        
        fig_clv = px.box(
            customer_segments,
            x='Cluster',
            y='CLV_Estimate',
            title="CLV Distribution by Segment",
            color='Cluster',
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig_clv.update_layout(yaxis_title="Estimated CLV ($)")
        st.plotly_chart(fig_clv, use_container_width=True)
    
    # Segment Deep Dive
    st.subheader("🔍 Segment Deep Dive")
    
    selected_cluster = st.selectbox("Select Segment for Detailed Analysis", 
                                   sorted(customer_segments['Cluster'].unique()))
    
    cluster_data = customer_segments[customer_segments['Cluster'] == selected_cluster]
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Customers", f"{len(cluster_data):,}")
    with col2:
        st.metric("Avg Recency", f"{cluster_data['Recency'].mean():.1f} days")
    with col3:
        st.metric("Avg Frequency", f"{cluster_data['Frequency'].mean():.1f}")
    with col4:
        st.metric("Avg Monetary", f"${cluster_data['Monetary'].mean():.2f}")
    
    # Segment characteristics
    col1, col2 = st.columns(2)
    
    with col1:
        # Recency distribution
        fig_hist = px.histogram(
            cluster_data,
            x='Recency',
            title=f"Recency Distribution - Cluster {selected_cluster}",
            nbins=30
        )
        st.plotly_chart(fig_hist, use_container_width=True)
    
    with col2:
        # Frequency vs Monetary scatter
        fig_scatter = px.scatter(
            cluster_data,
            x='Frequency',
            y='Monetary',
            title=f"Frequency vs Monetary - Cluster {selected_cluster}",
            size='CLV_Estimate',
            hover_data=['CustomerID']
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

# Product Analysis Page
elif page == "🛒 Product Analysis":
    st.header("🛒 Product Performance Analysis")
    
    # Top Products Overview
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏆 Top Products by Revenue")
        top_products_revenue = product_analysis.head(10)
        
        fig_bar = px.bar(
            top_products_revenue,
            x='Total_Revenue',
            y='Description',
            orientation='h',
            title="Top 10 Products by Revenue",
            text='Total_Revenue'
        )
        fig_bar.update_traces(texttemplate='$%{text:,.0f}', textposition='outside')
        fig_bar.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig_bar, use_container_width=True)
    
    with col2:
        st.subheader("📦 Top Products by Quantity")
        top_products_quantity = product_analysis.nlargest(10, 'Total_Quantity')
        
        fig_bar2 = px.bar(
            top_products_quantity,
            x='Total_Quantity',
            y='Description',
            orientation='h',
            title="Top 10 Products by Quantity Sold",
            text='Total_Quantity',
            color='Total_Quantity',
            color_continuous_scale='viridis'
        )
        fig_bar2.update_traces(texttemplate='%{text:,.0f}', textposition='outside')
        fig_bar2.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig_bar2, use_container_width=True)
    
    # Product Performance Matrix
    st.subheader("📊 Product Performance Matrix")
    
    # Create performance categories
    revenue_median = product_analysis['Total_Revenue'].median()
    quantity_median = product_analysis['Total_Quantity'].median()
    
    def categorize_product(row):
        if row['Total_Revenue'] >= revenue_median and row['Total_Quantity'] >= quantity_median:
            return "Star Products"
        elif row['Total_Revenue'] >= revenue_median and row['Total_Quantity'] < quantity_median:
            return "Premium Products"
        elif row['Total_Revenue'] < revenue_median and row['Total_Quantity'] >= quantity_median:
            return "Volume Products"
        else:
            return "Underperformers"
    
    product_analysis['Category'] = product_analysis.apply(categorize_product, axis=1)
    
    fig_scatter = px.scatter(
        product_analysis,
        x='Total_Quantity',
        y='Total_Revenue',
        color='Category',
        size='Unique_Customers',
        hover_data=['Description', 'Avg_Price'],
        title="Product Performance Matrix",
        log_x=True,
        log_y=True
    )
    
    # Add median lines
    fig_scatter.add_hline(y=revenue_median, line_dash="dash", line_color="red", 
                         annotation_text="Revenue Median")
    fig_scatter.add_vline(x=quantity_median, line_dash="dash", line_color="red", 
                         annotation_text="Quantity Median")
    
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    # Product Categories Analysis
    col1, col2 = st.columns(2)
    
    with col1:
        category_summary = product_analysis.groupby('Category').agg({
            'Total_Revenue': 'sum',
            'Description': 'count'
        }).reset_index()
        category_summary.columns = ['Category', 'Revenue', 'Product_Count']
        
        fig_pie = px.pie(
            category_summary,
            values='Revenue',
            names='Category',
            title="Revenue by Product Category"
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        st.subheader("📈 Category Performance")
        st.dataframe(
            category_summary.style.format({
                'Revenue': '${:,.2f}',
                'Product_Count': '{:.0f}'
            }),
            use_container_width=True
        )

# Geographic Analysis Page
elif page == "🌍 Geographic Analysis":
    st.header("🌍 Geographic Performance Analysis")
    
    # Top Countries Overview
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏆 Top Countries by Revenue")
        top_countries = geographical_analysis.head(15)
        
        fig_bar = px.bar(
            top_countries,
            x='Total_Revenue',
            y='Country',
            orientation='h',
            title="Top 15 Countries by Revenue",
            text='Total_Revenue',
            color='Total_Revenue',
            color_continuous_scale='blues'
        )
        fig_bar.update_traces(texttemplate='$%{text:,.0f}', textposition='outside')
        fig_bar.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig_bar, use_container_width=True)
    
    with col2:
        st.subheader("👥 Customer Distribution")
        
        fig_bar2 = px.bar(
            top_countries,
            x='Unique_Customers',
            y='Country',
            orientation='h',
            title="Customer Count by Country",
            text='Unique_Customers',
            color='Unique_Customers',
            color_continuous_scale='greens'
        )
        fig_bar2.update_traces(texttemplate='%{text:,.0f}', textposition='outside')
        fig_bar2.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig_bar2, use_container_width=True)
    
    # Performance Metrics
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💰 Average Order Value by Country")
        top_aov = geographical_analysis.nlargest(15, 'Avg_Order_Value')
        
        fig_bar3 = px.bar(
            top_aov,
            x='Avg_Order_Value',
            y='Country',
            orientation='h',
            title="Highest AOV Countries",
            text='Avg_Order_Value',
            color='Avg_Order_Value',
            color_continuous_scale='oranges'
        )
        fig_bar3.update_traces(texttemplate='$%{text:.2f}', textposition='outside')
        fig_bar3.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig_bar3, use_container_width=True)
    
    with col2:
        st.subheader("📊 Revenue vs Customers Scatter")
        
        fig_scatter = px.scatter(
            geographical_analysis,
            x='Unique_Customers',
            y='Total_Revenue',
            size='Total_Orders',
            hover_name='Country',
            title="Revenue vs Customer Count",
            log_x=True,
            log_y=True
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
    
    # Geographic Performance Table
    st.subheader("📋 Geographic Performance Summary")
    
    display_countries = st.slider("Number of countries to display", 10, 50, 20)
    
    geo_display = geographical_analysis.head(display_countries).style.format({
        'Total_Revenue': '${:,.2f}',
        'Total_Orders': '{:,.0f}',
        'Unique_Customers': '{:,.0f}',
        'Avg_Order_Value': '${:.2f}',
        'Revenue_Per_Customer': '${:.2f}'
    })
    
    st.dataframe(geo_display, use_container_width=True)

# Time Patterns Page
elif page == "⏰ Time Patterns":
    st.header("⏰ Temporal Analysis")
    
    # Daily and Hourly Patterns
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📅 Daily Revenue Trend")
        daily_trend = time_analysis.groupby('Date')['Revenue'].sum().reset_index()
        
        fig_line = px.line(
            daily_trend,
            x='Date',
            y='Revenue',
            title="Daily Revenue Over Time"
        )
        fig_line.update_layout(xaxis_title="Date", yaxis_title="Revenue ($)")
        st.plotly_chart(fig_line, use_container_width=True)
    
    with col2:
        st.subheader("🕐 Hourly Sales Pattern")
        hourly_pattern = time_analysis.groupby('Hour')['Revenue'].sum().reset_index()
        
        fig_bar = px.bar(
            hourly_pattern,
            x='Hour',
            y='Revenue',
            title="Sales by Hour of Day",
            color='Revenue',
            color_continuous_scale='viridis'
        )
        st.plotly_chart(fig_bar, use_container_width=True)
    
    # Monthly Analysis
    if 'retail_sample' in locals():
        st.subheader("📆 Monthly Trends")
        
        retail_sample['Month'] = retail_sample['InvoiceDate'].dt.month
        retail_sample['Year'] = retail_sample['InvoiceDate'].dt.year
        
        monthly_data = retail_sample.groupby(['Year', 'Month']).agg({
            'TotalAmount': 'sum',
            'CustomerID': 'nunique',
            'InvoiceNo': 'nunique'
        }).reset_index()
        
        monthly_data['Period'] = monthly_data['Year'].astype(str) + '-' + monthly_data['Month'].astype(str).str.zfill(2)
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig_monthly = px.line(
                monthly_data,
                x='Period',
                y='TotalAmount',
                title="Monthly Revenue Trend",
                markers=True
            )
            fig_monthly.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig_monthly, use_container_width=True)
        
        with col2:
            fig_customers = px.line(
                monthly_data,
                x='Period',
                y='CustomerID',
                title="Monthly Active Customers",
                markers=True,
                color_discrete_sequence=['orange']
            )
            fig_customers.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig_customers, use_container_width=True)
    
    # Heatmap Analysis
    st.subheader("🔥 Sales Heatmap")
    
    # Create day of week from sample data
    if 'retail_sample' in locals():
        retail_sample['DayOfWeek'] = retail_sample['InvoiceDate'].dt.dayofweek
        retail_sample['DayName'] = retail_sample['InvoiceDate'].dt.day_name()
        
        heatmap_data = retail_sample.groupby(['DayName', 'Hour'])['TotalAmount'].sum().reset_index()
        heatmap_pivot = heatmap_data.pivot(index='DayName', columns='Hour', values='TotalAmount').fillna(0)
        
        # Reorder days
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        heatmap_pivot = heatmap_pivot.reindex(day_order)
        
        fig_heatmap = px.imshow(
            heatmap_pivot,
            title="Sales Heatmap by Day and Hour",
            labels=dict(x="Hour", y="Day of Week", color="Revenue"),
            color_continuous_scale="Viridis"
        )
        st.plotly_chart(fig_heatmap, use_container_width=True)

# Customer Explorer Page
elif page == "🔍 Customer Explorer":
    st.header("🔍 Customer Explorer")
    
    # Customer Search and Filter
    st.subheader("🔎 Find Customers")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        cluster_filter = st.multiselect(
            "Filter by Segment",
            options=sorted(customer_segments['Cluster'].unique()),
            default=sorted(customer_segments['Cluster'].unique())
        )
    
    with col2:
        min_monetary = st.slider(
            "Minimum Total Spent",
            min_value=0,
            max_value=int(customer_segments['Monetary'].max()),
            value=0
        )
    
    with col3:
        min_frequency = st.slider(
            "Minimum Order Count",
            min_value=1,
            max_value=int(customer_segments['Frequency'].max()),
            value=1
        )
    
    # Apply filters
    filtered_customers = customer_segments[
        (customer_segments['Cluster'].isin(cluster_filter)) &
        (customer_segments['Monetary'] >= min_monetary) &
        (customer_segments['Frequency'] >= min_frequency)
    ]
    
    st.write(f"Found {len(filtered_customers):,} customers matching criteria")
    
    # Customer Analysis
    if len(filtered_customers) > 0:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("💰 Value Distribution")
            fig_hist = px.histogram(
                filtered_customers,
                x='Monetary',
                nbins=30,
                title="Customer Value Distribution"
            )
            st.plotly_chart(fig_hist, use_container_width=True)
        
        with col2:
            st.subheader("🎯 RFM Scatter")
            fig_scatter = px.scatter(
                filtered_customers,
                x='Frequency',
                y='Monetary',
                color='Cluster',
                size='CLV_Estimate',
                hover_data=['CustomerID', 'Recency'],
                title="Frequency vs Monetary Value"
            )
            st.plotly_chart(fig_scatter, use_container_width=True)
        
        # Top Customers Table
        st.subheader("👑 Top Customers")
        
        sort_by = st.selectbox(
            "Sort by",
            ['Monetary', 'CLV_Estimate', 'Frequency', 'Recency']
        )
        
        top_customers = filtered_customers.nlargest(20, sort_by)
        
        display_cols = ['CustomerID', 'Cluster', 'Recency', 'Frequency', 'Monetary', 
                       'Avg_Order_Value', 'CLV_Estimate', 'Country']

        st.dataframe(
            top_customers[display_cols].style.format({
                'Recency': '{:.0f}',
                'Frequency': '{:.0f}',
                'Monetary': '${:,.2f}',
                'Avg_Order_Value': '${:.2f}',
                'CLV_Estimate': '${:,.2f}'
            }),
            use_container_width=True
        )

# Product Recommendations Page
elif page == "🎯 Product Recommendations":
    st.header("🎯 Product Recommendation System")
    st.markdown("### Find Similar Products Using Collaborative Filtering")
    
    # Load product data for recommendations
    @st.cache_data
    def prepare_recommendation_data():
        """Prepare data for product recommendations"""
        # Create customer-product matrix
        customer_product_matrix = retail_sample.groupby(['CustomerID', 'Description'])['Quantity'].sum().unstack(fill_value=0)
        
        # Get product information
        product_info = retail_sample.groupby('Description').agg({
            'UnitPrice': 'mean',
            'Quantity': 'sum',
            'CustomerID': 'nunique',
            'TotalAmount': 'sum'
        }).reset_index()
        product_info.columns = ['Description', 'Avg_Price', 'Total_Quantity', 'Unique_Customers', 'Total_Revenue']
        
        return customer_product_matrix, product_info
    
    def get_product_recommendations(product_name, customer_product_matrix, n_recommendations=5):
        """Get product recommendations using collaborative filtering"""
        
        if product_name not in customer_product_matrix.columns:
            return None
        
        # Calculate cosine similarity between products
        product_similarity = cosine_similarity(customer_product_matrix.T)
        
        # Get similarity scores for the selected product
        product_idx = list(customer_product_matrix.columns).index(product_name)
        similarity_scores = list(enumerate(product_similarity[product_idx]))
        
        # Sort by similarity (excluding the product itself)
        similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:n_recommendations+1]
        
        # Get recommended product names
        recommended_products = []
        for idx, score in similarity_scores:
            product_name_rec = customer_product_matrix.columns[idx]
            recommended_products.append({
                'Product': product_name_rec,
                'Similarity_Score': score,
                'Index': idx
            })
        
        return recommended_products
    
    # Prepare data
    customer_product_matrix, product_info = prepare_recommendation_data()
    
    # Product selection interface
    st.subheader("🔍 Select a Product")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Product search
        search_term = st.text_input("🔎 Search for a product:", placeholder="Type product name here...")
        
        # Filter products based on search
        if search_term:
            filtered_products = [prod for prod in customer_product_matrix.columns if search_term.lower() in prod.lower()]
        else:
            filtered_products = list(customer_product_matrix.columns)
        
        # Show top products if no search
        if not search_term:
            st.info("💡 Tip: Search for a product name or select from popular products below")
            # Show most popular products
            popular_products = product_info.nlargest(20, 'Total_Revenue')['Description'].tolist()
            filtered_products = popular_products
        
        # Product selection
        if filtered_products:
            selected_product = st.selectbox(
                "Choose a product:",
                options=filtered_products[:50],  # Limit to first 50 for performance
                help="Select a product to get recommendations"
            )
        else:
            st.warning("No products found matching your search.")
            selected_product = None
    
    with col2:
        if st.button("🎯 Get Recommendations", type="primary", disabled=not selected_product):
            if selected_product:
                with st.spinner("Finding similar products..."):
                    recommendations = get_product_recommendations(selected_product, customer_product_matrix)
    
    # Display selected product info
    if selected_product:
        st.subheader(f"📦 Selected Product: {selected_product}")
        
        # Get product stats
        product_stats = product_info[product_info['Description'] == selected_product].iloc[0]
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Average Price", f"${product_stats['Avg_Price']:.2f}")
        with col2:
            st.metric("Total Sold", f"{product_stats['Total_Quantity']:,.0f}")
        with col3:
            st.metric("Unique Customers", f"{product_stats['Unique_Customers']:,.0f}")
        with col4:
            st.metric("Total Revenue", f"${product_stats['Total_Revenue']:,.2f}")
    
    # Display recommendations
    if selected_product and 'recommendations' in locals():
        if recommendations:
            st.subheader("🌟 Recommended Similar Products")
            st.markdown("*Based on collaborative filtering - customers who bought this product also bought:*")
            
            # Create recommendation cards
            for i, rec in enumerate(recommendations, 1):
                product_name = rec['Product']
                similarity_score = rec['Similarity_Score']
                
                # Get product info for recommendation
                rec_stats = product_info[product_info['Description'] == product_name]
                
                if not rec_stats.empty:
                    rec_stats = rec_stats.iloc[0]
                    
                    with st.container():
                        st.markdown(f"""
                        <div class="recommendation-card">
                            <h4>#{i} {product_name}</h4>
                            <div style="display: flex; justify-content: space-between; flex-wrap: wrap;">
                                <span><strong>Similarity:</strong> {similarity_score:.1%}</span>
                                <span><strong>Avg Price:</strong> ${rec_stats['Avg_Price']:.2f}</span>
                                <span><strong>Sold:</strong> {rec_stats['Total_Quantity']:,.0f} units</span>
                                <span><strong>Customers:</strong> {rec_stats['Unique_Customers']:,.0f}</span>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
            
            # Recommendation insights
            st.subheader("📊 Recommendation Insights")
            
            rec_df = pd.DataFrame(recommendations)
            rec_df = rec_df.merge(product_info, left_on='Product', right_on='Description', how='left')
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Similarity scores
                fig_similarity = px.bar(
                    rec_df,
                    x='Similarity_Score',
                    y='Product',
                    orientation='h',
                    title="Similarity Scores",
                    text='Similarity_Score'
                )
                fig_similarity.update_traces(texttemplate='%{text:.1%}', textposition='outside')
                fig_similarity.update_layout(yaxis={'categoryorder':'total ascending'})
                st.plotly_chart(fig_similarity, use_container_width=True)
            
            with col2:
                # Price comparison
                all_products = [selected_product] + [rec['Product'] for rec in recommendations]
                price_comparison = product_info[product_info['Description'].isin(all_products)].copy()
                price_comparison['Type'] = price_comparison['Description'].apply(
                    lambda x: 'Selected' if x == selected_product else 'Recommended'
                )
                
                fig_price = px.bar(
                    price_comparison,
                    x='Avg_Price',
                    y='Description',
                    color='Type',
                    orientation='h',
                    title="Price Comparison",
                    text='Avg_Price'
                )
                fig_price.update_traces(texttemplate='$%{text:.2f}', textposition='outside')
                st.plotly_chart(fig_price, use_container_width=True)
            
        else:
            st.warning("No similar products found for this item.")
    
    # Popular Products Section
    st.subheader("🔥 Most Popular Products")
    st.markdown("*Browse our top-selling products*")
    
    top_products = product_info.nlargest(10, 'Total_Revenue')
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig_revenue = px.bar(
            top_products,
            x='Total_Revenue',
            y='Description',
            orientation='h',
            title="Top Products by Revenue",
            text='Total_Revenue'
        )
        fig_revenue.update_traces(texttemplate='$%{text:,.0f}', textposition='outside')
        fig_revenue.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig_revenue, use_container_width=True)
    
    with col2:
        fig_customers = px.bar(
            top_products,
            x='Unique_Customers',
            y='Description',
            orientation='h',
            title="Top Products by Customer Count",
            text='Unique_Customers',
            color='Unique_Customers',
            color_continuous_scale='viridis'
        )
        fig_customers.update_traces(texttemplate='%{text:.0f}', textposition='outside')
        fig_customers.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig_customers, use_container_width=True)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666;'>
        <p>Shopper Spectrum - Customer Segmentation Analytics Dashboard</p>
        <p>Built with Streamlit • Data Analysis • Machine Learning</p>
    </div>
    """,
    unsafe_allow_html=True
)

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime
import time
from typing import Dict, List, Any
from utils.mongo import MongoDBInterface

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Any

# Import your MongoDB interface
# from your_mongo_interface import MongoDBInterface

# For demonstration, I'll include a simplified version of your interface
from pymongo import MongoClient
from pymongo.collection import Collection
from typing import Any, Dict, List, Optional

# Configuration - Set your MongoDB connection details here
MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "prod_db"

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Any

# Import your MongoDB interface
# from your_mongo_interface import MongoDBInterface

# For demonstration, I'll include a simplified version of your interface
from pymongo import MongoClient
from pymongo.collection import Collection
from typing import Any, Dict, List, Optional


class MongoDBInterface:
    def __init__(self, uri: str, db_name: str, collection_name: str):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection: Collection = self.db[collection_name]

    def create_document(self, data: Dict[str, Any]) -> str:
        """Insert a new document into the collection."""
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def read_documents(self, query: Dict[str, Any] = {}, projection: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """Find documents matching the query."""
        return list(self.collection.find(query, projection))

    def read_document_by_id(self, document_id: Any) -> Optional[Dict[str, Any]]:
        """Find a single document by its _id."""
        return self.collection.find_one({"_id": document_id})

    def update_document(self, query: Dict[str, Any], update_data: Dict[str, Any]) -> int:
        """Update documents matching the query."""
        result = self.collection.update_many(query, {"$set": update_data})
        return result.modified_count

    def delete_document(self, query: Dict[str, Any]) -> int:
        """Delete documents matching the query."""
        result = self.collection.delete_many(query)
        return result.deleted_count

    def close_connection(self):
        """Close the MongoDB client connection."""
        self.client.close()


# Configuration - Set your MongoDB connection details here
MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "prod_db"

# Collections
INVENTORY_COLLECTION = "inventory"
ROBOT_ANALYTICS_COLLECTION = "logs"  # Change this to your actual collection name
TICKETS_COLLECTION = "tickets"  # Change this to your actual collection name
PRODUCTS_COLLECTION = "products"  # Change this to your actual collection name

# Initialize MongoDB connections
@st.cache_resource
def get_inventory_interface():
    """Get MongoDB interface for inventory."""
    return MongoDBInterface(MONGO_URI, DATABASE_NAME, INVENTORY_COLLECTION)

@st.cache_resource
def get_robot_interface():
    """Get MongoDB interface for robot analytics."""
    return MongoDBInterface(MONGO_URI, DATABASE_NAME, ROBOT_ANALYTICS_COLLECTION)

@st.cache_resource
def get_tickets_interface():
    """Get MongoDB interface for tickets."""
    return MongoDBInterface(MONGO_URI, DATABASE_NAME, TICKETS_COLLECTION)

@st.cache_resource
def get_products_interface():
    """Get MongoDB interface for products."""
    return MongoDBInterface(MONGO_URI, DATABASE_NAME, PRODUCTS_COLLECTION)


# INVENTORY PAGE FUNCTIONS
@st.cache_data(ttl=60)
def load_inventory_data():
    """Load inventory data from MongoDB."""
    try:
        mongo = get_inventory_interface()
        documents = mongo.read_documents()
        
        inventory_dict = {}
        for doc in documents:
            doc_copy = {k: v for k, v in doc.items() if k != '_id'}
            inventory_dict.update(doc_copy)
        
        return inventory_dict
    except Exception as e:
        st.error(f"Error loading inventory data: {str(e)}")
        return {}

def save_inventory_data(inventory_dict: Dict[str, int]):
    """Save inventory data to MongoDB."""
    try:
        mongo = get_inventory_interface()
        mongo.delete_document({})
        mongo.create_document(inventory_dict)
        st.cache_data.clear()
        return True, "Data saved successfully!"
    except Exception as e:
        return False, f"Error saving data: {str(e)}"

def create_inventory_charts(inventory_dict: Dict[str, int]):
    """Create various charts for inventory visualization."""
    df = pd.DataFrame(list(inventory_dict.items()), columns=['Item', 'Quantity'])
    df = df.sort_values('Quantity', ascending=False)
    
    # Top 10 Items
    top_10 = df.head(10)
    fig_top = px.bar(
        top_10.sort_values('Quantity', ascending=True),
        x='Quantity',
        y='Item',
        orientation='h',
        title='📦 Top 10 Items by Quantity',
        color='Quantity',
        color_continuous_scale='Blues',
        text='Quantity'
    )
    fig_top.update_traces(texttemplate='%{text}', textposition='outside')
    fig_top.update_layout(height=400, showlegend=False)
    
    # All Items Overview
    fig_all = px.bar(
        df,
        x='Item',
        y='Quantity',
        title='📊 Complete Inventory Overview',
        color='Quantity',
        color_continuous_scale='Viridis'
    )
    fig_all.update_xaxes(tickangle=45)
    fig_all.update_layout(height=500, showlegend=False)
    
    # Low Stock Items
    low_stock = df[df['Quantity'] < 50].sort_values('Quantity')
    if not low_stock.empty:
        fig_low_stock = px.bar(
            low_stock,
            x='Item',
            y='Quantity',
            title='⚠️ Low Stock Items (< 50 units)',
            color='Quantity',
            color_continuous_scale='Reds',
            text='Quantity'
        )
        fig_low_stock.update_traces(texttemplate='%{text}', textposition='outside')
        fig_low_stock.update_xaxes(tickangle=45)
        fig_low_stock.update_layout(height=400, showlegend=False)
    else:
        fig_low_stock = None
    
    # Quantity Distribution
    fig_dist = px.histogram(
        df,
        x='Quantity',
        nbins=10,
        title='📈 Quantity Distribution',
        color_discrete_sequence=['#636EFA']
    )
    fig_dist.update_layout(height=400, showlegend=False)
    
    return fig_top, fig_all, fig_low_stock, fig_dist

def display_inventory_stats(inventory_dict: Dict[str, int]):
    """Display key inventory statistics."""
    total_items = sum(inventory_dict.values())
    total_products = len(inventory_dict)
    avg_quantity = total_items / total_products if total_products > 0 else 0
    max_item = max(inventory_dict.items(), key=lambda x: x[1]) if inventory_dict else ("", 0)
    min_item = min(inventory_dict.items(), key=lambda x: x[1]) if inventory_dict else ("", 0)
    low_stock_count = len([k for k, v in inventory_dict.items() if v < 50])
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📦 Total Items", f"{total_items:,}")
        st.metric("🛍️ Total Products", f"{total_products:,}")
    
    with col2:
        st.metric("📊 Average Quantity", f"{avg_quantity:.1f}")
        st.metric("⚠️ Low Stock Items", f"{low_stock_count}", delta=f"{low_stock_count} items")
    
    with col3:
        st.metric("📈 Highest Stock", f"{max_item[1]:,}", help=f"Item: {max_item[0]}")
        st.metric("📉 Lowest Stock", f"{min_item[1]:,}", help=f"Item: {min_item[0]}")
    
    with col4:
        median_quantity = pd.Series(list(inventory_dict.values())).median()
        std_quantity = pd.Series(list(inventory_dict.values())).std()
        st.metric("📊 Median Quantity", f"{median_quantity:.1f}")
        st.metric("📊 Std Deviation", f"{std_quantity:.1f}")


# ROBOT ANALYTICS PAGE FUNCTIONS
@st.cache_data(ttl=60)
def load_robot_data():
    """Load robot analytics data from MongoDB."""
    try:
        mongo = get_robot_interface()
        documents = mongo.read_documents()
        
        # Convert to DataFrame and calculate duration
        df = pd.DataFrame(documents)
        if not df.empty and 'start_time' in df.columns and 'end_time' in df.columns:
            df['start_time'] = pd.to_datetime(df['start_time'])
            df['end_time'] = pd.to_datetime(df['end_time'])
            df['duration_ms'] = (df['end_time'] - df['start_time']).dt.total_seconds() * 1000
            df['duration_seconds'] = df['duration_ms'] / 1000
        
        return df
    except Exception as e:
        st.error(f"Error loading robot data: {str(e)}")
        return pd.DataFrame()

def create_robot_charts(df):
    """Create various charts for robot analytics."""
    if df.empty:
        return None, None, None, None, None
    
    # 1. Total Movement Time by Robot
    robot_time = df.groupby('robot')['duration_seconds'].sum().reset_index()
    fig_robot_time = px.bar(
        robot_time,
        x='robot',
        y='duration_seconds',
        title='🤖 Total Movement Time by Robot',
        color='duration_seconds',
        color_continuous_scale='Blues',
        text='duration_seconds'
    )
    fig_robot_time.update_traces(texttemplate='%{text:.2f}s', textposition='outside')
    fig_robot_time.update_layout(height=400, showlegend=False)
    
    # 2. Movement Count by Robot
    move_count = df.groupby('robot').size().reset_index(name='move_count')
    fig_move_count = px.bar(
        move_count,
        x='robot',
        y='move_count',
        title='📊 Number of Moves by Robot',
        color='move_count',
        color_continuous_scale='Greens',
        text='move_count'
    )
    fig_move_count.update_traces(texttemplate='%{text}', textposition='outside')
    fig_move_count.update_layout(height=400, showlegend=False)
    
    # 3. Average Move Duration by Robot
    avg_duration = df.groupby('robot')['duration_seconds'].mean().reset_index()
    fig_avg_duration = px.bar(
        avg_duration,
        x='robot',
        y='duration_seconds',
        title='⏱️ Average Move Duration by Robot',
        color='duration_seconds',
        color_continuous_scale='Oranges',
        text='duration_seconds'
    )
    fig_avg_duration.update_traces(texttemplate='%{text:.3f}s', textposition='outside')
    fig_avg_duration.update_layout(height=400, showlegend=False)
    
    # 4. Movement Timeline
    df_timeline = df.sort_values('start_time')
    fig_timeline = px.scatter(
        df_timeline,
        x='start_time',
        y='robot',
        color='duration_seconds',
        size='duration_seconds',
        title='⏰ Robot Movement Timeline',
        hover_data=['station', 'move', 'targets', 'duration_seconds']
    )
    fig_timeline.update_layout(height=400)
    
    # 5. Station Activity
    if 'station' in df.columns:
        station_activity = df.groupby('station').size().reset_index(name='activity_count')
        fig_station = px.pie(
            station_activity,
            values='activity_count',
            names='station',
            title='🏭 Activity by Station'
        )
        fig_station.update_layout(height=400)
    else:
        fig_station = None
    
    return fig_robot_time, fig_move_count, fig_avg_duration, fig_timeline, fig_station

# TICKETS PAGE FUNCTIONS
@st.cache_data(ttl=30)
def load_tickets_data():
    """Load tickets data from MongoDB."""
    try:
        mongo = get_tickets_interface()
        documents = mongo.read_documents()
        
        # Convert to DataFrame
        df = pd.DataFrame(documents)
        if not df.empty:
            # Ensure created_at is datetime if it exists
            if 'created_at' in df.columns:
                df['created_at'] = pd.to_datetime(df['created_at'])
            else:
                # Add created_at if it doesn't exist (for display purposes)
                df['created_at'] = datetime.now()
        
        return df
    except Exception as e:
        st.error(f"Error loading tickets data: {str(e)}")
        return pd.DataFrame()

def create_ticket(title: str, description: str):
    """Create a new ticket in MongoDB."""
    try:
        mongo = get_tickets_interface()
        
        ticket_data = {
            "title": title,
            "description": description,
            "status": "Open",
            "priority": "Medium",
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }
        
        ticket_id = mongo.create_document(ticket_data)
        st.cache_data.clear()  # Clear cache to refresh data
        return True, f"Ticket created successfully! ID: {ticket_id}"
    except Exception as e:
        return False, f"Error creating ticket: {str(e)}"

def update_ticket_status(ticket_id, new_status):
    """Update ticket status."""
    try:
        mongo = get_tickets_interface()
        from bson import ObjectId
        
        update_data = {
            "status": new_status,
            "updated_at": datetime.now()
        }
        
        updated_count = mongo.update_document(
            {"_id": ObjectId(ticket_id)}, 
            update_data
        )
        
        if updated_count > 0:
            st.cache_data.clear()
            return True, "Ticket status updated successfully!"
        else:
            return False, "Ticket not found or no changes made."
    except Exception as e:
        return False, f"Error updating ticket: {str(e)}"


def display_robot_stats(df):
    """Display key robot statistics."""
    if df.empty:
        st.warning("No robot data available")
        return
    
    total_moves = len(df)
    total_time = df['duration_seconds'].sum()
    avg_move_time = df['duration_seconds'].mean()
    unique_robots = df['robot'].nunique()
    unique_stations = df['station'].nunique() if 'station' in df.columns else 0
    date_range = (df['start_time'].max() - df['start_time'].min()).total_seconds() / 3600  # hours
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🤖 Total Moves", f"{total_moves:,}")
        st.metric("⏱️ Total Time", f"{total_time:.2f}s")
    
    with col2:
        st.metric("📊 Avg Move Time", f"{avg_move_time:.3f}s")
        st.metric("🤖 Active Robots", f"{unique_robots}")
    
    with col3:
        st.metric("🏭 Active Stations", f"{unique_stations}")
        st.metric("⏰ Time Range", f"{date_range:.1f}h")
    
    with col4:
        # Most active robot
        most_active_robot = df['robot'].value_counts().iloc[0] if not df.empty else "N/A"
        most_active_count = df['robot'].value_counts().iloc[0] if not df.empty else 0
        st.metric("🏆 Most Active Robot", most_active_robot, help=f"{most_active_count} moves")
        
        # Fastest robot (lowest avg time)
        fastest_robot = df.groupby('robot')['duration_seconds'].mean().idxmin() if not df.empty else "N/A"
        fastest_time = df.groupby('robot')['duration_seconds'].mean().min() if not df.empty else 0
        st.metric("🚀 Fastest Robot", fastest_robot, help=f"{fastest_time:.3f}s avg")


# PAGE FUNCTIONS
def show_inventory_page():
    """Display the inventory management page."""
    st.header("📦 Inventory Management")
    
    # Control button
    if st.button("🔄 Refresh Inventory Data", type="primary"):
        st.cache_data.clear()
        st.rerun()
    
    # Load inventory data
    inventory_data = load_inventory_data()
    
    if not inventory_data:
        st.warning("📋 No inventory data found in the database.")
        st.info("💡 **Data Format**: Your MongoDB documents should contain key-value pairs where the key is the item name and the value is the quantity.")
        st.code("""
Example document:
{
    "Laptop": 25,
    "Mouse": 150,
    "Keyboard": 80,
    "Monitor": 45
}
        """)
        return
    
    # Display statistics
    st.subheader("📈 Key Metrics")
    display_inventory_stats(inventory_data)
    
    st.markdown("---")
    
    # Create and display charts
    st.subheader("📊 Inventory Visualizations")
    
    fig_top, fig_all, fig_low_stock, fig_dist = create_inventory_charts(inventory_data)
    
    # Display charts in tabs
    tab1, tab2, tab3, tab4 = st.tabs(["🔝 Top Items", "📊 All Items", "⚠️ Low Stock", "📈 Distribution"])
    
    with tab1:
        st.plotly_chart(fig_top, use_container_width=True)
    
    with tab2:
        st.plotly_chart(fig_all, use_container_width=True)
    
    with tab3:
        if fig_low_stock:
            st.plotly_chart(fig_low_stock, use_container_width=True)
        else:
            st.success("🎉 No low stock items! All items have 50+ units.")
    
    with tab4:
        st.plotly_chart(fig_dist, use_container_width=True)
    
    st.markdown("---")
    
    # Data table and editing
    st.subheader("📋 Inventory Data")
    
    # Convert to DataFrame for display
    df = pd.DataFrame(list(inventory_data.items()), columns=['Item', 'Quantity'])
    
    # Search and filter
    col1, col2 = st.columns([2, 1])
    with col1:
        search_term = st.text_input("🔍 Search items", placeholder="Type item name...")
    with col2:
        min_quantity = st.number_input("Min Quantity Filter", min_value=0, value=0)
    
    # Apply filters
    if search_term:
        df = df[df['Item'].str.contains(search_term, case=False)]
    df = df[df['Quantity'] >= min_quantity]
    df = df.sort_values('Quantity', ascending=False)
    
    # Display editable dataframe
    st.subheader(f"📝 Editable Inventory ({len(df)} items)")
    edited_df = st.data_editor(
        df,
        use_container_width=True,
        num_rows="dynamic",
        column_config={
            "Item": st.column_config.TextColumn("Item Name", required=True),
            "Quantity": st.column_config.NumberColumn("Quantity", min_value=0, required=True)
        },
        key="inventory_editor"
    )
    
    # Save changes
    if st.button("💾 Save Changes", type="primary"):
        new_inventory = dict(zip(edited_df['Item'], edited_df['Quantity']))
        success, message = save_inventory_data(new_inventory)
        if success:
            st.success(message)
            st.rerun()
        else:
            st.error(message)
    
    # Export functionality
    st.subheader("📥 Export Data")
    col1, col2 = st.columns(2)
    
    with col1:
        csv_data = df.to_csv(index=False)
        st.download_button(
            label="📄 Download as CSV",
            data=csv_data,
            file_name=f"inventory_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )
    
    with col2:
        json_data = df.set_index('Item')['Quantity'].to_json(indent=2)
        st.download_button(
            label="📄 Download as JSON",
            data=json_data,
            file_name=f"inventory_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json"
        )


# PRODUCTS PAGE FUNCTIONS
@st.cache_data(ttl=60)
def load_products_data():
    """Load products data from MongoDB."""
    try:
        mongo = get_products_interface()
        documents = mongo.read_documents()
        
        # Convert to DataFrame
        df = pd.DataFrame(documents)
        if not df.empty:
            # Ensure required columns are present
            if 'prod_time' in df.columns:
                df['prod_time'] = pd.to_numeric(df['prod_time'], errors='coerce')
            if 'prod_id' in df.columns:
                df['prod_id'] = pd.to_numeric(df['prod_id'], errors='coerce')
        
        return df
    except Exception as e:
        st.error(f"Error loading products data: {str(e)}")
        return pd.DataFrame()

def create_products_charts(df):
    """Create various charts for products analysis."""
    if df.empty:
        return None, None, None, None, None, None
    
    # 1. Production Time Distribution
    fig_time_dist = px.histogram(
        df,
        x='prod_time',
        nbins=20,
        title='⏱️ Production Time Distribution',
        color_discrete_sequence=['#636EFA'],
        labels={'prod_time': 'Production Time', 'count': 'Number of Products'}
    )
    fig_time_dist.update_layout(height=400, showlegend=False)
    
    # 2. Production Time by Color
    if 'color' in df.columns:
        fig_time_color = px.box(
            df,
            x='color',
            y='prod_time',
            title='📊 Production Time by Color',
            color='color',
            labels={'prod_time': 'Production Time', 'color': 'Color'}
        )
        fig_time_color.update_layout(height=400)
    else:
        fig_time_color = None
    
    # 3. Color Distribution (Pie Chart)
    if 'color' in df.columns:
        color_counts = df['color'].value_counts()
        fig_color_dist = px.pie(
            values=color_counts.values,
            names=color_counts.index,
            title='🎨 Product Color Distribution'
        )
        fig_color_dist.update_layout(height=400)
    else:
        fig_color_dist = None
    
    # 4. Production Timeline (if we have prod_id as sequence)
    if 'prod_id' in df.columns:
        df_timeline = df.sort_values('prod_id')
        fig_timeline = px.line(
            df_timeline,
            x='prod_id',
            y='prod_time',
            title='📈 Production Time Trend Over Product Sequence',
            color='color' if 'color' in df.columns else None,
            labels={'prod_id': 'Product ID', 'prod_time': 'Production Time'}
        )
        fig_timeline.update_layout(height=400)
    else:
        fig_timeline = None
    
    # 5. Average Production Time by Color (Bar Chart)
    if 'color' in df.columns:
        avg_time_color = df.groupby('color')['prod_time'].agg(['mean', 'count']).reset_index()
        avg_time_color.columns = ['color', 'avg_time', 'count']
        
        fig_avg_time = px.bar(
            avg_time_color,
            x='color',
            y='avg_time',
            title='⚡ Average Production Time by Color',
            color='avg_time',
            color_continuous_scale='Viridis',
            text='avg_time',
            hover_data=['count']
        )
        fig_avg_time.update_traces(texttemplate='%{text:.1f}', textposition='outside')
        fig_avg_time.update_layout(height=400, showlegend=False)
    else:
        fig_avg_time = None
    
    # 6. Production Efficiency (Products per time unit)
    if 'color' in df.columns:
        efficiency_data = df.groupby('color').agg({
            'prod_time': ['min', 'max', 'std'],
            'prod_id': 'count'
        }).reset_index()
        efficiency_data.columns = ['color', 'min_time', 'max_time', 'std_time', 'total_products']
        
        fig_efficiency = px.scatter(
            efficiency_data,
            x='total_products',
            y='min_time',
            size='max_time',
            color='std_time',
            title='🎯 Production Efficiency by Color',
            labels={
                'total_products': 'Total Products',
                'min_time': 'Minimum Production Time',
                'max_time': 'Maximum Production Time',
                'std_time': 'Time Variability'
            },
            hover_name='color'
        )
        fig_efficiency.update_layout(height=400)
    else:
        fig_efficiency = None
    
    return fig_time_dist, fig_time_color, fig_color_dist, fig_timeline, fig_avg_time, fig_efficiency

def display_products_stats(df):
    """Display key products statistics."""
    if df.empty:
        st.warning("No products data available")
        return
    
    total_products = len(df)
    
    if 'prod_time' in df.columns:
        avg_time = df['prod_time'].mean()
        min_time = df['prod_time'].min()
        max_time = df['prod_time'].max()
        total_time = df['prod_time'].sum()
        std_time = df['prod_time'].std()
    else:
        avg_time = min_time = max_time = total_time = std_time = 0
    
    if 'color' in df.columns:
        unique_colors = df['color'].nunique()
        most_common_color = df['color'].value_counts().index[0] if not df.empty else "N/A"
        most_common_count = df['color'].value_counts().iloc[0] if not df.empty else 0
    else:
        unique_colors = 0
        most_common_color = "N/A"
        most_common_count = 0
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🏭 Total Products", f"{total_products:,}")
        st.metric("⏱️ Average Time", f"{avg_time:.1f}" if avg_time > 0 else "N/A")
    
    with col2:
        st.metric("⚡ Min Time", f"{min_time:.1f}" if min_time > 0 else "N/A")
        st.metric("🐌 Max Time", f"{max_time:.1f}" if max_time > 0 else "N/A")
    
    with col3:
        st.metric("🕐 Total Time", f"{total_time:.1f}" if total_time > 0 else "N/A")
        st.metric("📊 Time Std Dev", f"{std_time:.2f}" if std_time > 0 else "N/A")
    
    with col4:
        st.metric("🎨 Unique Colors", f"{unique_colors}")
        st.metric("🏆 Most Common", most_common_color, help=f"{most_common_count} products")


def show_products_page():
    """Display the products statistics page."""
    st.header("🏭 Product Statistics")
    
    # Control button
    if st.button("🔄 Refresh Products Data", type="primary"):
        st.cache_data.clear()
        st.rerun()
    
    # Load products data
    products_data = load_products_data()
    
    if products_data.empty:
        st.warning("📋 No products data found in the database.")
        st.info("💡 **Expected Data Format**: Documents with production information")
        st.code("""
Example document:
{
    "_id": ObjectId("..."),
    "prod_id": 1,
    "prod_time": 43,
    "color": "Red"
}
        """)
        return
    
    # Display statistics
    st.subheader("📈 Key Metrics")
    display_products_stats(products_data)
    
    st.markdown("---")
    
    # Create and display charts
    st.subheader("📊 Production Analytics")
    
    fig_time_dist, fig_time_color, fig_color_dist, fig_timeline, fig_avg_time, fig_efficiency = create_products_charts(products_data)
    
    if fig_time_dist:
        # Display charts in tabs
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
            "⏱️ Time Distribution", 
            "📊 Time by Color", 
            "🎨 Color Distribution", 
            "📈 Timeline", 
            "⚡ Avg Times", 
            "🎯 Efficiency"
        ])
        
        with tab1:
            st.plotly_chart(fig_time_dist, use_container_width=True)
            
            # Additional insights
            if 'prod_time' in products_data.columns:
                median_time = products_data['prod_time'].median()
                percentile_75 = products_data['prod_time'].quantile(0.75)
                percentile_25 = products_data['prod_time'].quantile(0.25)
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Median Time", f"{median_time:.1f}")
                with col2:
                    st.metric("75th Percentile", f"{percentile_75:.1f}")
                with col3:
                    st.metric("25th Percentile", f"{percentile_25:.1f}")
        
        with tab2:
            if fig_time_color:
                st.plotly_chart(fig_time_color, use_container_width=True)
                
                # Statistical summary by color
                if 'color' in products_data.columns and 'prod_time' in products_data.columns:
                    color_stats = products_data.groupby('color')['prod_time'].describe()
                    st.subheader("📊 Statistical Summary by Color")
                    st.dataframe(color_stats.round(2), use_container_width=True)
            else:
                st.info("Color data not available for this analysis")
        
        with tab3:
            if fig_color_dist:
                st.plotly_chart(fig_color_dist, use_container_width=True)
                
                # Color production summary
                color_summary = products_data['color'].value_counts().reset_index()
                color_summary.columns = ['Color', 'Count']
                color_summary['Percentage'] = (color_summary['Count'] / len(products_data) * 100).round(1)
                st.dataframe(color_summary, use_container_width=True, hide_index=True)
            else:
                st.info("Color data not available")
        
        with tab4:
            if fig_timeline:
                st.plotly_chart(fig_timeline, use_container_width=True)
                
                # Trend analysis
                if 'prod_id' in products_data.columns and 'prod_time' in products_data.columns:
                    correlation = products_data['prod_id'].corr(products_data['prod_time'])
                    st.metric("📈 Time-Sequence Correlation", f"{correlation:.3f}")
                    
                    if correlation > 0.1:
                        st.info("🔺 Production time tends to increase over sequence")
                    elif correlation < -0.1:
                        st.info("🔻 Production time tends to decrease over sequence (improvement)")
                    else:
                        st.info("➡️ Production time is relatively stable over sequence")
            else:
                st.info("Product ID sequence not available")
        
        with tab5:
            if fig_avg_time:
                st.plotly_chart(fig_avg_time, use_container_width=True)
                
                # Best and worst performers
                if 'color' in products_data.columns:
                    avg_by_color = products_data.groupby('color')['prod_time'].mean().sort_values()
                    col1, col2 = st.columns(2)
                    with col1:
                        st.success(f"🚀 Fastest: {avg_by_color.index[0]} ({avg_by_color.iloc[0]:.1f})")
                    with col2:
                        st.warning(f"🐌 Slowest: {avg_by_color.index[-1]} ({avg_by_color.iloc[-1]:.1f})")
            else:
                st.info("Color data not available")
        
        with tab6:
            if fig_efficiency:
                st.plotly_chart(fig_efficiency, use_container_width=True)
                st.info("💡 Bubble size represents max production time, color represents time variability")
            else:
                st.info("Efficiency analysis requires color data")
    
    st.markdown("---")
    
    # Detailed products table
    st.subheader("📋 Products Data")
    
    # Filters
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if 'color' in products_data.columns:
            color_filter = st.selectbox("Filter by Color", ["All"] + sorted(products_data['color'].unique()))
        else:
            color_filter = "All"
    
    with col2:
        if 'prod_time' in products_data.columns:
            min_time_filter = st.number_input("Min Production Time", min_value=0.0, value=0.0)
        else:
            min_time_filter = 0.0
    
    with col3:
        if 'prod_time' in products_data.columns:
            max_time_filter = st.number_input(
                "Max Production Time", 
                min_value=0.0, 
                value=float(products_data['prod_time'].max()) if 'prod_time' in products_data.columns else 100.0
            )
        else:
            max_time_filter = 100.0
    
    # Apply filters
    filtered_df = products_data.copy()
    if color_filter != "All" and 'color' in filtered_df.columns:
        filtered_df = filtered_df[filtered_df['color'] == color_filter]
    if 'prod_time' in filtered_df.columns:
        filtered_df = filtered_df[
            (filtered_df['prod_time'] >= min_time_filter) & 
            (filtered_df['prod_time'] <= max_time_filter)
        ]
    
    # Sort by product ID if available
    if 'prod_id' in filtered_df.columns:
        filtered_df = filtered_df.sort_values('prod_id', ascending=False)
    
    # Display data
    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "prod_id": st.column_config.NumberColumn("Product ID", format="%d"),
            "prod_time": st.column_config.NumberColumn("Production Time", format="%.1f"),
            "color": st.column_config.TextColumn("Color")
        }
    )
    
    st.info(f"Showing {len(filtered_df)} of {len(products_data)} products")
    
    # Export functionality
    st.subheader("📥 Export Products Data")
    col1, col2 = st.columns(2)
    
    with col1:
        csv_data = filtered_df.to_csv(index=False)
        st.download_button(
            label="📄 Download Filtered Data as CSV",
            data=csv_data,
            file_name=f"products_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )
    
    with col2:
        # Summary statistics export
        if 'color' in products_data.columns and 'prod_time' in products_data.columns:
            summary_stats = products_data.groupby('color')['prod_time'].describe()
            summary_csv = summary_stats.to_csv()
            st.download_button(
                label="📊 Download Summary Stats as CSV",
                data=summary_csv,
                file_name=f"products_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv"
            )


def show_tickets_page():
    """Display the ticketing system page with Kanban board layout."""
    st.header("🎫 Suggestion & Support Tickets")
    
    # Ticket creation section (collapsible)
    with st.expander("✨ Create New Ticket", expanded=False):
        # Ticket creation form
        with st.form("create_ticket_form", clear_on_submit=True):
            ticket_title = st.text_input(
                "Ticket Title", 
                placeholder="Brief description of your suggestion or issue"
            )
            
            ticket_description = st.text_area(
                "Ticket Description", 
                placeholder="Provide detailed information about your suggestion, issue, or request...",
                height=150
            )
            
            # Additional fields for better categorization
            col_priority, col_category = st.columns(2)
            with col_priority:
                priority = st.selectbox("Priority", ["Low", "Medium", "High", "Critical"])
            
            with col_category:
                category = st.selectbox("Category", [
                    "Suggestion", 
                    "Bug Report", 
                    "Feature Request", 
                    "Technical Issue", 
                    "General Inquiry"
                ])
            
            submit_ticket = st.form_submit_button("🚀 Submit Ticket", type="primary")
            
            if submit_ticket:
                if ticket_title and ticket_description:
                    # Enhanced ticket data with additional fields
                    enhanced_description = f"**Category:** {category}\n**Priority:** {priority}\n\n{ticket_description}"
                    
                    success, message = create_ticket(ticket_title, enhanced_description)
                    if success:
                        st.success(message)
                        st.balloons()  # Fun celebration effect
                        st.rerun()  # Refresh to show new ticket
                    else:
                        st.error(message)
                else:
                    st.error("Please fill in both title and description.")
    
    # Control buttons
    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        if st.button("🔄 Refresh Tickets"):
            st.cache_data.clear()
            st.rerun()
    
    with col2:
        show_stats = st.checkbox("📊 Show Statistics", value=True)
    
    # Load tickets data
    tickets_df = load_tickets_data()
    
    if tickets_df.empty:
        st.info("No tickets found. Create your first ticket above!")
        st.markdown("""
        ### 💡 How to use the Ticketing System:
        
        1. **Create Tickets** - Use the form above to submit suggestions, bug reports, or requests
        2. **Track Progress** - Monitor ticket status in the Kanban board below
        3. **Categorize** - Select appropriate priority and category for better organization
        4. **Manage** - Drag tickets between columns or update status directly
        
        **Ticket Status Options:**
        - 🔓 **Open** - New ticket, awaiting review
        - 🔄 **In Progress** - Ticket is being worked on
        - ✅ **Closed** - Ticket has been resolved
        """)
        return
    
    # Show statistics if enabled
    if show_stats:
        st.subheader("📊 Ticket Statistics")
        
        total_tickets = len(tickets_df)
        
        # Status distribution
        if 'status' in tickets_df.columns:
            status_counts = tickets_df['status'].value_counts()
            open_tickets = status_counts.get('Open', 0)
            closed_tickets = status_counts.get('Closed', 0)
            in_progress = status_counts.get('In Progress', 0)
        else:
            open_tickets = total_tickets
            closed_tickets = 0
            in_progress = 0
        
        # Display metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("📋 Total", total_tickets)
        with col2:
            st.metric("🔓 Open", open_tickets)
        with col3:
            st.metric("🔄 In Progress", in_progress)
        with col4:
            st.metric("✅ Closed", closed_tickets)
        
        st.markdown("---")
    
    # KANBAN BOARD LAYOUT
    st.subheader("📋 Kanban Board")
    
    # Create three columns for the Kanban board
    col_open, col_progress, col_closed = st.columns(3)
    
    # Define status categories
    statuses = {
        'Open': {'column': col_open, 'icon': '🔓', 'color': '#ff9999'},
        'In Progress': {'column': col_progress, 'icon': '🔄', 'color': '#ffcc99'},
        'Closed': {'column': col_closed, 'icon': '✅', 'color': '#99ff99'}
    }
    
    # Sort tickets by created_at (newest first)
    if 'created_at' in tickets_df.columns:
        tickets_df = tickets_df.sort_values('created_at', ascending=False)
    
    # Group tickets by status
    for status, config in statuses.items():
        with config['column']:
            # Column header with count
            status_tickets = tickets_df[tickets_df.get('status', 'Open') == status]
            st.markdown(f"""
            <div style="
                background-color: {config['color']};
                padding: 10px;
                border-radius: 10px;
                text-align: center;
                margin-bottom: 15px;
                font-weight: bold;
                color: #333;
            ">
                {config['icon']} {status} ({len(status_tickets)})
            </div>
            """, unsafe_allow_html=True)
            
            # Display tickets in this status
            for idx, ticket in status_tickets.iterrows():
                # Extract priority and category if available
                description = ticket.get('description', '')
                priority = 'Medium'  # default
                category = 'General'  # default
                
                # Parse enhanced description
                if '**Priority:**' in description:
                    try:
                        priority_line = description.split('**Priority:**')[1].split('\n')[0].strip()
                        priority = priority_line
                    except:
                        pass
                
                if '**Category:**' in description:
                    try:
                        category_line = description.split('**Category:**')[1].split('\n')[0].strip()
                        category = category_line
                    except:
                        pass
                
                # Clean description (remove metadata)
                clean_description = description
                if '**Category:**' in clean_description and '**Priority:**' in clean_description:
                    clean_description = '\n\n'.join(clean_description.split('\n\n')[1:])
                
                # Priority color coding
                priority_colors = {
                    'Low': '#90EE90',
                    'Medium': '#FFD700', 
                    'High': '#FFA500',
                    'Critical': '#FF6B6B'
                }
                priority_color = priority_colors.get(priority, '#FFD700')
                
                # Create ticket card
                with st.container():
                    st.markdown(f"""
                    <div style="
                        border: 1px solid #ddd;
                        border-radius: 8px;
                        padding: 12px;
                        margin-bottom: 10px;
                        background-color: white;
                        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                        border-left: 4px solid {priority_color};
                    ">
                        <div style="font-weight: bold; font-size: 14px; margin-bottom: 5px;">
                            {ticket.get('title', 'Untitled')}
                        </div>
                        <div style="font-size: 11px; color: #666; margin-bottom: 8px;">
                            📂 {category} | ⚡ {priority}
                        </div>
                        <div style="font-size: 12px; color: #333; margin-bottom: 8px; max-height: 60px; overflow-y: auto;">
                            {clean_description[:100]}{'...' if len(clean_description) > 100 else ''}
                        </div>
                        <div style="font-size: 10px; color: #999;">
                            {ticket.get('created_at', '').strftime('%Y-%m-%d %H:%M') if 'created_at' in ticket and pd.notna(ticket['created_at']) else 'No date'}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Status change buttons (compact layout)
                    button_col1, button_col2, button_col3 = st.columns(3)
                    
                    current_status = ticket.get('status', 'Open')
                    
                    with button_col1:
                        if current_status != 'Open':
                            if st.button("🔓", key=f"open_{ticket['_id']}", help="Move to Open"):
                                success, message = update_ticket_status(str(ticket['_id']), 'Open')
                                if success:
                                    st.rerun()
                    
                    with button_col2:
                        if current_status != 'In Progress':
                            if st.button("🔄", key=f"progress_{ticket['_id']}", help="Move to In Progress"):
                                success, message = update_ticket_status(str(ticket['_id']), 'In Progress')
                                if success:
                                    st.rerun()
                    
                    with button_col3:
                        if current_status != 'Closed':
                            if st.button("✅", key=f"close_{ticket['_id']}", help="Move to Closed"):
                                success, message = update_ticket_status(str(ticket['_id']), 'Closed')
                                if success:
                                    st.rerun()
                    
                    # Expandable details
                    with st.expander("📖 View Details", expanded=False):
                        st.write("**Full Description:**")
                        st.write(clean_description)
                        
                        if 'created_at' in ticket and pd.notna(ticket['created_at']):
                            st.write(f"**Created:** {ticket['created_at'].strftime('%Y-%m-%d %H:%M:%S')}")
                        
                        if 'updated_at' in ticket and pd.notna(ticket['updated_at']):
                            st.write(f"**Updated:** {ticket['updated_at'].strftime('%Y-%m-%d %H:%M:%S')}")
                        
                        st.write(f"**Ticket ID:** {ticket['_id']}")
            
            # Add some spacing if column is empty
            if len(status_tickets) == 0:
                st.markdown("""
                <div style="
                    background-color: #f8f9fa;
                    padding: 20px;
                    border-radius: 8px;
                    text-align: center;
                    color: #6c757d;
                    border: 2px dashed #dee2e6;
                ">
                    No tickets in this status
                </div>
                """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Export functionality
    st.subheader("📥 Export Tickets")
    
    csv_data = tickets_df.to_csv(index=False)
    st.download_button(
        label="📄 Download All Tickets as CSV",
        data=csv_data,
        file_name=f"tickets_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv"
    )


def show_robot_analytics_page():
    """Display the robot analytics page."""
    st.header("🤖 Robot Analytics")
    
    # Control button
    if st.button("🔄 Refresh Robot Data", type="primary"):
        st.cache_data.clear()
        st.rerun()
    
    # Load robot data
    robot_data = load_robot_data()
    
    if robot_data.empty:
        st.warning("📋 No robot data found in the database.")
        st.info("💡 **Expected Data Format**: Documents with robot movement information")
        st.code("""
Example document:
{
    "_id": ObjectId("..."),
    "product_increment": 1,
    "station": "S1",
    "robot": "R1", 
    "move": "J",
    "targets": "R1Base",
    "start_time": datetime,
    "end_time": datetime
}
        """)
        return
    
    # Display statistics
    st.subheader("📈 Key Metrics")
    display_robot_stats(robot_data)
    
    st.markdown("---")
    
    # Create and display charts
    st.subheader("📊 Robot Analytics")
    
    fig_robot_time, fig_move_count, fig_avg_duration, fig_timeline, fig_station = create_robot_charts(robot_data)
    
    if fig_robot_time:
        # Display charts in tabs
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["⏱️ Total Time", "📊 Move Count", "🚀 Avg Duration", "⏰ Timeline", "🏭 Stations"])
        
        with tab1:
            st.plotly_chart(fig_robot_time, use_container_width=True)
        
        with tab2:
            st.plotly_chart(fig_move_count, use_container_width=True)
        
        with tab3:
            st.plotly_chart(fig_avg_duration, use_container_width=True)
        
        with tab4:
            st.plotly_chart(fig_timeline, use_container_width=True)
        
        with tab5:
            if fig_station:
                st.plotly_chart(fig_station, use_container_width=True)
            else:
                st.info("Station data not available")
    
    st.markdown("---")
    
    # Detailed robot performance table
    st.subheader("🤖 Robot Performance Summary")
    
    if not robot_data.empty:
        # Create summary table
        robot_summary = robot_data.groupby('robot').agg({
            'duration_seconds': ['count', 'sum', 'mean', 'min', 'max'],
            'start_time': ['min', 'max']
        }).round(4)
        
        robot_summary.columns = ['Move Count', 'Total Time (s)', 'Avg Time (s)', 'Min Time (s)', 'Max Time (s)', 'First Move', 'Last Move']
        robot_summary = robot_summary.reset_index()
        
        st.dataframe(
            robot_summary,
            use_container_width=True,
            column_config={
                "Total Time (s)": st.column_config.NumberColumn("Total Time (s)", format="%.3f"),
                "Avg Time (s)": st.column_config.NumberColumn("Avg Time (s)", format="%.4f"),
                "Min Time (s)": st.column_config.NumberColumn("Min Time (s)", format="%.4f"),
                "Max Time (s)": st.column_config.NumberColumn("Max Time (s)", format="%.4f"),
            }
        )
        
        # Export robot data
        st.subheader("📥 Export Robot Data")
        col1, col2 = st.columns(2)
        
        with col1:
            csv_data = robot_data.to_csv(index=False)
            st.download_button(
                label="📄 Download Raw Data as CSV",
                data=csv_data,
                file_name=f"robot_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv"
            )
        
        with col2:
            summary_csv = robot_summary.to_csv(index=False)
            st.download_button(
                label="📄 Download Summary as CSV",
                data=summary_csv,
                file_name=f"robot_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv"
            )


def main():
    st.set_page_config(
        page_title="Management Dashboard",
        page_icon="📊",
        layout="wide"
    )
    
    # Main title
    st.title("📊 Management Dashboard")
    
    # Page selection dropdown
    page = st.selectbox(
        "Select Dashboard",
        ["📦 Inventory Management", "🤖 Robot Analytics", "🎫 Suggestion & Support Tickets", "🏭 Product Statistics"],
        index=0
    )
    
    st.markdown("---")
    
    # Display selected page
    if page == "📦 Inventory Management":
        show_inventory_page()
    elif page == "🤖 Robot Analytics":
        show_robot_analytics_page()
    elif page == "🎫 Suggestion & Support Tickets":
        show_tickets_page()
    elif page == "🏭 Product Statistics":
        show_products_page()


if __name__ == "__main__":
    main()
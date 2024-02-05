import pandas as pd
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer  # Ensure you have yellowbrick installed
import os
import folium

# Load outlets data from Excel file
excel_file_path = 'filename.xlsx'  # Change this to your Excel file path
df = pd.read_excel(excel_file_path)

# Display the total number of outlets
total_outlets = len(df)
print(f"Total number of outlets: {total_outlets}")

# Function to generate distinct colors based on the number of clusters
def generate_cluster_colors(num_clusters):
    # Use an extended set of distinct colors
    base_colors = ['blue', 'green', 'red', 'orange', 'purple', 'yellow', 'cyan', 'pink',
                   'lightblue', 'lightgreen', 'darkblue', 'darkgreen', 'beige', 'gray', 'darkred']
    
    # Repeat the base colors to cover the required number of clusters
    cluster_colors = (base_colors * (num_clusters // len(base_colors) + 1))[:num_clusters]
    
    return cluster_colors

# Function to plot Folium Map and export to HTML
def plot_folium_map_and_export(data, cluster_centers, directory_path, num_clusters, min_outlets_per_cluster, max_outlets_per_cluster):
    # Generate cluster colors based on the actual number of clusters
    cluster_colors = generate_cluster_colors(num_clusters)

    # Initialize an empty map
    folium_map = folium.Map(location=cluster_centers[0], zoom_start=13)

    # Initialize a Pandas DataFrame to store all cluster data
    all_clusters_data = pd.DataFrame()

    for i, center in enumerate(cluster_centers):
        cluster_data = data[data['Cluster'] == (i + 1)]  # Adjusted to start from 1

        # Ensure the number of outlets in the cluster is within the specified range
        cluster_data = cluster_data.iloc[:max_outlets_per_cluster]

        # Plot outlets with different colors and cluster number details
        for index, row in cluster_data.iterrows():
            icon_color = cluster_colors[i]
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                popup=f"Cluster {row['Cluster']}\n{row['KODE OUTLET']} - {row['NAMA OUTLET']}",
                icon=folium.Icon(color=icon_color, icon='map-marker')
            ).add_to(folium_map)

        # Concatenate cluster data to the DataFrame
        all_clusters_data = pd.concat([all_clusters_data, cluster_data])

    try:
        # Save the combined map
        map_filename = 'cluster.html'
        folium_map.save(os.path.join(directory_path, map_filename))
        print(f"Folium Map for Geographical Clusters saved as '{map_filename}'")

        # Export all clusters to one Excel file
        excel_filename = 'excel_file_name.xlsx'
        with pd.ExcelWriter(os.path.join(directory_path, excel_filename)) as writer:
            for i, cluster_data in enumerate(all_clusters_data.groupby('Cluster')):
                cluster_num, cluster_data = cluster_data
                cluster_data[['KODE OUTLET', 'NAMA OUTLET', 'Latitude', 'Longitude']].to_excel(writer, sheet_name=f'Cluster_{cluster_num}', index=False)

        print(f"All clusters exported to '{excel_filename}'")

    except Exception as e:
        print(f"Error saving Folium Map or exporting outlets for all geographical clusters: {e}")

# Use the elbow method to find the optimal number of clusters
visualizer = KElbowVisualizer(KMeans(), k=(2, 20), metric='distortion', timings=False)
visualizer.fit(df[['Latitude', 'Longitude']])
optimal_clusters = visualizer.elbow_value_

# Suggest an optimal number of outlets per cluster based on the total outlets and optimal clusters
optimal_outlets_per_cluster = total_outlets // optimal_clusters

# Display recommendations
print(f"\nRecommended Optimal Number of Clusters: {optimal_clusters}")
print(f"Recommended Optimal Outlets per Cluster: {optimal_outlets_per_cluster}")

# Ask the user for the desired minimum and maximum outlets per cluster
min_outlets_per_cluster = int(input("\nEnter the minimum number of outlets per cluster: "))
max_outlets_per_cluster = int(input("Enter the maximum number of outlets per cluster: "))

# Ask the user for the desired number of clusters
num_clusters = int(input("Enter the number of clusters: "))

# Perform K-means clustering with the chosen number of clusters
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
df['Cluster'] = kmeans.fit_predict(df[['Latitude', 'Longitude']]) + 1  # Start clusters from 1

# Get cluster center coordinates
cluster_centers = kmeans.cluster_centers_

# Specify the output directory path
output_directory_path = r'filepath'

# Plot Folium Map for all geographical clusters and export to HTML and Excel
plot_folium_map_and_export(df, cluster_centers, output_directory_path, num_clusters, min_outlets_per_cluster, max_outlets_per_cluster)

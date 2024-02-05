Geographical Clustering Readme
This repository contains Python code for performing geographical clustering on outlet data using K-means clustering. The script uses the Yellowbrick library to visualize the elbow method and determine the optimal number of clusters. The resulting clusters are then plotted on a Folium map and exported to both HTML and Excel files.

Prerequisites
Python 3.x
pandas
scikit-learn
yellowbrick
folium
Install the required libraries using the following command:

bash
Copy code
pip install pandas scikit-learn yellowbrick folium
Usage
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/your-repository.git
cd your-repository
Install Dependencies:
Make sure to install the necessary Python libraries using the provided requirements.txt file.

bash
Copy code
pip install -r requirements.txt
Prepare Data:
Replace the ALL_NEW_DEPO_BANJARBARU.xlsx file in the repository with your own Excel file containing outlet data. Ensure that the Excel file has columns named 'Latitude' and 'Longitude' for geographical coordinates.

Run the Script:
Execute the geographical_clustering.py script to perform clustering based on user input.

bash
Copy code
python geographical_clustering.py
User Input:

Enter the desired minimum and maximum number of outlets per cluster.
Input the desired number of clusters.
The script will then perform K-means clustering and generate a Folium map with clustered outlets.
Output:

The Folium map will be saved as ALL_NEW_CLUSTER_BANJARBARU.html in the specified output directory.
All clusters will be exported to an Excel file named ALL_NEW_CLUSTER_BANJARBARU.xlsx in the same output directory.
Directory Structure
geographical_clustering.py: Main Python script for clustering and visualization.
ALL_NEW_DEPO_BANJARBARU.xlsx: Sample Excel file containing outlet data (replace with your own data).
requirements.txt: List of required Python libraries.
C:\Users\fatah\OneDrive\文件\PMA\KOORDINAT\CLUSTER BANJARBARU: Default output directory for maps and Excel files.
Feel free to customize the script and adapt it to your specific use case.

Note: Ensure that you have the required permissions to access and modify the specified output directory.

For any issues or questions, please open an issue.

Happy clustering!

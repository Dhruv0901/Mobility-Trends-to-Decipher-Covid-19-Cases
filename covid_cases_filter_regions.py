import pandas as pd

# Read the CSV file
main = pd.read_csv('AU_Mobility_Report.csv')

# List of councils to filter out across all states
councils_to_filter = [
    "City of Sydney",
    "City of Wollongong",
    "City of Newcastle",
    "City of Albury",
    "Tamworth Regional Council",
    "Ballina Shire",
    "Port Macquarie-Hastings Council",
    "Dubbo City Council",
    "Wagga Wagga City Council",
    "City of Darwin",
    "Alice Springs Town Council",
    "Cairns Regional",
    "Toowoomba Regional",
    "Mackay Regional",
    "Rockhampton Regional",
    "Sunshine Coast Regional",
    "Brisbane City",
    "Bundaberg Regional",
    "Gladstone Regional",
    "City of Gold Coast",
    "Whitsunday Regional",
    "Townsville City",
    "Mount Isa City",
    "Adelaide City Council",
    "City of West Torrens",
    "City of Mount Gambier",
    "City of Port Lincoln",
    "City of Whyalla",
    "Port Augusta City Council",
    "City of Hobart",
    "City of Launceston",
    "City of Devonport",
    "City of Burnie",
    "Waratah-Wynyard Council",
    "City of Melbourne",
    "City of Greater Dandenong",
    "City of Hume",
    "Greater Geelong City",
    "Mildura Rural City",
    "Latrobe City",
    "City of Ballarat",
    "City of Warrnambool",
    "Wangaratta Rural City",
    "City of Perth",
    "City of Greater Geraldton",
    "City of Albany",
    "City of Kalgoorlie-Boulder",
    "Shire of East Pilbara",
    "Shire of Ashburton",
    "Town of Port Hedland",
    "City of Busselton",
    "City of Karratha",
    "Shire of Broome",
    "Shire of Esperance"
]

# Create a new DataFrame for filtered data
filtered_data = []

# Iterate over the rows in the DataFrame
for index, row in main.iterrows():
    state = row['sub_region_1']  # Get the state
    council = row['sub_region_2']  # Get the council

    # Check if the council is not in the filter list
    if council not in councils_to_filter:
        filtered_data.append(row)

# Create a new DataFrame from the filtered data
filtered_df = pd.DataFrame(filtered_data)

# Write the updated DataFrame to a new CSV file
filtered_df.to_csv('Filtered_AU_Mobility_Report_No_Flight.csv', index=False)



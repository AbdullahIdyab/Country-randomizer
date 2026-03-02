import requests

def get_countries():
    url = "https://restcountries.com/v3.1/all?fields=name,unMember" 
    #print("Pinging the API...")
    response = requests.get(url)
    force_add = ["Palestine", "Vatican City", "Taiwan"]
    force_remove = ["Israel"]
    
    if response.status_code == 200:
        raw_data = response.json()
        clean_list = []

        for country in raw_data:
            if country.get("unMember") == True:
                name = country.get("name", {}).get("common", "Unknown")
                clean_list.append(name)

        clean_list.extend(force_add)
        final_list = [c for c in clean_list if c not in force_remove]
        return final_list
    
    else:
        print(f"API failed. Status code: {response.status_code}")
        return ["United Kingdom", "France", "Japan", "Brazil", "Australia"]

test_list = get_countries()
#print(len(test_list))
#print(f"Successfully loaded {len(my_countries)} countries!")
#print("Here is a sample to prove it works:", my_countries[:5])
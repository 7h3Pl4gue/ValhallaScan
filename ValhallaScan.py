import shodan

def display_valhalla_art():
    valhalla_art = """
          _______  _                 _______  _        _        _______  _______  _______  _______  _       
|\     /|(  ___  )( \      |\     /|(  ___  )( \      ( \      (  ___  )(  ____ \(  ____ \(  ___  )( (    /|
| )   ( || (   ) || (      | )   ( || (   ) || (      | (      | (   ) || (    \/| (    \/| (   ) ||  \  ( |
| |   | || (___) || |      | (___) || (___) || |      | |      | (___) || (_____ | |      | (___) ||   \ | |
( (   ) )|  ___  || |      |  ___  ||  ___  || |      | |      |  ___  |(_____  )| |      |  ___  || (\ \) |
 \ \_/ / | (   ) || |      | (   ) || (   ) || |      | |      | (   ) |      ) || |      | (   ) || | \   |
  \   /  | )   ( || (____/\| )   ( || )   ( || (____/\| (____/\| )   ( |/\____) || (____/\| )   ( || )  \  |
   \_/   |/     \|(_______/|/     \||/     \|(_______/(_______/|/     \|\_______)(_______/|/     \||/    )_)
                                                                                                            
    """
    print(valhalla_art)
    print("Made By R4GN40RK - FUCK YOU V01D AND ZENN <3")
def search_valhalla(api_key, country_code, port=None, product=None, os=None, num_pages=1):
    # Initialize the Shodan API client
    api = shodan.Shodan(api_key)

    try:
        query = f"country:{country_code}"

        if port:
            query += f" port:{port}"

        if product:
            query += f" product:{product}"

        if os:
            query += f" os:{os}"

        # Perform the Shodan search
        results = api.search(query, page=num_pages)

        # Display the results
        print(f"Total results found: {results['total']}\n")
        output_text = ""

        for match in results['matches']:
            ip = match['ip_str']
            port = match['port']
            organization = match.get('org', 'N/A')
            product = match.get('product', 'N/A')
            os = match.get('os', 'N/A')
            data = match['data']

            print(f"IP: {ip}")
            print(f"Port: {port}")
            print(f"Organization: {organization}")
            print(f"Product: {product}")
            print(f"OS: {os}")
            print(f"Data: {data}\n")

            output_text += f"IP: {ip}\nPort: {port}\nOrganization: {organization}\nProduct: {product}\nOS: {os}\nData: {data}\n\n"

        return output_text

    except shodan.APIError as e:
        print(f"Error: {e}")
        return None

def save_to_txt(output_text):
    try:
        filename = input("Do you want to save the output to a .txt file? (yes/no): ")
        if filename.lower() == "yes":
            filename = input("Enter the filename (without .txt extension): ")
            with open(f"{filename}.txt", "w") as file:
                file.write(output_text)
            print("Output saved successfully.")
        else:
            print("Output not saved.")

    except IOError as e:
        print(f"Error while saving to file: {e}")

if __name__ == "__main__":
    display_valhalla_art()

    # Replace 'V01Ds Feet Pics' with your Shodan API key Or ZENN IS A BITCH
    api_key = "V01Ds Feet Pics"

    country_code = input("Enter the country code (e.g., US, DE, GB, etc.): ")
    search_port = input("Do you want to search by port? (yes/no): ").lower()

    if search_port == "yes":
        port = input("Enter the port number you want to filter by (e.g., 80, 443, 22, etc.): ")
        num_pages = int(input("Enter the number of pages to output (1 - 20): "))
    else:
        port = None

    search_by_product = input("Do you want to search by product? (yes/no): ").lower()
    search_by_os = input("Do you want to search by OS? (yes/no): ").lower()

    if search_by_product == "yes":
        product = input("Enter the product you want to search for: ")
        num_pages = int(input("Enter the number of pages to output (1 - 20): "))
    else:
        product = None

    if search_by_os == "yes":
        os = input("Enter the OS you want to search for: ")
        num_pages = int(input("Enter the number of pages to output (1 - 20): "))
    else:
        os = None

    output_text = search_valhalla(api_key, country_code, port, product, os, num_pages)

    if output_text:
        save_to_txt(output_text)

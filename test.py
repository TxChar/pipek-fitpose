from urllib.parse import urlparse, parse_qs


def convert_google_maps_to_iframe(url):
    # Parse the URL and extract the path and query parameters
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    # Extract coordinates from the URL path
    path_parts = parsed_url.path.split("/")
    coordinates = path_parts[3].split("@")[1].split(",")

    # Extract place ID from the path
    place_id = path_parts[-1].split("!")[1].split(":")[1]

    # Construct the embed URL
    embed_url = f"https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d0!2d{coordinates[1]}!3d{coordinates[0]}!4m5!3m4!1s{place_id}!8m2!3d{coordinates[0]}!4d{coordinates[1]}"

    # Return the IFrame HTML code
    iframe_html = f'<iframe src="{embed_url}" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'
    return iframe_html


# Example URL
url = "https://www.google.co.th/maps/place/%E0%B8%A1%E0%B8%AB%E0%B8%B2%E0%B8%A7%E0%B8%B4%E0%B8%97%E0%B8%A2%E0%B8%B2%E0%B8%A5%E0%B8%B1%E0%B8%A2%E0%B8%98%E0%B8%A3%E0%B8%A3%E0%B8%A1%E0%B8%A8%E0%B8%B2%E0%B8%AA%E0%B8%95%E0%B8%A3%E0%B9%8C+%E0%B8%A8%E0%B8%B9%E0%B8%99%E0%B8%A2%E0%B9%8C%E0%B8%A5%E0%B8%B3%E0%B8%9B%E0%B8%B2%E0%B8%87/@18.3170581,99.3986862,17z/data=!4m6!3m5!1s0x30d96f264a1dd1f9:0xf0346c6d9b33150!8m2!3d18.3174089!4d99.3992878!16s%2Fg%2F1227d6vq?hl=th&entry=ttu&g_ep=EgoyMDI0MDkxOC4xIKXMDSoASAFQAw%3D%3D"

iframe_code = convert_google_maps_to_iframe(url)
print(iframe_code)

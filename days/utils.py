

def get_resort_choices(destination):
    switcher = {
        "Idaho":(
            "Sun Valley",
            "Bogus Basin"
        ),
        "California":(
            "Mammoth",
            "Squaw Valley/Alpine Meadows",
            "Heavenly",
            "Northstar",
            "Kirkwood"
        ),
        "British Columbia":(
            "Kicking Horse",
            "Revelstoke",
            "Lake Louise",
            "Sunshine Village",
            "Red Mountain",
            "Fernie",
            "Kimberly",
            "Whistler",
            "Big White",
            "Sun Peaks",
            "Whitewater"
        ),
        "Montana":(
            "Bridger Bowl",
            "Big Sky",
            "Whitefish",
        ),
        "Southern Rockies":(
            "Teluride",
            "Silverton",
            "Taos",
            "Wolf Creek"
        ),
        "Wyoming":(
            "Jackson Hole",
            "Targhee"
        ),
        "Rockies":(
            "A-Basin",
            "Keystone",
            "Vail",
            "Copper",
            "Aspen",
            "Crested Butte",
            "Breckenridge",
            "Steamboat",
            "Beaver Creek",
            "Eldora",
            "Winter Park"
        ),
        "Salt Lake City":(
            "Alta",
            "Snowbird",
            "Brighton",
            "Solitude",
            "Park City",
            "Deer Valley",
            "Snowbasin"
        )
    }

    return switcher.get(destination, "Oops...something went wrong")
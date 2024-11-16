ids = {
    'user1': [213, 213, 213, 15, 213],
    'user2': [54, 54, 119, 119, 119],
    'user3': [213, 98, 98, 35]
}

unique_geo_tags = set()
for geo_tags in ids.values():
    unique_geo_tags.update(geo_tags)

print(unique_geo_tags)

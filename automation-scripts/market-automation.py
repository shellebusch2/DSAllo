# Python script for Make automation of Notion database

# ALLO Markets and their UUID (found in Notion)
markets = {
    "Imperial": "bba783bb3859472eaf0a110ed64aa71f",
    "Scottsbluff": "eb952732a77d4796b2ca817995274623",
    "Ashland": "984a18d72667413d93d24ea6f082ae20",
    "Bridgeport": "51ad868a28394bc7b1cd11e6b48d4e65",
    "Gering": "00a4f99b7fe84f889be40d79a91eda8a",
    "Alliance": "bba783bb3859472eaf0a110ed64aa71f",
    "Ogallala": "0802403aae3647f6b4e4c5a992e514bd",
    "North Platte": "90bf3be5ce5542c4b4e5b6bb83c06253",
    "Valentine": "00438c2921694eb48c4ca1ac2e331417",
    "Kearney": "57705389c30045639f1c189a588a3870",
    "Grand Island": "5ecab9a30cfc43418672de2c39b8c30d",
    "Hastings": "5375fc5f101345c1aad5c953ef80d9a9",
    "York": "055e89e0705845eb8643bfb2fc086570",
    "Columbus": "72a43cbd4068487d84304ba050006c07",
    "Norfolk":"0e804bae3dce4bbf9c7c9e9fd8767561",
    "Wayne": "df447672f35341a695d8c8d92f1b3a82",
    "Fremont": "5de138f31514498e8bfa28d82c90586c",
    "Seward": "ec644d520260416eaea0433232f4cf2f",
    "Milford": "8cf65ea916f84c9e904d24619727dc1d",
    "Lincoln": "ee931cedf6134d869e674bae26afcb1b",
    "Waverly": "d524f8144ab94ce5aaafad0875455107",
    "Gretna": "7dc9d162e9ac452eac2469904d64943d",
    "La Vista": "d39a29402de64d8a85116a7426912067",
    "Papillion": "8ac07ec1dd0e4695b9aabcc4f7d80c0f",
    "Bellevue": "a793d4b6e48f43f091ca8cab8894c9b3",
    "Fort Morgan": "28cf5dd2dba34fc38ff7126ceb51c7d9",
    "Breckenridge": "33e02a060c3c43b080e50487e214e736",
    "Greeley": "68f1db8133de4484b2c81d3a61fa611a",
    "Hudson": "d0979fa0c44f454884b3b8e2a122a13b",
    "Erie": "8c18ef6eb0ef4945a584f165f1320a03",
    "Eaton": "0a162290d6934db19e8cd2cde9c6149e",
    "Brighton": "bd24605c464e49d4a6c9f911dbf0f2eb",
    "Lake Havasu": "e262c517c89e42989ded02b197e4cc28",
    "Kingman": "0528d530bde4482298e07df28f188343",
    "Yuma": "4730c0afb7384283a9658831b2fed6d7",
    "San Luis": "c365a708efd24f92b9239b39f1e40d60"
}

# Template to follow for Make automation of city to market: 
# "{{if(4.properties_value.City.name = \"" + city + "\"; \"" + uuid + "\"; )}}"

for city, uuid in markets.items():
    print(
            "{{if(1.properties_value.City.name = \"" + city + "\"; \"" + uuid + "\"; )}}"
        )
    
    
    
    
    
  
    
   


import pandas as pd
import matplotlib.pyplot as plt
sales_df = pd.read_csv(r"C:\Users\Nidhi\Downloads\smartphone_sales.csv")
print("=" * 70)
print("SMARTPHONE MARKET ANALYSIS PROJECT")
print("=" * 70)
print("\nThis project analyzes smartphone sales data to uncover market trends,")
print("consumer preferences, and brand performance across various parameters.")
print("\nKey analysis areas include:")
print("• Sales performance and revenue analysis")
print("• Feature comparisons (Camera, Battery, Storage, RAM)")
print("• Price analysis and market positioning")
print("• Brand-wise performance evaluation")
print("• Customer rating and warranty analysis")
print("\n" + "=" * 50)
print("📁 DATASET OVERVIEW")
print("=" * 50)
print(f"Total number of smartphones analyzed: {len(sales_df)}")
print(f"Brands included: {', '.join(sales_df['Brand'].unique())}")
print(f"Data columns: {', '.join(sales_df.columns)}")
print(f"Time period: {sales_df['Launch_Year'].min()} - {sales_df['Launch_Year'].max()}")
print('Analysis Options:')
print('1 - Combined analysis of all brands')
print('2 - Analysis of phones from a specific brand')
print('3 - Modify the Dataset')
print('4 - Exit')
choice=int(input('Enter your choice : '))
if choice==1:
 while True:
    print('Parameters for Analysis:')
    print('1 - Total sales, Revenue per brand')
    print('2 - Top 10 best selling model from all brands')
    print('3 - Best selling model of each brand')
    print('4 - Market Share by Revenue')
    print('5 - Average Customer Rating by Brand')
    print('6 - Analysis of Price vs Units Sold')
    print('7 - Best camera model from each brand')
    print('8 - Top 10 best camera models from all brands')
    print('9 - Best battery capacity from each brand')
    print('10 - Top 10 phones with highest battery capacity from all brands')
    print('11 - Phones according to price,10 cheapest, most expensive phone from all brands')
    print('12 - Storage Comparison by phones')
    print('13 - Warranty comparison between phones')
    print('14 - Exit')
    choice_1=int(input('Enter your choice : '))
    if choice_1==1:
        brand_sales = sales_df.groupby("Brand")["Units_Sold"].sum().sort_values(ascending=False)
        print("Total Units Sold by Brand in ascending order:\n", brand_sales)
        brand_revenue = sales_df.groupby("Brand")["Revenue"].sum().sort_values(ascending=False)
        print("Total Revenue by Brand in ascending order")
        print(brand_revenue)
        pass
    if choice_1==2:
        top_10_models = sales_df.nlargest(10, 'Units_Sold')
        plt.figure(figsize=(12, 6))
        colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']
        plt.barh(top_10_models['Model'], top_10_models['Units_Sold'], color=colors)
        plt.title('Top 10 Best Selling Smartphone Models from all brands')
        plt.xlabel('Units Sold')
        plt.ylabel('Phone Model')
        plt.tight_layout()
        plt.show()
        print('top 10 best selling phones from all brands')
        print(top_10_models)
        pass
    if choice_1==3:
        idx_bestsellers = sales_df.groupby('Brand')['Units_Sold'].idxmax()
        best_selling_models = sales_df.loc[idx_bestsellers]
        result_df = best_selling_models[['Brand', 'Model', 'Units_Sold']]
        print('Best selling model of each brand')
        print(result_df)
        brand_sales = sales_df.groupby("Brand")["Units_Sold"].sum()
        plt.figure(figsize=(10, 6))
        brand_sales.plot(kind="bar", color="skyblue")
        plt.title("Units Sold by Brand")
        plt.xlabel("Brand")
        plt.ylabel("Units Sold")
        plt.tight_layout()
        plt.show()
        pass
    if choice_1==4:
        brand_revenue = sales_df.groupby("Brand")["Revenue"].sum()
        plt.figure(figsize=(10, 6))
        plt.plot(brand_revenue.index, brand_revenue.values, marker="o", linestyle="-", color="blue")
        plt.title("Market Share by Revenue (Line Chart)")
        plt.xlabel("Brand")
        plt.ylabel("Total Revenue (INR)")
        plt.show()
        pass
    if choice_1==5:
        avg_rating = sales_df.groupby("Brand")["Customer_Rating"].mean()
        plt.figure(figsize=(10, 6))
        plt.plot(avg_rating.index, avg_rating.values, marker="o", color="red")
        plt.title("Average Customer Rating by Brand")
        plt.xlabel("Brand")
        plt.ylabel("Rating (out of 5)")
        plt.show()
        pass
    if choice_1==6:
        plt.figure(figsize=(12, 6))
        x = range(len(sales_df))
        plt.bar([i - 0.2 for i in x], sales_df["Price"], width=0.4, label="Price (INR)", color="orange")
        plt.bar([i + 0.2 for i in x], sales_df["Units_Sold"], width=0.4, label="Units Sold", color="blue")
        plt.title("Price vs Units Sold (Model-wise)")
        plt.xlabel("Smartphone Models") 
        plt.ylabel("Values")
        plt.xticks(x, sales_df["Model"], rotation=90)
        plt.legend()
        plt.grid(axis="y", linestyle="--", alpha=0.7)
        plt.show()
        pass
    if choice_1==7:
       idx_best_camera = sales_df.groupby('Brand')['Camera_MP'].idxmax()
       best_camera_models = sales_df.loc[idx_best_camera]
       result_df = best_camera_models[['Brand', 'Model', 'Camera_MP', 'Price', 'Customer_Rating']]
       result_df = result_df.sort_values('Camera_MP', ascending=False)
       print('Best camera model of each brand')
       print(result_df)
       pass
    if choice_1==8:
       best_camera_phones = sales_df.nlargest(10, 'Camera_MP')
       result_df = best_camera_phones[['Brand', 'Model', 'Camera_MP', 'Price', 'Customer_Rating']]
       print('10 Best phones with respect to camera quality')
       print(result_df)
       pass
    if choice_1==9:
        idx_best_battery = sales_df.groupby('Brand')['Battery_mAh'].idxmax()
        best_battery_phones = sales_df.loc[idx_best_battery]
        result_df = best_battery_phones[['Brand', 'Model', 'Battery_mAh', 'Price', 'Customer_Rating']]
        result_df = result_df.sort_values('Battery_mAh', ascending=False)
        print('Best battery capacity from each brand')
        print(result_df)
        pass
    if choice_1==10:
        top_battery= sales_df.nlargest(10, 'Battery_mAh')
        result_df = top_battery[['Brand', 'Model', 'Battery_mAh','Price','Customer_Rating']]
        print('Top 10 phones with highest battery capacity from all brands')
        print(result_df)
        pass
    if choice_1==11:
        plt.figure(figsize=(12, 10))
        plt.barh(sales_df['Model'], sales_df['Price'], color='lightgreen')
        plt.title('Price of Each Phone Model', fontsize=14)
        plt.xlabel('Price (₹)')
        plt.ylabel('Phone Model')
        plt.tight_layout()
        plt.show()
        cheapest = sales_df.nsmallest(10, 'Price')
        most_expensive = sales_df.nlargest(10, 'Price')
        print(" 10 MOST EXPENSIVE PHONES:")
        print(most_expensive.to_string(index=False))
        print(" 10 CHEAPEST PHONES:")
        print(cheapest.to_string(index=False))
        pass
    if choice_1==12:
        plt.figure(figsize=(12, 10))
        plt.barh(sales_df['Model'], sales_df['Storage_GB'], color='green')
        plt.title('Storage Capacity by Models', fontsize=14)
        plt.xlabel('Storage (GB)')
        plt.ylabel('Model')
        plt.tight_layout()
        plt.show()
        pass
    if choice_1==13:
        plt.figure(figsize=(12, 10))
        plt.barh(sales_df['Model'], sales_df['Warranty_Years'], color='orange')
        plt.title('Warranty of different phones', fontsize=14)
        plt.xlabel('Warranty (years)')
        plt.ylabel('Model')
        plt.tight_layout()
        plt.show()
        pass
    if choice_1==14:
        print('Do you really want to exit?')
        print('1 - Yes')
        print('2 - No')
        choice_1_1=int(input('Enter your choice:'))
        if choice_1_1==1:
            print('See you soon.Thank you!!!')
            break
        if choice_1_1==2:
            pass
             
if choice==2:
   while True:
    print('Selection of Brand for Analysis:')
    print('1 - Analysis of Samsung brand ')
    print('2 - Analysis of Apple brand ')
    print('3 - Analysis of Xiaomi brand ')
    print('4 - Analysis of OnePlus brand ')
    print('5 - Analysis of Oppo brand ')
    print('6 - Analysis of Vivo brand ')
    print('7 - Analysis of Realme brand ')
    print('8 - Analysis of Motorola brand ')
    print('9 - Analysis of Google brand ')
    print('10 - Analysis of Nokia brand ')
    print('11 - Exit')
    choice_2=int(input('Enter your choice: '))
    if choice_2==1:
        print('Parameters for Analysis:')
        print('1 - Price Comparison(Least and Most Expensive model)')
        print('2 - Best selling Samsung phone')
        print('3 - Storage comparison')
        print('4 - Camera comparison')
        print('5 - Battery comparison')
        print('6 - Warranty comparison')
        print('7 - Rating comparison')
        print('8 - Exit')
        choice_3=int(input('Enter your choice : '))
        pass
        if choice_3==1:
            samsung_df = sales_df[sales_df['Brand'] == 'Samsung'].sort_values('Price')
            plt.figure(figsize=(10, 6))
            plt.bar(samsung_df['Model'], samsung_df['Price'], color='blue')
            plt.title('Samsung Phones - Price Comparison', fontsize=14)
            plt.xlabel('Samsung Models')
            plt.ylabel('Price (₹)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            print("Samsung Phones - Price Comparison:")
            print(samsung_df[['Model', 'Price']].to_string(index=False))
            cheapest_samsung = samsung_df.iloc[0]  
            most_expensive_samsung = samsung_df.iloc[-1] 
            print(" CHEAPEST SAMSUNG PHONE:")
            print(f"Model: {cheapest_samsung['Model']}")
            print(f"Price: ₹{cheapest_samsung['Price']:,}")
            print(" MOST EXPENSIVE SAMSUNG PHONE:")
            print(f"Model: {most_expensive_samsung['Model']}")
            print(f"Price: ₹{most_expensive_samsung['Price']:,}")
            pass
        if choice_3==2:
            samsung_df = sales_df[sales_df['Brand'] == 'Samsung'].sort_values('Units_Sold')
            plt.figure(figsize=(10, 6))
            plt.bar(samsung_df['Model'], samsung_df['Units_Sold'], color='pink')
            plt.title('Samsung Phones - Units Sold', fontsize=14)
            plt.xlabel('Samsung Models')
            plt.ylabel('Units Sold')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_selling_samsung = samsung_df.nlargest(1, 'Units_Sold').iloc[0]
            print("BEST SELLING SAMSUNG PHONE:")
            print(f"Model: {best_selling_samsung['Model']}")
            print(f"Units Sold: {best_selling_samsung['Units_Sold']:,}")
            print(f"Price: ₹{best_selling_samsung['Price']:,}")
            pass
        if choice_3==3:
            samsung_df = sales_df[sales_df['Brand'] == 'Samsung'].sort_values('Storage_GB')
            plt.figure(figsize=(10, 6))
            plt.bar(samsung_df['Model'], samsung_df['Storage_GB'], color='green')
            plt.title('Samsung Phones - Storage Comparison', fontsize=14)
            plt.xlabel('Samsung Models')
            plt.ylabel('Storage (GB)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            highest_storage_samsung = samsung_df.nlargest(1, 'Storage_GB').iloc[0]
            print("Samsung Phones - Storage Comparison:")
            print(samsung_df[['Model', 'Storage_GB']].to_string(index=False))
            print(" SAMSUNG PHONE WITH HIGHEST STORAGE:")
            print(f"Model: {highest_storage_samsung['Model']}")
            print(f"Storage: {highest_storage_samsung['Storage_GB']} GB")
            print(f"Price: ₹{highest_storage_samsung['Price']:,}")
            pass
        if choice_3==4:
            samsung_df = sales_df[sales_df['Brand'] == 'Samsung'].sort_values('Camera_MP')
            plt.figure(figsize=(10, 6))
            plt.bar(samsung_df['Model'], samsung_df['Camera_MP'], color='purple')
            plt.title('Samsung Phones - Camera Comparison', fontsize=14)
            plt.xlabel('Samsung Models')
            plt.ylabel('Camera Megapixels (MP)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_camera_samsung = samsung_df.nlargest(1, 'Camera_MP').iloc[0]
            print("Samsung Phones - Camera Comparison:")
            print(samsung_df[['Model', 'Camera_MP']].to_string(index=False))
            print("SAMSUNG PHONE WITH BEST CAMERA:")
            print(f"Model: {best_camera_samsung['Model']}")
            print(f"Camera: {best_camera_samsung['Camera_MP']} MP")
            print(f"Price: ₹{best_camera_samsung['Price']:,}")
            pass
        if choice_3==5:
            samsung_df = sales_df[sales_df['Brand'] == 'Samsung'].sort_values('Battery_mAh')
            plt.figure(figsize=(10, 6))
            plt.bar(samsung_df['Model'], samsung_df['Battery_mAh'], color='orange')
            plt.title('Samsung Phones - Battery Comparison', fontsize=14)
            plt.xlabel('Samsung Models')
            plt.ylabel('Battery Capacity (mAh)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_battery_samsung = samsung_df.nlargest(1, 'Battery_mAh').iloc[0]
            print("Samsung Phones - Battery Comparison:")
            print(samsung_df[['Model', 'Battery_mAh']].to_string(index=False))
            print("SAMSUNG PHONE WITH BEST BATTERY:")
            print(f"Model: {best_battery_samsung['Model']}")
            print(f"Battery: {best_battery_samsung['Battery_mAh']} mAh")
            print(f"Price: ₹{best_battery_samsung['Price']:,}")
            pass
        if choice_3==6:
            samsung_df = sales_df[sales_df['Brand'] == 'Samsung'].sort_values('Warranty_Years')
            plt.figure(figsize=(10, 6))
            plt.bar(samsung_df['Model'], samsung_df['Warranty_Years'], color='brown')
            plt.title('Samsung Phones - Warranty Comparison', fontsize=14)
            plt.xlabel('Samsung Models')
            plt.ylabel('Warranty (Years)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_warranty_samsung = samsung_df.nlargest(1, 'Warranty_Years').iloc[0]
            print("Samsung Phones - Warranty Comparison:")
            print(samsung_df[['Model', 'Warranty_Years']].to_string(index=False))
            print("SAMSUNG PHONE WITH BEST WARRANTY:")
            print(f"Model: {best_warranty_samsung['Model']}")
            print(f"Warranty: {best_warranty_samsung['Warranty_Years']} years")
            print(f"Price: ₹{best_warranty_samsung['Price']:,}")
            pass
        if choice_3==7:
            samsung_df = sales_df[sales_df['Brand'] == 'Samsung'].sort_values('Customer_Rating')
            plt.barh(samsung_df['Model'], samsung_df['Customer_Rating'])
            plt.title('Samsung Customer Ratings')
            plt.show()
            highest = samsung_df.nlargest(1, 'Customer_Rating').iloc[0]
            lowest = samsung_df.nsmallest(1, 'Customer_Rating').iloc[0]
            print(f"Highest Rated: {highest['Model']} - {highest['Customer_Rating']}/5")
            print(f"Lowest Rated: {lowest['Model']} - {lowest['Customer_Rating']}/5")
            pass
        if choice_3==8:
            print('Do you really want to exit?')
            print('1 - Yes')
            print('2 - No')
            choice_1_1=int(input('Enter your choice:'))
            if choice_1_1==1:
                print('See you soon.Thank you!!!')
                break
            if choice_1_1==2:
                pass
    if choice_2==2:
        print('Parameters for Analysis:')
        print('1 - Price Comparison(Least and Most Expensive model)')
        print('2 - Best selling Samsung phone')
        print('3 - Storage comparison')
        print('4 - Camera comparison')
        print('5 - Battery comparison')
        print('6 - Warranty comparison')
        print('7 - Rating comparison')
        print('8 - Exit')
        choice_3=int(input('Enter your choice : '))
        if choice_3==1:
           apple_df = sales_df[sales_df['Brand'] == 'Apple'].sort_values('Price')
           plt.figure(figsize=(10, 6))
           plt.bar(apple_df['Model'], apple_df['Price'], color='blue')
           plt.title('Apple Phones - Price Comparison', fontsize=14)
           plt.xlabel('Apple Models')
           plt.ylabel('Price (₹)')
           plt.xticks(rotation=45)
           plt.grid(axis='y', linestyle='--', alpha=0.7)
           plt.tight_layout()
           plt.show()
           print("Apple Phones - Price Comparison:")
           print(apple_df[['Model', 'Price']].to_string(index=False))
           cheapest_apple = apple_df.iloc[0]  
           most_expensive_apple = apple_df.iloc[-1] 
           print(" CHEAPEST APPLE PHONE:")
           print(f"Model: {cheapest_apple['Model']}")
           print(f"Price: ₹{cheapest_apple['Price']:,}")
           print(" MOST EXPENSIVE APPLE PHONE:")
           print(f"Model: {most_expensive_apple['Model']}")
           print(f"Price: ₹{most_expensive_apple['Price']:,}")
           pass
        if choice_3==2:
            apple_df = sales_df[sales_df['Brand'] == 'Apple'].sort_values('Units_Sold')
            plt.figure(figsize=(10, 6))
            plt.bar(apple_df['Model'], apple_df['Units_Sold'], color='pink')
            plt.title('Apple Phones - Units Sold', fontsize=14)
            plt.xlabel('Apple Models')
            plt.ylabel('Units Sold')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_selling_apple = apple_df.nlargest(1, 'Units_Sold').iloc[0]
            print("BEST SELLING APPLE PHONE:")
            print(f"Model: {best_selling_apple['Model']}")
            print(f"Units Sold: {best_selling_apple['Units_Sold']:,}")
            print(f"Price: ₹{best_selling_apple['Price']:,}")
            pass
        if choice_3==3:
            apple_df = sales_df[sales_df['Brand'] == 'Apple'].sort_values('Storage_GB')
            plt.figure(figsize=(10, 6))
            plt.bar(apple_df['Model'], apple_df['Storage_GB'], color='green')
            plt.title('Apple Phones - Storage Comparison', fontsize=14)
            plt.xlabel('Apple Models')
            plt.ylabel('Storage (GB)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            highest_storage_apple = apple_df.nlargest(1, 'Storage_GB').iloc[0]
            print("Apple Phones - Storage Comparison:")
            print(apple_df[['Model', 'Storage_GB']].to_string(index=False))
            print(" APPLE PHONE WITH HIGHEST STORAGE:")
            print(f"Model: {highest_storage_apple['Model']}")
            print(f"Storage: {highest_storage_apple['Storage_GB']} GB")
            print(f"Price: ₹{highest_storage_apple['Price']:,}")
            pass
        if choice_3==4:
            apple_df = sales_df[sales_df['Brand'] == 'Apple'].sort_values('Camera_MP')
            plt.figure(figsize=(10, 6))
            plt.bar(apple_df['Model'], apple_df['Camera_MP'], color='purple')
            plt.title('Apple Phones - Camera Comparison', fontsize=14)
            plt.xlabel('Apple Models')
            plt.ylabel('Camera Megapixels (MP)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_camera_apple = apple_df.nlargest(1, 'Camera_MP').iloc[0]
            print("Apple Phones - Camera Comparison:")
            print(apple_df[['Model', 'Camera_MP']].to_string(index=False))
            print("APPLE PHONE WITH BEST CAMERA:")
            print(f"Model: {best_camera_apple['Model']}")
            print(f"Camera: {best_camera_apple['Camera_MP']} MP")
            print(f"Price: ₹{best_camera_apple['Price']:,}")
            pass
        if choice_3==5:
            apple_df = sales_df[sales_df['Brand'] == 'Apple'].sort_values('Battery_mAh')
            plt.figure(figsize=(10, 6))
            plt.bar(apple_df['Model'], apple_df['Battery_mAh'], color='orange')
            plt.title('Apple Phones - Battery Comparison', fontsize=14)
            plt.xlabel('Apple Models')
            plt.ylabel('Battery Capacity (mAh)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_battery_apple = apple_df.nlargest(1, 'Battery_mAh').iloc[0]
            print("Apple Phones - Battery Comparison:")
            print(apple_df[['Model', 'Battery_mAh']].to_string(index=False))
            print("APPLE PHONE WITH BEST BATTERY:")
            print(f"Model: {best_battery_apple['Model']}")
            print(f"Battery: {best_battery_apple['Battery_mAh']} mAh")
            print(f"Price: ₹{best_battery_apple['Price']:,}")
            pass
        if choice_3==6:
            apple_df = sales_df[sales_df['Brand'] == 'Apple'].sort_values('Warranty_Years')
            plt.figure(figsize=(10, 6))
            plt.bar(apple_df['Model'], apple_df['Warranty_Years'], color='brown')
            plt.title('Apple Phones - Warranty Comparison', fontsize=14)
            plt.xlabel('Apple Models')
            plt.ylabel('Warranty (Years)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_warranty_apple = apple_df.nlargest(1, 'Warranty_Years').iloc[0]
            print("Apple Phones - Warranty Comparison:")
            print(apple_df[['Model', 'Warranty_Years']].to_string(index=False))
            print("APPLE PHONE WITH BEST WARRANTY:")
            print(f"Model: {best_warranty_apple['Model']}")
            print(f"Warranty: {best_warranty_apple['Warranty_Years']} years")
            print(f"Price: ₹{best_warranty_apple['Price']:,}")
            pass
        if choice_3==7:
            apple_df = sales_df[sales_df['Brand'] == 'Apple'].sort_values('Customer_Rating')
            plt.barh(apple_df['Model'], apple_df['Customer_Rating'])
            plt.title('Apple Customer Ratings')
            plt.show()
            highest = apple_df.nlargest(1, 'Customer_Rating').iloc[0]
            lowest = apple_df.nsmallest(1, 'Customer_Rating').iloc[0]
            print(f"Highest Rated: {highest['Model']} - {highest['Customer_Rating']}/5")
            print(f"Lowest Rated: {lowest['Model']} - {lowest['Customer_Rating']}/5")
            pass
        if choice_3==8:
            print('Do you really want to exit?')
            print('1 - Yes')
            print('2 - No')
            choice_1_1=int(input('Enter your choice:'))
            if choice_1_1==1:
                print('See you soon.Thank you!!!')
                break
            if choice_1_1==2:
                pass
    if choice_2==3:
        print('Parameters for Analysis:')
        print('1 - Price Comparison(Least and Most Expensive model)')
        print('2 - Best selling Samsung phone')
        print('3 - Storage comparison')
        print('4 - Camera comparison')
        print('5 - Battery comparison')
        print('6 - Warranty comparison')
        print('7 - Rating comparison')
        print('8 - Exit')
        choice_3=int(input('Enter your choice : '))
        if choice_3==1:
            xiaomi_df = sales_df[sales_df['Brand'] == 'Xiaomi'].sort_values('Price')
            plt.figure(figsize=(10, 6))
            plt.bar(xiaomi_df['Model'], xiaomi_df['Price'], color='blue')
            plt.title('Xiaomi Phones - Price Comparison', fontsize=14)
            plt.xlabel('Xiaomi Models')
            plt.ylabel('Price (₹)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            print("Xiaomi Phones - Price Comparison:")
            print(xiaomi_df[['Model', 'Price']].to_string(index=False))
            cheapest_xiaomi = xiaomi_df.iloc[0]  
            most_expensive_xiaomi = xiaomi_df.iloc[-1] 
            print(" CHEAPEST XIAOMI PHONE:")
            print(f"Model: {cheapest_xiaomi['Model']}")
            print(f"Price: ₹{cheapest_xiaomi['Price']:,}")
            print(" MOST EXPENSIVE XIAOMI PHONE:")
            print(f"Model: {most_expensive_xiaomi['Model']}")
            print(f"Price: ₹{most_expensive_xiaomi['Price']:,}")
            pass
        if choice_3==2:
            xiaomi_df = sales_df[sales_df['Brand'] == 'Xiaomi'].sort_values('Units_Sold')
            plt.figure(figsize=(10, 6))
            plt.bar(xiaomi_df['Model'], xiaomi_df['Units_Sold'], color='pink')
            plt.title('Xiaomi Phones - Units Sold', fontsize=14)
            plt.xlabel('Xiaomi Models')
            plt.ylabel('Units Sold')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_selling_xiaomi = xiaomi_df.nlargest(1, 'Units_Sold').iloc[0]
            print("BEST SELLING XIAOMI PHONE:")
            print(f"Model: {best_selling_xiaomi['Model']}")
            print(f"Units Sold: {best_selling_xiaomi['Units_Sold']:,}")
            print(f"Price: ₹{best_selling_xiaomi['Price']:,}")
            pass
        if choice_3==3:
            xiaomi_df = sales_df[sales_df['Brand'] == 'Xiaomi'].sort_values('Storage_GB')
            plt.figure(figsize=(10, 6))
            plt.bar(xiaomi_df['Model'], xiaomi_df['Storage_GB'], color='green')
            plt.title('Xiaomi Phones - Storage Comparison', fontsize=14)
            plt.xlabel('Xiaomi Models')
            plt.ylabel('Storage (GB)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            highest_storage_xiaomi = xiaomi_df.nlargest(1, 'Storage_GB').iloc[0]
            print("Xiaomi Phones - Storage Comparison:")
            print(xiaomi_df[['Model', 'Storage_GB']].to_string(index=False))
            print(" XIAOMI PHONE WITH HIGHEST STORAGE:")
            print(f"Model: {highest_storage_xiaomi['Model']}")
            print(f"Storage: {highest_storage_xiaomi['Storage_GB']} GB")
            print(f"Price: ₹{highest_storage_xiaomi['Price']:,}")
            pass
        if choice_3==4:
            xiaomi_df = sales_df[sales_df['Brand'] == 'Xiaomi'].sort_values('Camera_MP')
            plt.figure(figsize=(10, 6))
            plt.bar(xiaomi_df['Model'], xiaomi_df['Camera_MP'], color='purple')
            plt.title('Xiaomi Phones - Camera Comparison', fontsize=14)
            plt.xlabel('Xiaomi Models')
            plt.ylabel('Camera Megapixels (MP)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_camera_xiaomi = xiaomi_df.nlargest(1, 'Camera_MP').iloc[0]
            print("Xiaomi Phones - Camera Comparison:")
            print(xiaomi_df[['Model', 'Camera_MP']].to_string(index=False))
            print("XIAOMI PHONE WITH BEST CAMERA:")
            print(f"Model: {best_camera_xiaomi['Model']}")
            print(f"Camera: {best_camera_xiaomi['Camera_MP']} MP")
            print(f"Price: ₹{best_camera_xiaomi['Price']:,}")
            pass
        if choice_3==5:
            xiaomi_df = sales_df[sales_df['Brand'] == 'Xiaomi'].sort_values('Battery_mAh')
            plt.figure(figsize=(10, 6))
            plt.bar(xiaomi_df['Model'], xiaomi_df['Battery_mAh'], color='orange')
            plt.title('Xiaomi Phones - Battery Comparison', fontsize=14)
            plt.xlabel('Xiaomi Models')
            plt.ylabel('Battery Capacity (mAh)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_battery_xiaomi = xiaomi_df.nlargest(1, 'Battery_mAh').iloc[0]
            print("Xiaomi Phones - Battery Comparison:")
            print(xiaomi_df[['Model', 'Battery_mAh']].to_string(index=False))
            print("XIAOMI PHONE WITH BEST BATTERY:")
            print(f"Model: {best_battery_xiaomi['Model']}")
            print(f"Battery: {best_battery_xiaomi['Battery_mAh']} mAh")
            print(f"Price: ₹{best_battery_xiaomi['Price']:,}")
            pass
        if choice_3==6:
            xiaomi_df = sales_df[sales_df['Brand'] == 'Xiaomi'].sort_values('Warranty_Years')
            plt.figure(figsize=(10, 6))
            plt.bar(xiaomi_df['Model'], xiaomi_df['Warranty_Years'], color='brown')
            plt.title('Xiaomi Phones - Warranty Comparison', fontsize=14)
            plt.xlabel('Xiaomi Models')
            plt.ylabel('Warranty (Years)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_warranty_xiaomi = xiaomi_df.nlargest(1, 'Warranty_Years').iloc[0]
            print("Xiaomi Phones - Warranty Comparison:")
            print(xiaomi_df[['Model', 'Warranty_Years']].to_string(index=False))
            print("XIAOMI PHONE WITH BEST WARRANTY:")
            print(f"Model: {best_warranty_xiaomi['Model']}")
            print(f"Warranty: {best_warranty_xiaomi['Warranty_Years']} years")
            print(f"Price: ₹{best_warranty_xiaomi['Price']:,}")
            pass
        if choice_3==7:
            Xiaomi_df = sales_df[sales_df['Brand'] == 'Xiaomi'].sort_values('Customer_Rating')
            plt.barh(Xiaomi_df['Model'], Xiaomi_df['Customer_Rating'])
            plt.title('Xiaomi Customer Ratings')
            plt.show()
            highest = Xiaomi_df.nlargest(1, 'Customer_Rating').iloc[0]
            lowest = Xiaomi_df.nsmallest(1, 'Customer_Rating').iloc[0]
            print(f"Highest Rated: {highest['Model']} - {highest['Customer_Rating']}/5")
            print(f"Lowest Rated: {lowest['Model']} - {lowest['Customer_Rating']}/5")
            pass
        if choice_3==8:
            print('Do you really want to exit?')
            print('1 - Yes')
            print('2 - No')
            choice_1_1=int(input('Enter your choice:'))
            if choice_1_1==1:
                print('See you soon.Thank you!!!')
                break
            if choice_1_1==2:
                pass
    if choice_2==4:
        print('Parameters for Analysis:')
        print('1 - Price Comparison(Least and Most Expensive model)')
        print('2 - Best selling Samsung phone')
        print('3 - Storage comparison')
        print('4 - Camera comparison')
        print('5 - Battery comparison')
        print('6 - Warranty comparison')
        print('7 - Rating comparison')
        print('8 - Exit')
        choice_3=int(input('Enter your choice : '))
        if choice_3==1:
            OnePlus_df = sales_df[sales_df['Brand'] == 'OnePlus'].sort_values('Price')
            plt.figure(figsize=(10, 6))
            plt.bar(OnePlus_df['Model'], OnePlus_df['Price'], color='blue')
            plt.title('OnePlus Phones - Price Comparison', fontsize=14)
            plt.xlabel('OnePlus Models')
            plt.ylabel('Price (₹)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            print("OnePlus Phones - Price Comparison:")
            print(OnePlus_df[['Model', 'Price']].to_string(index=False))
            cheapest_OnePlus = OnePlus_df.iloc[0]  
            most_expensive_OnePlus = OnePlus_df.iloc[-1] 
            print(" CHEAPEST ONEPLUS PHONE:")
            print(f"Model: {cheapest_OnePlus['Model']}")
            print(f"Price: ₹{cheapest_OnePlus['Price']:,}")
            print(" MOST EXPENSIVE ONEPLUS PHONE:")
            print(f"Model: {most_expensive_OnePlus['Model']}")
            print(f"Price: ₹{most_expensive_OnePlus['Price']:,}")
            pass
        if choice_3==2:
            OnePlus_df = sales_df[sales_df['Brand'] == 'OnePlus'].sort_values('Units_Sold')
            plt.figure(figsize=(10, 6))
            plt.bar(OnePlus_df['Model'], OnePlus_df['Units_Sold'], color='pink')
            plt.title('OnePlus Phones - Units Sold', fontsize=14)
            plt.xlabel('OnePlus Models')
            plt.ylabel('Units Sold')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_selling_OnePlus = OnePlus_df.nlargest(1, 'Units_Sold').iloc[0]
            print("BEST SELLING ONEPLUS PHONE:")
            print(f"Model: {best_selling_OnePlus['Model']}")
            print(f"Units Sold: {best_selling_OnePlus['Units_Sold']:,}")
            print(f"Price: ₹{best_selling_OnePlus['Price']:,}")
            pass
        if choice_3==3:
            OnePlus_df = sales_df[sales_df['Brand'] == 'OnePlus'].sort_values('Storage_GB')
            plt.figure(figsize=(10, 6))
            plt.bar(OnePlus_df['Model'], OnePlus_df['Storage_GB'], color='green')
            plt.title('OnePlus Phones - Storage Comparison', fontsize=14)
            plt.xlabel('OnePlus Models')
            plt.ylabel('Storage (GB)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            highest_storage_OnePlus = OnePlus_df.nlargest(1, 'Storage_GB').iloc[0]
            print("OnePlus Phones - Storage Comparison:")
            print(OnePlus_df[['Model', 'Storage_GB']].to_string(index=False))
            print(" ONEPLUS PHONE WITH HIGHEST STORAGE:")
            print(f"Model: {highest_storage_OnePlus['Model']}")
            print(f"Storage: {highest_storage_OnePlus['Storage_GB']} GB")
            print(f"Price: ₹{highest_storage_OnePlus['Price']:,}")
            pass
        if choice_3==4:
            OnePlus_df = sales_df[sales_df['Brand'] == 'OnePlus'].sort_values('Camera_MP')
            plt.figure(figsize=(10, 6))
            plt.bar(OnePlus_df['Model'], OnePlus_df['Camera_MP'], color='purple')
            plt.title('OnePlus Phones - Camera Comparison', fontsize=14)
            plt.xlabel('OnePlus Models')
            plt.ylabel('Camera Megapixels (MP)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_camera_OnePlus = OnePlus_df.nlargest(1, 'Camera_MP').iloc[0]
            print("OnePlus Phones - Camera Comparison:")
            print(OnePlus_df[['Model', 'Camera_MP']].to_string(index=False))
            print("ONEPLUS PHONE WITH BEST CAMERA:")
            print(f"Model: {best_camera_OnePlus['Model']}")
            print(f"Camera: {best_camera_OnePlus['Camera_MP']} MP")
            print(f"Price: ₹{best_camera_OnePlus['Price']:,}")
            pass
        if choice_3==5:
            OnePlus_df = sales_df[sales_df['Brand'] == 'OnePlus'].sort_values('Battery_mAh')
            plt.figure(figsize=(10, 6))
            plt.bar(OnePlus_df['Model'], OnePlus_df['Battery_mAh'], color='orange')
            plt.title('OnePlus Phones - Battery Comparison', fontsize=14)
            plt.xlabel('OnePlus Models')
            plt.ylabel('Battery Capacity (mAh)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_battery_OnePlus = OnePlus_df.nlargest(1, 'Battery_mAh').iloc[0]
            print("OnePlus Phones - Battery Comparison:")
            print(OnePlus_df[['Model', 'Battery_mAh']].to_string(index=False))
            print("ONEPLUS PHONE WITH BEST BATTERY:")
            print(f"Model: {best_battery_OnePlus['Model']}")
            print(f"Battery: {best_battery_OnePlus['Battery_mAh']} mAh")
            print(f"Price: ₹{best_battery_OnePlus['Price']:,}")
            pass
        if choice_3==6:
            OnePlus_df = sales_df[sales_df['Brand'] == 'OnePlus'].sort_values('Warranty_Years')
            plt.figure(figsize=(10, 6))
            plt.bar(OnePlus_df['Model'], OnePlus_df['Warranty_Years'], color='brown')
            plt.title('OnePlus Phones - Warranty Comparison', fontsize=14)
            plt.xlabel('OnePlus Models')
            plt.ylabel('Warranty (Years)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_warranty_OnePlus = OnePlus_df.nlargest(1, 'Warranty_Years').iloc[0]
            print("OnePlus Phones - Warranty Comparison:")
            print(OnePlus_df[['Model', 'Warranty_Years']].to_string(index=False))
            print("ONEPLUS PHONE WITH BEST WARRANTY:")
            print(f"Model: {best_warranty_OnePlus['Model']}")
            print(f"Warranty: {best_warranty_OnePlus['Warranty_Years']} years")
            print(f"Price: ₹{best_warranty_OnePlus['Price']:,}")
            pass
        if choice_3==7:
            OnePlus_df = sales_df[sales_df['Brand'] == 'OnePlus'].sort_values('Customer_Rating')
            plt.barh(OnePlus_df['Model'], OnePlus_df['Customer_Rating'])
            plt.title('OnePlus Customer Ratings')
            plt.show()
            highest = OnePlus_df.nlargest(1, 'Customer_Rating').iloc[0]
            lowest = OnePlus_df.nsmallest(1, 'Customer_Rating').iloc[0]
            print(f"Highest Rated: {highest['Model']} - {highest['Customer_Rating']}/5")
            print(f"Lowest Rated: {lowest['Model']} - {lowest['Customer_Rating']}/5")
            pass
        if choice_3==8:
            print('Do you really want to exit?')
            print('1 - Yes')
            print('2 - No')
            choice_1_1=int(input('Enter your choice:'))
            if choice_1_1==1:
                print('See you soon.Thank you!!!')
                break
            if choice_1_1==2:
                pass
    if choice_2==5:
        print('Parameters for Analysis:')
        print('1 - Price Comparison(Least and Most Expensive model)')
        print('2 - Best selling Samsung phone')
        print('3 - Storage comparison')
        print('4 - Camera comparison')
        print('5 - Battery comparison')
        print('6 - Warranty comparison')
        print('7 - Rating comparison')
        print('8 - Exit')
        choice_3=int(input('Enter your choice : '))
        if choice_3==1:
           oppo_df = sales_df[sales_df['Brand'] == 'Oppo'].sort_values('Price')
           plt.figure(figsize=(10, 6))
           plt.bar(oppo_df['Model'], oppo_df['Price'], color='blue')
           plt.title('Oppo Phones - Price Comparison', fontsize=14)
           plt.xlabel('Oppo Models')
           plt.ylabel('Price (₹)')
           plt.xticks(rotation=45)
           plt.grid(axis='y', linestyle='--', alpha=0.7)
           plt.tight_layout()
           plt.show()
           print("Oppo Phones - Price Comparison:")
           print(oppo_df[['Model', 'Price']].to_string(index=False))
           cheapest_oppo = oppo_df.iloc[0]  
           most_expensive_oppo = oppo_df.iloc[-1] 
           print(" CHEAPEST OPPO PHONE:")
           print(f"Model: {cheapest_oppo['Model']}")
           print(f"Price: ₹{cheapest_oppo['Price']:,}")
           print(" MOST EXPENSIVE OPPO PHONE:")
           print(f"Model: {most_expensive_oppo['Model']}")
           print(f"Price: ₹{most_expensive_oppo['Price']:,}")
           pass
        if choice_3==2:
           oppo_df = sales_df[sales_df['Brand'] == 'Oppo'].sort_values('Units_Sold')
           plt.figure(figsize=(10, 6))
           plt.bar(oppo_df['Model'], oppo_df['Units_Sold'], color='pink')
           plt.title('Oppo Phones - Units Sold', fontsize=14)
           plt.xlabel('Oppo Models')
           plt.ylabel('Units Sold')
           plt.xticks(rotation=45)
           plt.grid(axis='y', linestyle='--', alpha=0.7)
           plt.tight_layout()
           plt.show()
           best_selling_oppo = oppo_df.nlargest(1, 'Units_Sold').iloc[0]
           print("BEST SELLING OPPO PHONE:")
           print(f"Model: {best_selling_oppo['Model']}")
           print(f"Units Sold: {best_selling_oppo['Units_Sold']:,}")
           print(f"Price: ₹{best_selling_oppo['Price']:,}")
           pass
        if choice_3==3:
            oppo_df = sales_df[sales_df['Brand'] == 'Oppo'].sort_values('Storage_GB')
            plt.figure(figsize=(10, 6))
            plt.bar(oppo_df['Model'], oppo_df['Storage_GB'], color='green')
            plt.title('Oppo Phones - Storage Comparison', fontsize=14)
            plt.xlabel('Oppo Models')
            plt.ylabel('Storage (GB)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            highest_storage_oppo = oppo_df.nlargest(1, 'Storage_GB').iloc[0]
            print("Oppo Phones - Storage Comparison:")
            print(oppo_df[['Model', 'Storage_GB']].to_string(index=False))
            print(" OPPO PHONE WITH HIGHEST STORAGE:")
            print(f"Model: {highest_storage_oppo['Model']}")
            print(f"Storage: {highest_storage_oppo['Storage_GB']} GB")
            print(f"Price: ₹{highest_storage_oppo['Price']:,}")
            pass
        if choice_3==4:
            oppo_df = sales_df[sales_df['Brand'] == 'Oppo'].sort_values('Camera_MP')
            plt.figure(figsize=(10, 6))
            plt.bar(oppo_df['Model'], oppo_df['Camera_MP'], color='purple')
            plt.title('Oppo Phones - Camera Comparison', fontsize=14)
            plt.xlabel('Oppo Models')
            plt.ylabel('Camera Megapixels (MP)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_camera_oppo = oppo_df.nlargest(1, 'Camera_MP').iloc[0]
            print("Oppo Phones - Camera Comparison:")
            print(oppo_df[['Model', 'Camera_MP']].to_string(index=False))
            print("OPPO PHONE WITH BEST CAMERA:")
            print(f"Model: {best_camera_oppo['Model']}")
            print(f"Camera: {best_camera_oppo['Camera_MP']} MP")
            print(f"Price: ₹{best_camera_oppo['Price']:,}")
            pass
        if choice_3==5:
            oppo_df = sales_df[sales_df['Brand'] == 'Oppo'].sort_values('Battery_mAh')
            plt.figure(figsize=(10, 6))
            plt.bar(oppo_df['Model'], oppo_df['Battery_mAh'], color='orange')
            plt.title('Oppo Phones - Battery Comparison', fontsize=14)
            plt.xlabel('Oppo Models')
            plt.ylabel('Battery Capacity (mAh)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_battery_oppo = oppo_df.nlargest(1, 'Battery_mAh').iloc[0]
            print("Oppo Phones - Battery Comparison:")
            print(oppo_df[['Model', 'Battery_mAh']].to_string(index=False))
            print("OPPO PHONE WITH BEST BATTERY:")
            print(f"Model: {best_battery_oppo['Model']}")
            print(f"Battery: {best_battery_oppo['Battery_mAh']} mAh")
            print(f"Price: ₹{best_battery_oppo['Price']:,}")
            pass
        if choice_3==6:
            oppo_df = sales_df[sales_df['Brand'] == 'Oppo'].sort_values('Warranty_Years')
            plt.figure(figsize=(10, 6))
            plt.bar(oppo_df['Model'], oppo_df['Warranty_Years'], color='brown')
            plt.title('Oppo Phones - Warranty Comparison', fontsize=14)
            plt.xlabel('Oppo Models')
            plt.ylabel('Warranty (Years)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_warranty_oppo = oppo_df.nlargest(1, 'Warranty_Years').iloc[0]
            print("Oppo Phones - Warranty Comparison:")
            print(oppo_df[['Model', 'Warranty_Years']].to_string(index=False))
            print("OPPO PHONE WITH BEST WARRANTY:")
            print(f"Model: {best_warranty_oppo['Model']}")
            print(f"Warranty: {best_warranty_oppo['Warranty_Years']} years")
            print(f"Price: ₹{best_warranty_oppo['Price']:,}")
            pass
        if choice_3==7:
            Oppo_df = sales_df[sales_df['Brand'] == 'Oppo'].sort_values('Customer_Rating')
            plt.barh(Oppo_df['Model'], Oppo_df['Customer_Rating'])
            plt.title('Oppo Customer Ratings')
            plt.show()
            highest = Oppo_df.nlargest(1, 'Customer_Rating').iloc[0]
            lowest = Oppo_df.nsmallest(1, 'Customer_Rating').iloc[0]
            print(f"Highest Rated: {highest['Model']} - {highest['Customer_Rating']}/5")
            print(f"Lowest Rated: {lowest['Model']} - {lowest['Customer_Rating']}/5")
            pass
        if choice_3==8:
            print('Do you really want to exit?')
            print('1 - Yes')
            print('2 - No')
            choice_1_1=int(input('Enter your choice:'))
            if choice_1_1==1:
                print('See you soon.Thank you!!!')
                break
            if choice_1_1==2:
                pass
    if choice_2==6:
        print('Parameters for Analysis:')
        print('1 - Price Comparison(Least and Most Expensive model)')
        print('2 - Best selling Samsung phone')
        print('3 - Storage comparison')
        print('4 - Camera comparison')
        print('5 - Battery comparison')
        print('6 - Warranty comparison')
        print('7 - Rating comparison')
        print('8 - Exit')
        choice_3=int(input('Enter your choice : '))
        if choice_3==1:
           vivo_df = sales_df[sales_df['Brand'] == 'Vivo'].sort_values('Price')
           plt.figure(figsize=(10, 6))
           plt.bar(vivo_df['Model'], vivo_df['Price'], color='blue')
           plt.title('Vivo Phones - Price Comparison', fontsize=14)
           plt.xlabel('Vivo Models')
           plt.ylabel('Price (₹)')
           plt.xticks(rotation=45)
           plt.grid(axis='y', linestyle='--', alpha=0.7)
           plt.tight_layout()
           plt.show()
           print("Vivo Phones - Price Comparison:")
           print(vivo_df[['Model', 'Price']].to_string(index=False))
           cheapest_vivo = vivo_df.iloc[0]  
           most_expensive_vivo = vivo_df.iloc[-1] 
           print(" CHEAPEST VIVO PHONE:")
           print(f"Model: {cheapest_vivo['Model']}")
           print(f"Price: ₹{cheapest_vivo['Price']:,}")
           print(" MOST EXPENSIVE VIVO PHONE:")
           print(f"Model: {most_expensive_vivo['Model']}")
           print(f"Price: ₹{most_expensive_vivo['Price']:,}")
           pass
        if choice_3==2:
           vivo_df = sales_df[sales_df['Brand'] == 'Vivo'].sort_values('Units_Sold')
           plt.figure(figsize=(10, 6))
           plt.bar(vivo_df['Model'], vivo_df['Units_Sold'], color='pink')
           plt.title('Vivo Phones - Units Sold', fontsize=14)
           plt.xlabel('Vivo Models')
           plt.ylabel('Units Sold')
           plt.xticks(rotation=45)
           plt.grid(axis='y', linestyle='--', alpha=0.7)
           plt.tight_layout()
           plt.show()
           best_selling_vivo = vivo_df.nlargest(1, 'Units_Sold').iloc[0]
           print("BEST SELLING VIVO PHONE:")
           print(f"Model: {best_selling_vivo['Model']}")
           print(f"Units Sold: {best_selling_vivo['Units_Sold']:,}")
           print(f"Price: ₹{best_selling_vivo['Price']:,}")
           pass
        if choice_3==3:
            vivo_df = sales_df[sales_df['Brand'] == 'Vivo'].sort_values('Storage_GB')
            plt.figure(figsize=(10, 6))
            plt.bar(vivo_df['Model'], vivo_df['Storage_GB'], color='green')
            plt.title('Vivo Phones - Storage Comparison', fontsize=14)
            plt.xlabel('Vivo Models')
            plt.ylabel('Storage (GB)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            highest_storage_vivo = vivo_df.nlargest(1, 'Storage_GB').iloc[0]
            print("Vivo Phones - Storage Comparison:")
            print(vivo_df[['Model', 'Storage_GB']].to_string(index=False))
            print(" VIVO PHONE WITH HIGHEST STORAGE:")
            print(f"Model: {highest_storage_vivo['Model']}")
            print(f"Storage: {highest_storage_vivo['Storage_GB']} GB")
            print(f"Price: ₹{highest_storage_vivo['Price']:,}")
            pass
        if choice_3==4:
            vivo_df = sales_df[sales_df['Brand'] == 'Vivo'].sort_values('Camera_MP')
            plt.figure(figsize=(10, 6))
            plt.bar(vivo_df['Model'], vivo_df['Camera_MP'], color='purple')
            plt.title('Vivo Phones - Camera Comparison', fontsize=14)
            plt.xlabel('Vivo Models')
            plt.ylabel('Camera Megapixels (MP)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_camera_vivo = vivo_df.nlargest(1, 'Camera_MP').iloc[0]
            print("Vivo Phones - Camera Comparison:")
            print(vivo_df[['Model', 'Camera_MP']].to_string(index=False))
            print("VIVO PHONE WITH BEST CAMERA:")
            print(f"Model: {best_camera_vivo['Model']}")
            print(f"Camera: {best_camera_vivo['Camera_MP']} MP")
            print(f"Price: ₹{best_camera_vivo['Price']:,}")
            pass
        if choice_3==5:
            vivo_df = sales_df[sales_df['Brand'] == 'Vivo'].sort_values('Battery_mAh')
            plt.figure(figsize=(10, 6))
            plt.bar(vivo_df['Model'], vivo_df['Battery_mAh'], color='orange')
            plt.title('Vivo Phones - Battery Comparison', fontsize=14)
            plt.xlabel('Vivo Models')
            plt.ylabel('Battery Capacity (mAh)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_battery_vivo = vivo_df.nlargest(1, 'Battery_mAh').iloc[0]
            print("Vivo Phones - Battery Comparison:")
            print(vivo_df[['Model', 'Battery_mAh']].to_string(index=False))
            print("VIVO PHONE WITH BEST BATTERY:")
            print(f"Model: {best_battery_vivo['Model']}")
            print(f"Battery: {best_battery_vivo['Battery_mAh']} mAh")
            print(f"Price: ₹{best_battery_vivo['Price']:,}")
            pass
        if choice_3==6:
            vivo_df = sales_df[sales_df['Brand'] == 'Vivo'].sort_values('Warranty_Years')
            plt.figure(figsize=(10, 6))
            plt.bar(vivo_df['Model'], vivo_df['Warranty_Years'], color='brown')
            plt.title('Vivo Phones - Warranty Comparison', fontsize=14)
            plt.xlabel('Vivo Models')
            plt.ylabel('Warranty (Years)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_warranty_vivo = vivo_df.nlargest(1, 'Warranty_Years').iloc[0]
            print("Vivo Phones - Warranty Comparison:")
            print(vivo_df[['Model', 'Warranty_Years']].to_string(index=False))
            print("VIVO PHONE WITH BEST WARRANTY:")
            print(f"Model: {best_warranty_vivo['Model']}")
            print(f"Warranty: {best_warranty_vivo['Warranty_Years']} years")
            print(f"Price: ₹{best_warranty_vivo['Price']:,}")
            pass
        if choice_3==7:
           Vivo_df = sales_df[sales_df['Brand'] == 'Vivo'].sort_values('Customer_Rating')
           plt.barh(Vivo_df['Model'], Vivo_df['Customer_Rating'])
           plt.title('Vivo Customer Ratings')
           plt.show()
           highest = Vivo_df.nlargest(1, 'Customer_Rating').iloc[0]
           lowest = Vivo_df.nsmallest(1, 'Customer_Rating').iloc[0]
           print(f"Highest Rated: {highest['Model']} - {highest['Customer_Rating']}/5")
           print(f"Lowest Rated: {lowest['Model']} - {lowest['Customer_Rating']}/5")
           pass
        if choice_3==8:
            print('Do you really want to exit?')
            print('1 - Yes')
            print('2 - No')
            choice_1_1=int(input('Enter your choice:'))
            if choice_1_1==1:
                print('See you soon.Thank you!!!')
                break
            if choice_1_1==2:
                pass
    if choice_2==7:
        print('Parameters for Analysis:')
        print('1 - Price Comparison(Least and Most Expensive model)')
        print('2 - Best selling Samsung phone')
        print('3 - Storage comparison')
        print('4 - Camera comparison')
        print('5 - Battery comparison')
        print('6 - Warranty comparison')
        print('7 - Rating comparison')
        print('8 - Exit')
        choice_3=int(input('Enter your choice : '))
        if choice_3==1:
           realme_df = sales_df[sales_df['Brand'] == 'Realme'].sort_values('Price')
           plt.figure(figsize=(10, 6))
           plt.bar(realme_df['Model'], realme_df['Price'], color='blue')
           plt.title('Realme Phones - Price Comparison', fontsize=14)
           plt.xlabel('Realme Models')
           plt.ylabel('Price (₹)')
           plt.xticks(rotation=45)
           plt.grid(axis='y', linestyle='--', alpha=0.7)
           plt.tight_layout()
           plt.show()
           print("Realme Phones - Price Comparison:")
           print(realme_df[['Model', 'Price']].to_string(index=False))
           cheapest_realme = realme_df.iloc[0]  
           most_expensive_realme = realme_df.iloc[-1] 
           print(" CHEAPEST REALME PHONE:")
           print(f"Model: {cheapest_realme['Model']}")
           print(f"Price: ₹{cheapest_realme['Price']:,}")
           print(" MOST EXPENSIVE REALME PHONE:")
           print(f"Model: {most_expensive_realme['Model']}")
           print(f"Price: ₹{most_expensive_realme['Price']:,}")
           pass
        if choice_3==2:
           realme_df = sales_df[sales_df['Brand'] == 'Realme'].sort_values('Units_Sold')
           plt.figure(figsize=(10, 6))
           plt.bar(realme_df['Model'], realme_df['Units_Sold'], color='pink')
           plt.title('Realme Phones - Units Sold', fontsize=14)
           plt.xlabel('Realme Models')
           plt.ylabel('Units Sold')
           plt.xticks(rotation=45)
           plt.grid(axis='y', linestyle='--', alpha=0.7)
           plt.tight_layout()
           plt.show()
           best_selling_realme = realme_df.nlargest(1, 'Units_Sold').iloc[0]
           print("BEST SELLING REALME PHONE:")
           print(f"Model: {best_selling_realme['Model']}")
           print(f"Units Sold: {best_selling_realme['Units_Sold']:,}")
           print(f"Price: ₹{best_selling_realme['Price']:,}")
           pass
        if choice_3==3:
            realme_df = sales_df[sales_df['Brand'] == 'Realme'].sort_values('Storage_GB')
            plt.figure(figsize=(10, 6))
            plt.bar(realme_df['Model'], realme_df['Storage_GB'], color='green')
            plt.title('Realme Phones - Storage Comparison', fontsize=14)
            plt.xlabel('Realme Models')
            plt.ylabel('Storage (GB)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            highest_storage_realme = realme_df.nlargest(1, 'Storage_GB').iloc[0]
            print("Realme Phones - Storage Comparison:")
            print(realme_df[['Model', 'Storage_GB']].to_string(index=False))
            print(" REALME PHONE WITH HIGHEST STORAGE:")
            print(f"Model: {highest_storage_realme['Model']}")
            print(f"Storage: {highest_storage_realme['Storage_GB']} GB")
            print(f"Price: ₹{highest_storage_realme['Price']:,}")
            pass
        if choice_3==4:
            realme_df = sales_df[sales_df['Brand'] == 'Realme'].sort_values('Camera_MP')
            plt.figure(figsize=(10, 6))
            plt.bar(realme_df['Model'], realme_df['Camera_MP'], color='purple')
            plt.title('Realme Phones - Camera Comparison', fontsize=14)
            plt.xlabel('Realme Models')
            plt.ylabel('Camera Megapixels (MP)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_camera_realme = realme_df.nlargest(1, 'Camera_MP').iloc[0]
            print("Realme Phones - Camera Comparison:")
            print(realme_df[['Model', 'Camera_MP']].to_string(index=False))
            print("REALME PHONE WITH BEST CAMERA:")
            print(f"Model: {best_camera_realme['Model']}")
            print(f"Camera: {best_camera_realme['Camera_MP']} MP")
            print(f"Price: ₹{best_camera_realme['Price']:,}")
            pass
        if choice_3==5:
            realme_df = sales_df[sales_df['Brand'] == 'Realme'].sort_values('Battery_mAh')
            plt.figure(figsize=(10, 6))
            plt.bar(realme_df['Model'], realme_df['Battery_mAh'], color='orange')
            plt.title('Realme Phones - Battery Comparison', fontsize=14)
            plt.xlabel('Realme Models')
            plt.ylabel('Battery Capacity (mAh)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_battery_realme = realme_df.nlargest(1, 'Battery_mAh').iloc[0]
            print("Realme Phones - Battery Comparison:")
            print(realme_df[['Model', 'Battery_mAh']].to_string(index=False))
            print("REALME PHONE WITH BEST BATTERY:")
            print(f"Model: {best_battery_realme['Model']}")
            print(f"Battery: {best_battery_realme['Battery_mAh']} mAh")
            print(f"Price: ₹{best_battery_realme['Price']:,}")
            pass
        if choice_3==6:
            realme_df = sales_df[sales_df['Brand'] == 'Realme'].sort_values('Warranty_Years')
            plt.figure(figsize=(10, 6))
            plt.bar(realme_df['Model'], realme_df['Warranty_Years'], color='brown')
            plt.title('Realme Phones - Warranty Comparison', fontsize=14)
            plt.xlabel('Realme Models')
            plt.ylabel('Warranty (Years)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_warranty_realme = realme_df.nlargest(1, 'Warranty_Years').iloc[0]
            print("Realme Phones - Warranty Comparison:")
            print(realme_df[['Model', 'Warranty_Years']].to_string(index=False))
            print("REALME PHONE WITH BEST WARRANTY:")
            print(f"Model: {best_warranty_realme['Model']}")
            print(f"Warranty: {best_warranty_realme['Warranty_Years']} years")
            print(f"Price: ₹{best_warranty_realme['Price']:,}")
            pass
        if choice_3==7:
            Realme_df = sales_df[sales_df['Brand'] == 'Realme'].sort_values('Customer_Rating')
            plt.barh(Realme_df['Model'], Realme_df['Customer_Rating'])
            plt.title('Realme Customer Ratings')
            plt.show()
            highest = Realme_df.nlargest(1, 'Customer_Rating').iloc[0]
            lowest = Realme_df.nsmallest(1, 'Customer_Rating').iloc[0]
            print(f"Highest Rated: {highest['Model']} - {highest['Customer_Rating']}/5")
            print(f"Lowest Rated: {lowest['Model']} - {lowest['Customer_Rating']}/5")
            pass
        if choice_3==8:
            print('Do you really want to exit?')
            print('1 - Yes')
            print('2 - No')
            choice_1_1=int(input('Enter your choice:'))
            if choice_1_1==1:
                print('See you soon.Thank you!!!')
                break
            if choice_1_1==2:
                pass
    if choice_2==8:
        print('Parameters for Analysis:')
        print('1 - Price Comparison(Least and Most Expensive model)')
        print('2 - Best selling Samsung phone')
        print('3 - Storage comparison')
        print('4 - Camera comparison')
        print('5 - Battery comparison')
        print('6 - Warranty comparison')
        print('7 - Rating comparison')
        print('8 - Exit')
        choice_3=int(input('Enter your choice : '))
        if choice_3==1:
           motorola_df = sales_df[sales_df['Brand'] == 'Motorola'].sort_values('Price')
           plt.figure(figsize=(10, 6))
           plt.bar(motorola_df['Model'], motorola_df['Price'], color='blue')
           plt.title('Motorola Phones - Price Comparison', fontsize=14)
           plt.xlabel('Motorola Models')
           plt.ylabel('Price (₹)')
           plt.xticks(rotation=45)
           plt.grid(axis='y', linestyle='--', alpha=0.7)
           plt.tight_layout()
           plt.show()
           print("Motorola Phones - Price Comparison:")
           print(motorola_df[['Model', 'Price']].to_string(index=False))
           cheapest_motorola = motorola_df.iloc[0]  
           most_expensive_motorola = motorola_df.iloc[-1] 
           print(" CHEAPEST MOTOROLA PHONE:")
           print(f"Model: {cheapest_motorola['Model']}")
           print(f"Price: ₹{cheapest_motorola['Price']:,}")
           print(" MOST EXPENSIVE MOTOROLA PHONE:")
           print(f"Model: {most_expensive_motorola['Model']}")
           print(f"Price: ₹{most_expensive_motorola['Price']:,}")
           pass
        if choice_3==2:
           motorola_df = sales_df[sales_df['Brand'] == 'Motorola'].sort_values('Units_Sold')
           plt.figure(figsize=(10, 6))
           plt.bar(motorola_df['Model'], motorola_df['Units_Sold'], color='pink')
           plt.title('Motorola Phones - Units Sold', fontsize=14)
           plt.xlabel('Motorola Models')
           plt.ylabel('Units Sold')
           plt.xticks(rotation=45)
           plt.grid(axis='y', linestyle='--', alpha=0.7)
           plt.tight_layout()
           plt.show()
           best_selling_motorola = motorola_df.nlargest(1, 'Units_Sold').iloc[0]
           print("BEST SELLING MOTOROLA PHONE:")
           print(f"Model: {best_selling_motorola['Model']}")
           print(f"Units Sold: {best_selling_motorola['Units_Sold']:,}")
           print(f"Price: ₹{best_selling_motorola['Price']:,}")
           pass
        if choice_3==3:
            motorola_df = sales_df[sales_df['Brand'] == 'Motorola'].sort_values('Storage_GB')
            plt.figure(figsize=(10, 6))
            plt.bar(motorola_df['Model'], motorola_df['Storage_GB'], color='green')
            plt.title('Motorola Phones - Storage Comparison', fontsize=14)
            plt.xlabel('Motorola Models')
            plt.ylabel('Storage (GB)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            highest_storage_motorola = motorola_df.nlargest(1, 'Storage_GB').iloc[0]
            print("Motorola Phones - Storage Comparison:")
            print(motorola_df[['Model', 'Storage_GB']].to_string(index=False))
            print(" MOTOROLA PHONE WITH HIGHEST STORAGE:")
            print(f"Model: {highest_storage_motorola['Model']}")
            print(f"Storage: {highest_storage_motorola['Storage_GB']} GB")
            print(f"Price: ₹{highest_storage_motorola['Price']:,}")
            pass
        if choice_3==4:
            motorola_df = sales_df[sales_df['Brand'] == 'Motorola'].sort_values('Camera_MP')
            plt.figure(figsize=(10, 6))
            plt.bar(motorola_df['Model'], motorola_df['Camera_MP'], color='purple')
            plt.title('Motorola Phones - Camera Comparison', fontsize=14)
            plt.xlabel('Motorola Models')
            plt.ylabel('Camera Megapixels (MP)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_camera_motorola = motorola_df.nlargest(1, 'Camera_MP').iloc[0]
            print("Motorola Phones - Camera Comparison:")
            print(motorola_df[['Model', 'Camera_MP']].to_string(index=False))
            print("MOTOROLA PHONE WITH BEST CAMERA:")
            print(f"Model: {best_camera_motorola['Model']}")
            print(f"Camera: {best_camera_motorola['Camera_MP']} MP")
            print(f"Price: ₹{best_camera_motorola['Price']:,}")
            pass
        if choice_3==5:
            motorola_df = sales_df[sales_df['Brand'] == 'Motorola'].sort_values('Battery_mAh')
            plt.figure(figsize=(10, 6))
            plt.bar(motorola_df['Model'], motorola_df['Battery_mAh'], color='orange')
            plt.title('Motorola Phones - Battery Comparison', fontsize=14)
            plt.xlabel('Motorola Models')
            plt.ylabel('Battery Capacity (mAh)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_battery_motorola = motorola_df.nlargest(1, 'Battery_mAh').iloc[0]
            print("Motorola Phones - Battery Comparison:")
            print(motorola_df[['Model', 'Battery_mAh']].to_string(index=False))
            print("MOTOROLA PHONE WITH BEST BATTERY:")
            print(f"Model: {best_battery_motorola['Model']}")
            print(f"Battery: {best_battery_motorola['Battery_mAh']} mAh")
            print(f"Price: ₹{best_battery_motorola['Price']:,}")
            pass
        if choice_3==6:
            motorola_df = sales_df[sales_df['Brand'] == 'Motorola'].sort_values('Warranty_Years')
            plt.figure(figsize=(10, 6))
            plt.bar(motorola_df['Model'], motorola_df['Warranty_Years'], color='brown')
            plt.title('Motorola Phones - Warranty Comparison', fontsize=14)
            plt.xlabel('Motorola Models')
            plt.ylabel('Warranty (Years)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_warranty_motorola = motorola_df.nlargest(1, 'Warranty_Years').iloc[0]
            print("Motorola Phones - Warranty Comparison:")
            print(motorola_df[['Model', 'Warranty_Years']].to_string(index=False))
            print("MOTOROLA PHONE WITH BEST WARRANTY:")
            print(f"Model: {best_warranty_motorola['Model']}")
            print(f"Warranty: {best_warranty_motorola['Warranty_Years']} years")
            print(f"Price: ₹{best_warranty_motorola['Price']:,}")
            pass
        if choice_3==7:
            Motorola_df = sales_df[sales_df['Brand'] == 'Motorola'].sort_values('Customer_Rating')
            plt.barh(Motorola_df['Model'], Motorola_df['Customer_Rating'])
            plt.title('Motorola Customer Ratings')
            plt.show()
            highest = Motorola_df.nlargest(1, 'Customer_Rating').iloc[0]
            lowest = Motorola_df.nsmallest(1, 'Customer_Rating').iloc[0]
            print(f"Highest Rated: {highest['Model']} - {highest['Customer_Rating']}/5")
            print(f"Lowest Rated: {lowest['Model']} - {lowest['Customer_Rating']}/5")
            pass
        if choice_3==8:
            print('Do you really want to exit?')
            print('1 - Yes')
            print('2 - No')
            choice_1_1=int(input('Enter your choice:'))
            if choice_1_1==1:
                print('See you soon.Thank you!!!')
                break
            if choice_1_1==2:
                pass
    if choice_2==9:
        print('Parameters for Analysis:')
        print('1 - Price Comparison(Least and Most Expensive model)')
        print('2 - Best selling Samsung phone')
        print('3 - Storage comparison')
        print('4 - Camera comparison')
        print('5 - Battery comparison')
        print('6 - Warranty comparison')
        print('7 - Rating comparison')
        print('8 - Exit')
        choice_3=int(input('Enter your choice : '))
        if choice_3==1:
           google_df = sales_df[sales_df['Brand'] == 'Google'].sort_values('Price')
           plt.figure(figsize=(10, 6))
           plt.bar(google_df['Model'], google_df['Price'], color='blue')
           plt.title('Google Phones - Price Comparison', fontsize=14)
           plt.xlabel('Google Models')
           plt.ylabel('Price (₹)')
           plt.xticks(rotation=45)
           plt.grid(axis='y', linestyle='--', alpha=0.7)
           plt.tight_layout()
           plt.show()
           print("Google Phones - Price Comparison:")
           print(google_df[['Model', 'Price']].to_string(index=False))
           cheapest_google = google_df.iloc[0]  
           most_expensive_google = google_df.iloc[-1] 
           print(" CHEAPEST GOOGLE PHONE:")
           print(f"Model: {cheapest_google['Model']}")
           print(f"Price: ₹{cheapest_google['Price']:,}")
           print(" MOST EXPENSIVE GOOGLE PHONE:")
           print(f"Model: {most_expensive_google['Model']}")
           print(f"Price: ₹{most_expensive_google['Price']:,}")
           pass
        if choice_3==2:
           google_df = sales_df[sales_df['Brand'] == 'Google'].sort_values('Units_Sold')
           plt.figure(figsize=(10, 6))
           plt.bar(google_df['Model'], google_df['Units_Sold'], color='pink')
           plt.title('Google Phones - Units Sold', fontsize=14)
           plt.xlabel('Google Models')
           plt.ylabel('Units Sold')
           plt.xticks(rotation=45)
           plt.grid(axis='y', linestyle='--', alpha=0.7)
           plt.tight_layout()
           plt.show()
           best_selling_google = google_df.nlargest(1, 'Units_Sold').iloc[0]
           print("BEST SELLING GOOGLE PHONE:")
           print(f"Model: {best_selling_google['Model']}")
           print(f"Units Sold: {best_selling_google['Units_Sold']:,}")
           print(f"Price: ₹{best_selling_google['Price']:,}")
           pass
        if choice_3==3:
            google_df = sales_df[sales_df['Brand'] == 'Google'].sort_values('Storage_GB')
            plt.figure(figsize=(10, 6))
            plt.bar(google_df['Model'], google_df['Storage_GB'], color='green')
            plt.title('Google Phones - Storage Comparison', fontsize=14)
            plt.xlabel('Google Models')
            plt.ylabel('Storage (GB)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            highest_storage_google = google_df.nlargest(1, 'Storage_GB').iloc[0]
            print("Google Phones - Storage Comparison:")
            print(google_df[['Model', 'Storage_GB']].to_string(index=False))
            print(" GOOGLE PHONE WITH HIGHEST STORAGE:")
            print(f"Model: {highest_storage_google['Model']}")
            print(f"Storage: {highest_storage_google['Storage_GB']} GB")
            print(f"Price: ₹{highest_storage_google['Price']:,}")
            pass
        if choice_3==4:
            google_df = sales_df[sales_df['Brand'] == 'Google'].sort_values('Camera_MP')
            plt.figure(figsize=(10, 6))
            plt.bar(google_df['Model'], google_df['Camera_MP'], color='purple')
            plt.title('Google Phones - Camera Comparison', fontsize=14)
            plt.xlabel('Google Models')
            plt.ylabel('Camera Megapixels (MP)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_camera_google = google_df.nlargest(1, 'Camera_MP').iloc[0]
            print("Google Phones - Camera Comparison:")
            print(google_df[['Model', 'Camera_MP']].to_string(index=False))
            print("GOOGLE PHONE WITH BEST CAMERA:")
            print(f"Model: {best_camera_google['Model']}")
            print(f"Camera: {best_camera_google['Camera_MP']} MP")
            print(f"Price: ₹{best_camera_google['Price']:,}")
            pass
        if choice_3==5:
            google_df = sales_df[sales_df['Brand'] == 'Google'].sort_values('Battery_mAh')
            plt.figure(figsize=(10, 6))
            plt.bar(google_df['Model'], google_df['Battery_mAh'], color='orange')
            plt.title('Google Phones - Battery Comparison', fontsize=14)
            plt.xlabel('Google Models')
            plt.ylabel('Battery Capacity (mAh)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_battery_google = google_df.nlargest(1, 'Battery_mAh').iloc[0]
            print("Google Phones - Battery Comparison:")
            print(google_df[['Model', 'Battery_mAh']].to_string(index=False))
            print("GOOGLE PHONE WITH BEST BATTERY:")
            print(f"Model: {best_battery_google['Model']}")
            print(f"Battery: {best_battery_google['Battery_mAh']} mAh")
            print(f"Price: ₹{best_battery_google['Price']:,}")
            pass
        if choice_3==6:
            google_df = sales_df[sales_df['Brand'] == 'Google'].sort_values('Warranty_Years')
            plt.figure(figsize=(10, 6))
            plt.bar(google_df['Model'], google_df['Warranty_Years'], color='brown')
            plt.title('Google Phones - Warranty Comparison', fontsize=14)
            plt.xlabel('Google Models')
            plt.ylabel('Warranty (Years)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_warranty_google = google_df.nlargest(1, 'Warranty_Years').iloc[0]
            print("Google Phones - Warranty Comparison:")
            print(google_df[['Model', 'Warranty_Years']].to_string(index=False))
            print("GOOGLE PHONE WITH BEST WARRANTY:")
            print(f"Model: {best_warranty_google['Model']}")
            print(f"Warranty: {best_warranty_google['Warranty_Years']} years")
            print(f"Price: ₹{best_warranty_google['Price']:,}")
            pass
        if choice_3==7:
            Google_df = sales_df[sales_df['Brand'] == 'Google'].sort_values('Customer_Rating')
            plt.barh(Google_df['Model'], Google_df['Customer_Rating'])
            plt.title('Google Customer Ratings')
            plt.show()
            highest = Google_df.nlargest(1, 'Customer_Rating').iloc[0]
            lowest = Google_df.nsmallest(1, 'Customer_Rating').iloc[0]
            print(f"Highest Rated: {highest['Model']} - {highest['Customer_Rating']}/5")
            print(f"Lowest Rated: {lowest['Model']} - {lowest['Customer_Rating']}/5")
            pass
        if choice_3==8:
            print('Do you really want to exit?')
            print('1 - Yes')
            print('2 - No')
            choice_1_1=int(input('Enter your choice:'))
            if choice_1_1==1:
                print('See you soon.Thank you!!!')
                break
            if choice_1_1==2:
                pass
    if choice_2==10:
        print('Parameters for Analysis:')
        print('1 - Price Comparison(Least and Most Expensive model)')
        print('2 - Best selling Samsung phone')
        print('3 - Storage comparison')
        print('4 - Camera comparison')
        print('5 - Battery comparison')
        print('6 - Warranty comparison')
        print('7 - Rating comparison')
        print('8 - Exit')
        choice_3=int(input('Enter your choice : '))
        if choice_3==1:
           nokia_df = sales_df[sales_df['Brand'] == 'Nokia'].sort_values('Price')
           plt.figure(figsize=(10, 6))
           plt.bar(nokia_df['Model'], nokia_df['Price'], color='blue')
           plt.title('Nokia Phones - Price Comparison', fontsize=14)
           plt.xlabel('Nokia Models')
           plt.ylabel('Price (₹)')
           plt.xticks(rotation=45)
           plt.grid(axis='y', linestyle='--', alpha=0.7)
           plt.tight_layout()
           plt.show()
           print("Nokia Phones - Price Comparison:")
           print(nokia_df[['Model', 'Price']].to_string(index=False))
           cheapest_nokia = nokia_df.iloc[0]  
           most_expensive_nokia = nokia_df.iloc[-1] 
           print(" CHEAPEST NOKIA PHONE:")
           print(f"Model: {cheapest_nokia['Model']}")
           print(f"Price: ₹{cheapest_nokia['Price']:,}")
           print(" MOST EXPENSIVE NOKIA PHONE:")
           print(f"Model: {most_expensive_nokia['Model']}")
           print(f"Price: ₹{most_expensive_nokia['Price']:,}")
           pass
        if choice_3==2:
           nokia_df = sales_df[sales_df['Brand'] == 'Nokia'].sort_values('Units_Sold')
           plt.figure(figsize=(10, 6))
           plt.bar(nokia_df['Model'], nokia_df['Units_Sold'], color='pink')
           plt.title('Nokia Phones - Units Sold', fontsize=14)
           plt.xlabel('Nokia Models')
           plt.ylabel('Units Sold')
           plt.xticks(rotation=45)
           plt.grid(axis='y', linestyle='--', alpha=0.7)
           plt.tight_layout()
           plt.show()
           best_selling_nokia = nokia_df.nlargest(1, 'Units_Sold').iloc[0]
           print("BEST SELLING NOKIA PHONE:")
           print(f"Model: {best_selling_nokia['Model']}")
           print(f"Units Sold: {best_selling_nokia['Units_Sold']:,}")
           print(f"Price: ₹{best_selling_nokia['Price']:,}")
           pass
        if choice_3==3:
            nokia_df = sales_df[sales_df['Brand'] == 'Nokia'].sort_values('Storage_GB')
            plt.figure(figsize=(10, 6))
            plt.bar(nokia_df['Model'], nokia_df['Storage_GB'], color='green')
            plt.title('Nokia Phones - Storage Comparison', fontsize=14)
            plt.xlabel('Nokia Models')
            plt.ylabel('Storage (GB)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            highest_storage_nokia = nokia_df.nlargest(1, 'Storage_GB').iloc[0]
            print("Nokia Phones - Storage Comparison:")
            print(nokia_df[['Model', 'Storage_GB']].to_string(index=False))
            print(" NOKIA PHONE WITH HIGHEST STORAGE:")
            print(f"Model: {highest_storage_nokia['Model']}")
            print(f"Storage: {highest_storage_nokia['Storage_GB']} GB")
            print(f"Price: ₹{highest_storage_nokia['Price']:,}")
            pass
        if choice_3==4:
            nokia_df = sales_df[sales_df['Brand'] == 'Nokia'].sort_values('Camera_MP')
            plt.figure(figsize=(10, 6))
            plt.bar(nokia_df['Model'], nokia_df['Camera_MP'], color='purple')
            plt.title('Nokia Phones - Camera Comparison', fontsize=14)
            plt.xlabel('Nokia Models')
            plt.ylabel('Camera Megapixels (MP)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_camera_nokia = nokia_df.nlargest(1, 'Camera_MP').iloc[0]
            print("Nokia Phones - Camera Comparison:")
            print(nokia_df[['Model', 'Camera_MP']].to_string(index=False))
            print("NOKIA PHONE WITH BEST CAMERA:")
            print(f"Model: {best_camera_nokia['Model']}")
            print(f"Camera: {best_camera_nokia['Camera_MP']} MP")
            print(f"Price: ₹{best_camera_nokia['Price']:,}")
            pass
        if choice_3==5:
            nokia_df = sales_df[sales_df['Brand'] == 'Nokia'].sort_values('Battery_mAh')
            plt.figure(figsize=(10, 6))
            plt.bar(nokia_df['Model'], nokia_df['Battery_mAh'], color='orange')
            plt.title('Nokia Phones - Battery Comparison', fontsize=14)
            plt.xlabel('Nokia Models')
            plt.ylabel('Battery Capacity (mAh)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_battery_nokia = nokia_df.nlargest(1, 'Battery_mAh').iloc[0]
            print("Nokia Phones - Battery Comparison:")
            print(nokia_df[['Model', 'Battery_mAh']].to_string(index=False))
            print("NOKIA PHONE WITH BEST BATTERY:")
            print(f"Model: {best_battery_nokia['Model']}")
            print(f"Battery: {best_battery_nokia['Battery_mAh']} mAh")
            print(f"Price: ₹{best_battery_nokia['Price']:,}")
            pass
        if choice_3==6:
            nokia_df = sales_df[sales_df['Brand'] == 'Nokia'].sort_values('Warranty_Years')
            plt.figure(figsize=(10, 6))
            plt.bar(nokia_df['Model'], nokia_df['Warranty_Years'], color='brown')
            plt.title('Nokia Phones - Warranty Comparison', fontsize=14)
            plt.xlabel('Nokia Models')
            plt.ylabel('Warranty (Years)')
            plt.xticks(rotation=45)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            best_warranty_nokia = nokia_df.nlargest(1, 'Warranty_Years').iloc[0]
            print("Nokia Phones - Warranty Comparison:")
            print(nokia_df[['Model', 'Warranty_Years']].to_string(index=False))
            print("NOKIA PHONE WITH BEST WARRANTY:")
            print(f"Model: {best_warranty_nokia['Model']}")
            print(f"Warranty: {best_warranty_nokia['Warranty_Years']} years")
            print(f"Price: ₹{best_warranty_nokia['Price']:,}")
            pass
        if choice_3==7:
            Nokia_df = sales_df[sales_df['Brand'] == 'Nokia'].sort_values('Customer_Rating')
            plt.barh(Nokia_df['Model'], Nokia_df['Customer_Rating'])
            plt.title('Nokia Customer Ratings')
            plt.show()
            highest = Nokia_df.nlargest(1, 'Customer_Rating').iloc[0]
            lowest = Nokia_df.nsmallest(1, 'Customer_Rating').iloc[0]
            print(f"Highest Rated: {highest['Model']} - {highest['Customer_Rating']}/5")
            print(f"Lowest Rated: {lowest['Model']} - {lowest['Customer_Rating']}/5")
            pass
        if choice_3==8:
            print('Do you really want to exit?')
            print('1 - Yes')
            print('2 - No')
            choice_1_1=int(input('Enter your choice:'))
            if choice_1_1==1:
                print('See you soon.Thank you!!!')
                break
            if choice_1_1==2:
                pass
    if choice_2==11:
            print('Do you really want to exit?')
            print('1 - Yes')
            print('2 - No')
            choice_1_1=int(input('Enter your choice:'))
            if choice_1_1==1:
                print('See you soon.Thank you!!!')
                break
            if choice_1_1==2:
                pass
if choice==3:
 while True:
    print('Methods of modifying:')
    print('1. Add a new record')
    print('2. Delete a record')
    print('3. Update a record')
    print('4. Continue without changes')
    edit_choice = int(input("Enter your choice: "))

    if edit_choice == 1:
        # Add new record
        new_data = {
            "Brand": input("Enter brand: "),
            "Model": input("Enter model name: "),
            "Price": int(input("Enter price: ")),
            "Units_Sold": int(input("Enter units sold: ")),
            "Revenue": int(input("Enter revenue: ")),
            "Camera_MP": int(input("Enter camera megapixels: ")),
            "Battery_mAh": int(input("Enter battery capacity (mAh): ")),
            "Storage_GB": int(input("Enter storage (GB): ")),
            "RAM_GB": int(input("Enter RAM (GB): ")),
            "Warranty_Years": int(input("Enter warranty (years): ")),
            "Customer_Rating": float(input("Enter customer rating (out of 5): ")),
            "Launch_Year": int(input("Enter launch year: "))
        }
        sales_df = pd.concat([sales_df, pd.DataFrame([new_data])], ignore_index=True)
        print('New record added successfully.')
        sales_df.to_csv("smartphone_sales.csv", index=False)
        print("Dataset updated successfully.")

    elif edit_choice == 2:
        # Delete record
        model_name = input("Enter the model name to delete: ")
        sales_df = sales_df[sales_df["Model"] != model_name]
        sales_df.to_csv("smartphone_sales.csv", index=False)
        print("Dataset updated successfully.")
        
    elif edit_choice == 3:
        # Update record
        model_name = input("Enter the model name to update: ")
        column = input("Enter the column to update(): ")
        new_value = input("Enter the new value: ")
        sales_df.loc[sales_df["Model"] == model_name, column] = new_value
        sales_df.to_csv("smartphone_sales.csv", index=False)
        print("Dataset updated successfully.")
    
    elif edit_choice == 4:
        print('Are you sure you do not want to make any changes?')
        print('1 - Yes')
        print('2 - No')
        choice_1_1=int(input('Enter your choice:'))
        if choice_1_1==1:
            print('See you soon.Thank you!!!')
            break
        if choice_1_1==2:
            pass
if choice==4:
 while True:
        print('See you soon.Thank you!!!')
        break
import csv
import asyncio
import os
from playwright.async_api import async_playwright

async def scraping(max_page = 24):
    async with async_playwright() as p:
        try:
            url = "https://ev-database.org/#group=vehicle-group&rs-pr=10000_100000&rs-er=0_1000&rs-ld=0_1000&rs-ac=2_23&rs-dcfc=0_400&rs-ub=10_200&rs-tw=0_3000&rs-ef=100_350&rs-sa=-1_5&rs-w=1000_3500&rs-c=0_5000&rs-y=2010_2030&s=1&p=0-50"
            browser = await p.chromium.launch(headless = False)
            page = await browser.new_page()
            await page.goto(url)
            await page.wait_for_selector('div.list.jplist-ready') 
            
            next_page = 1
            car_list = []
            
            while next_page <= max_page:
                car_datas = await page.query_selector_all('div.list-item')
                for car in car_datas:
                    try:
                    
                        # name
                        name_el = await car.query_selector('a.title span.hidden')
                        name = await name_el.inner_text() if name_el else "N/A"
                        
                        # km
                        range_el = await car.query_selector('div.specs span.erange_real')
                        range_km = await range_el.inner_text() if range_el else "N/A"
                        
                        # efishensiy
                        effinciency_el = await car.query_selector('div.specs span.efficiency')
                        efficiency = await effinciency_el.inner_text() if effinciency_el else "N/A"
                        
                        # weight
                        weight_el = await car.query_selector('div.specs span.weight.hidden')
                        weight = await weight_el.inner_text() if weight_el else "N/A"
                        
                        # acceleration(0-100)
                        acceleration_el = await car.query_selector('div.specs span.acceleration.hidden')
                        acceleration = await acceleration_el.inner_text() if acceleration_el else "N/A"
                        
                        # 1-stop range
                        stop_range_el = await car.query_selector('div.specs span.long_distance_total_sort.hidden')
                        stop_range = await stop_range_el.inner_text() if stop_range_el else 'N/A'
                        
                        #battery kWh
                        battery_el = await car.query_selector('div.specs span.battery.hidden')
                        battery = await battery_el.inner_text() if battery_el else "N/A"
                        
                        # fast charger kW
                        charger_el = await car.query_selector('div.specs span.fastcharge_speed.hidden')
                        charger = await charger_el.inner_text() if charger_el else "N/A"
                        
                        # Towing (kg)
                        towing_el = await car.query_selector('div.specs span.towweight.hidden')
                        towing = await towing_el.inner_text() if towing_el else "N/A"
                        
                        # Cargo volume (L)
                        cargo_el = await car.query_selector('div.specs span.cargosort.hidden')
                        cargo = await cargo_el.inner_text() if cargo_el else "N/A"
                        
                        # price/range(km)
                        price_range_el = await car.query_selector('div.specs span.priceperrange.hidden')
                        price_range = await price_range_el.inner_text() if price_range_el else "N/A"
                        
                        # price euro
                        price_euro_el = await car.query_selector('div.pricing span.country_de')
                        price = await price_euro_el.inner_text() if price_euro_el else "N/A"
                        
                        
                        
                        car_list.append({
                            "Name":name,
                            "Range_km":range_km,
                            "Efficiency": efficiency,
                            "Weight": weight,
                            "Acceleration(0-100)":acceleration,
                            "Firth_stop_range":stop_range,
                            "Battery_kWh":battery,
                            "Fast_charger(kW)":charger,
                            "Towing_kg":towing,
                            "Cargo_volume":cargo,
                            "Price/Range(km)":price_range,
                            'Price':price
                            
                        })
                        
                        
                        
                    except Exception as e:
                        print('Xatolik:', e)
                        
                next_button = await page.query_selector('div.pagination-nav-nextlast button[data-type="next"]')
                if not next_button:
                    break
                await next_button.click()
                await page.wait_for_selector('div.list.jplist-ready')
                next_page += 1
                
            await page.close()
            path = r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\ModularProgramProjects\finalProject\data\scraped_raw_data"
            # path = Path(r"C:\Users\bunyo\OneDrive\Desktop\AI_Course\webScraping\earthquake")
            full_path = os.path.join(path, "car_data.csv")
            
            with open(full_path,'w',newline="", encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=["Name","Range_km","Efficiency","Weight","Acceleration(0-100)","Firth_stop_range","Battery_kWh","Fast_charger(kW)","Towing_kg","Cargo_volume","Price/Range(km)","Price"])
                writer.writeheader()
                writer.writerows(car_list)
            
        except Exception as e:
            print(f"Xatolik boldiyu {e}")

asyncio.run(scraping())
import asyncio
import playwright
from playwright.async_api import async_playwright
import csv
import os
from pathlib import Path

async def scraper(max_page=1):
    async with async_playwright() as p:
        try:
            url = r"https://www.emsc.eu/Earthquake_data/index.php?view=1"
            browser = await p.chromium.launch(headless = False)
            page = await browser.new_page()
            await page.goto(url)
            
            await page.wait_for_timeout(5000)
            # accespt_button = await page.locator("a").filter(has_text="Accept").nth(1)
            # await accespt_button.click()
    
            await page.wait_for_selector('.content')
            
            
            Earth_list = []
            next_page = 1
            
            while next_page <= max_page:
                data_per_page = await page.query_selector_all('.sonly.normal')
                            
                for data in data_per_page:
                    try:
                        # date
                        date_el = await data.query_selector('.tbdate')
                        date = await date_el.inner_text() if date_el else "N/A"
                        
                        # latutate
                        lat_degree_el = await data.query_selector('.tblat')
                        lat_degree = await lat_degree_el.inner_text() if lat_degree_el else "N/A"
                        
                        # longitude
                        lon_degree_el = await data.query_selector('.tblon')
                        lon_degree = await lon_degree_el.inner_text() if lon_degree_el else "N/A"
                        
                        # depth km
                        depth_el = await data.query_selector('.tbdepth')
                        depth = await depth_el.inner_text() if depth_el else "N/A"
                        
                        # type
                        type_el = await data.query_selector('.tbtyp')
                        Type = await type_el.inner_text() if type_el else "N/A"
                        
                        # magnituda
                        magnituda_el = await data.query_selector('.tbmag2')
                        magnituda = await magnituda_el.inner_text() if magnituda_el else "N/A"
                        
                        # network
                        network_el = await data.query_selector('.tbnetw')
                        network = await network_el.inner_text() if network_el else "N/A"
            
                        # location
                        location_el = await data.query_selector('.tbreg')    
                        location = await location_el.inner_text() if location_el else "N/A"
                    
                        
                        Earth_list.append({
                            "Date": date,
                            "Location": location,
                            "Lat_degrees": lat_degree,
                            "Long_degrees":lon_degree,
                            "Depth":depth,
                            "Type":Type,
                            "Magnituda":magnituda,
                            "Network":network                  
                                            
                        })
                        
                    except Exception as e:
                        print(f"Xatolik bulli {e}")
                        
                next_button = page.locator('.pag.spes.spes1').nth(1)
                # await page.get_by_text("›").nth(1)
                if not next_button:
                    break
                
                await next_button.click()
                await page.wait_for_selector('.sonly.normal')
                
                next_page += 1  
            await page.close()
            
            path = Path(r"C:\Users\bunyo\onedrive\desktop\AI_Course\ModularProgramProjects\Second_week_project\offline_testing\data_for_offline_test\scraped_data")
            full_path = os.path.join(path, "new_earthquake.csv")
            
            with open(full_path,'w',newline="", encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=["Date","Location","Lat_degrees","Long_degrees","Depth","Type","Magnituda","Network"])
                writer.writeheader()
                writer.writerows(Earth_list)
                  
            # print(Earth_list)    
            
            
        except Exception as e:
            print(f"XAtolik {e}")
            
asyncio.run(scraper())
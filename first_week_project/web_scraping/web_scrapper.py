import playwright
import csv
import asyncio
from playwright.async_api import async_playwright

async def scraper(max_page=10):
    async with async_playwright() as p:
        try:
            url = 'https://www.topuniversities.com/world-university-rankings?items_per_page=150&sort_by=rank&order_by=asc'
            browser = await p.chromium.launch(headless = False)
            page = await browser.new_page()
            await page.goto(url, wait_until="domcontentloaded")   
               
            
            Univerlist = []
            page_number = 1    
            
            while page_number < max_page:
                
                await page.wait_for_selector('div.new-ranking-cards')
                
                datas = await page.query_selector_all('div.new-ranking-cards')
                for data in datas:
                    try:
                        
                        # 1 Reyting
                        rank_el = await data.query_selector('.rank-no')
                        rank = await rank_el.inner_text() if rank_el else "N/A"
                        
                        # 2 Umumiy ball
                        score_el = await data.query_selector('.rank-score')
                        score = await score_el.inner_text() if score_el else "N/A"
                        
                        # 3 Universitet nomi
                        name_el = await data.query_selector('a.uni-link')
                        name = await name_el.inner_text() if name_el else "N/A"
                        
                      
                        
                        # location
                        location_el = await data.query_selector('.location')
                        location_all = await location_el.inner_text() if location_el else "N/A"
                        location = location_all.split(',')[-1].strip()
                        
                        # 4 Academic Reputation
                        acad_rep_el = await data.query_selector('#academic-reputation')
                        acad_rep = await acad_rep_el.get_attribute('aria-valuenow') if acad_rep_el else "N/A"
                        
                        # 5 citations-per-faculty
                        Citations_per_faculty_el = await data.query_selector('#citations-per-faculty')
                        Citations_per_faculty = await Citations_per_faculty_el.get_attribute('aria-valuenow') if Citations_per_faculty_el else "N/A"
                        
                        
                        # 6 Chet ellik talabalar nisbati (International Student Ratio)
                        int_students_el = await data.query_selector('#international-student-ratio')
                        int_students = await int_students_el.get_attribute('aria-valuenow') if int_students_el else "N/A"
                        
                        # 7 faculty-student-ratio
                        faculty_student_ratio_el = await data.query_selector('#faculty-student-ratio')
                        faculty_student_ratio = await faculty_student_ratio_el.get_attribute('aria-valuenow') if faculty_student_ratio_el else "N/A"
                        
                        #8 employer-reputation
                        employer_reputation_el = await data.query_selector('#employer-reputation')
                        employer_reputation = await employer_reputation_el.get_attribute('aria-valuenow') if employer_reputation_el else "N/A"
                        
                        # 9 employment-outcomes
                        employment_outcomes_el = await data.query_selector('#employment-outcomes')
                        employment_outcomes = await employment_outcomes_el.get_attribute('aria-valuenow') if employment_outcomes_el else "N/A"
                        
                        # 10 international-faculty-ratio
                        international_faculty_ratio_el = await data.query_selector('#international-faculty-ratio')
                        international_faculty_ratio = await international_faculty_ratio_el.get_attribute('aria-valuenow') if international_faculty_ratio_el else "N/A"
                        
                        # 11 sustainability-score
                        sustainability_score_el = await data.query_selector('#sustainability-score') 
                        sustainability_score = await sustainability_score_el.get_attribute('aria-valuenow') if sustainability_score_el else "N/A"
                        
                        # 12 international-research-network
                        international_research_network_el = await data.query_selector('#international-research-network')
                        international_research_network = await international_research_network_el.get_attribute('aria-valuenow') if international_research_network_el else "N/A"
                        
                        
                        
                        
                        Univerlist.append({
                            "Rank":rank,
                            "Score":score,
                            "Name":name,
                            "Location":location,
                            "Citations_per_faculty":Citations_per_faculty,
                            "Acedemik Reputation":acad_rep,
                            "Students":int_students,
                            "faculty_student_ratio":faculty_student_ratio,
                            "employer_reputation":employer_reputation,
                            "employment_outcomes":employment_outcomes,
                            "international_faculty_ratio":international_faculty_ratio,
                            "sustainability_score":sustainability_score,
                            "international_research_network":international_research_network
                            
                        })
                    
                    except Exception as e:
                        print(f"Xatolik boldi {e}")
                        
                next_button = page.locator('.page-link.next')
                if not next_button:
                    break
                
                await next_button.click()
                await page.wait_for_selector('div.new-ranking-cards')
                # await page.wait_for_timeout(6000)
                page_number += 1
                
                
            await browser.close()   
            

            with open(f"_products.csv", "w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=["Rank", "Score", "Name", "Location", "Acedemik Reputation","Students","Citations_per_faculty","faculty_student_ratio","employer_reputation","employment_outcomes","international_faculty_ratio","sustainability_score","international_research_network"])
                writer.writeheader()
                writer.writerows(Univerlist)   
            
           
            
            
       
        except Exception as e:
            print(f"Xatolik boldi {e}")
            
        
        
asyncio.run(scraper())

#ui fluid selection dropdown

# page.locator('.perpage_dropdown_js').click()
# page.locator('.perpage_dropdown_js .item[data-value="150"]').click()

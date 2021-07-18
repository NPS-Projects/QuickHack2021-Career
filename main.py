from bs4 import BeautifulSoup as bs
from selenium import webdriver

# output file
output_filename = "Job_list.csv"

# headers = "Company, Job_Position, Salary, Location, Link"
headers = "Company, Job_Position, Location,"
f = open(output_filename, 'w')
f.write(headers)

# start browser
driver = webdriver.Chrome('./chromedriver.exe')

# Get all HTML
# jobstreet
job_street_url = "https://www.jobstreet.com.my/en/job-search/intern-jobs/?createdAt=14d&job-type=internship&salary=0&salary-max=2147483647&specialization=508"
driver.get(job_street_url)
jS_html = driver.page_source  # html file for JobStreet
driver.close()  # close after getting html file

# parse html into BeautifulSoup
jS_bs = bs(jS_html, "html.parser")
js_container = jS_bs.findAll("div", {"class": "sx2jih0 zcydq878"})
print(len(js_container))
for j in js_container:
    job_pos = j.find("div", {"class": "sx2jih0 _2j8fZ_0 sIMFL_0 _1JtWu_0"})
    job_data = str(j.find("span"))

    temp_data = job_data[job_data.find("title"):]
    start_index = temp_data.find("\">") + 2
    end_index = temp_data.find("</a>")
    
    job_company_str = temp_data[start_index:end_index]

    if job_pos is not None:
        print(job_pos.string)
        
    print(job_company_str)

# job_company = jS_bs.findAll("div", {"class":'sx2jih0 zcydq82b _18qlyvc0 _18qlyvcv _18qlyvc1 _18qlyvc8'})
# job_position = jS_bs.findAll("div", {"class":'sx2jih0 _2j8fZ_0 sIMFL_0 _1JtWu_0'})
# job_location = jS_bs.findAll("div", {"class":'sx2jih0 zcydq82b zcydq8r iwjz4h0'})
# print(len(job_company),len(job_position), len(job_location))
# job_link = jS_bs.findAll()
# print((job_position))
# find each job from page


# job_street_html = job_street_client.read()
# job_street_client.close()
# jobStreet_soup = BeautifulSoup(job_street_html, "html.parser")
# print(jobStreet_soup.h1)
